from Core.AbstractRnnCore import AbstractRnnCore
from Core.IODevice import WordConnectionsIODevice
from PyQt5.QtCore import pyqtSignal
from Core.Params import CommonParams
import numpy as np
import datetime
from PyQt5 import QtCore
import math
import json

vexp = np.vectorize(math.exp)


class Rnn1Core(AbstractRnnCore):
    signalPlot = pyqtSignal(list)
    signal_autoCopy = pyqtSignal()

    def __init__(self, common_params: CommonParams, rnn_params):
        super(Rnn1Core, self).__init__(common_params, rnn_params)

        self.io_device = WordConnectionsIODevice(
            self.common_params.d, self.common_params.q)
        self.io_device.set_dictionary_filename(
            self.rnn_params.dictionary_filename)
        self.io_device.set_input_data_filename(
            self.rnn_params.input_data_filename)

        if self.common_params.processing_type != 'Novelty filter':
            self.snp_g = np.zeros(self.snp_shape, dtype=np.float64)
        else:
            self.snp_g = np.zeros(self.snp_shape, dtype=np.bool)
            self.prev_changed_snps_matrix = np.zeros(
                self.snp_g.shape, dtype=np.bool)

        self.weights_history = []

        self.ssps_history = []
        self.neu_states_history = []

        self.last_iterator_value = -1

        self.copied = False

        self.cntr = 0

        self.to_day_str = None

    def start_process_signals(self):
        self.cntr = 0
        self.weights_history = []
        self.last_iterator_value = -1
        today = datetime.datetime.today()
        self.to_day_str = today.strftime("%Y-%m-%d-%H-%M-%S")
        super(Rnn1Core, self).start_process_signals()

    def analyze_rnn_state(self):
        if self.common_params.processing_type == 'Novelty filter':
            self.ssps_history.append(self.SSPs.copy())
            self.neu_states_history.append(self.neu_states.copy())
            while len(
                    self.ssps_history) > self.common_params.rnn2DelayNumTacts:
                del self.ssps_history[0]
                del self.neu_states_history[0]

    def finish_process_signals(self):
        super(Rnn1Core, self).finish_process_signals()

        self.io_device.reset()

        if self.common_params.processing_type == 'Novelty filter' and len(
                self.weights_history):
            self.signalPlot.emit(self.weights_history)
            self.weights_history = []

    def copy_model(self):
        if self.copied:
            return
        self.copied = True
        model_dict = dict()
        model_dict['io_device'] = self.io_device.get_io_device_state()
        model_dict['io_device']['mode'] = self.common_params.processing_type
        model_dict['SSPs'] = self.SSPs
        model_dict['sspTact'] = self.sspTact
        model_dict['neu_states'] = np.copy(self.neu_states)
        model_dict['to_day_str'] = self.to_day_str

        model_dict['snp_k'] = np.copy(self.snp_k)
        if self.common_params.continuous_mode:
            self.signalNextTact.disconnect(self.process_signals)
        self.signalModel.emit(model_dict)

    def rnn2finished(self):
        self.copied = False

        if self.common_params.continuous_mode:
            self.signalNextTact.connect(
                self.process_signals, QtCore.Qt.QueuedConnection)
            self.signalNextTact.emit()

    def clear_rnn(self):
        self.weights_history = []
        self.last_iterator_value = -1

        super(Rnn1Core, self).clear_rnn()

        if self.common_params.processing_type != 'Novelty filter':
            self.snp_g = np.zeros(self.snp_shape, dtype=np.float64)
        else:
            self.snp_g = np.zeros(self.snp_shape, dtype=np.bool)

    def emit_neurones_single_pulses(self):
        for item in self.SSPs:
            if item == self.route[len(self.route) - 1]:
                continue

            route_ssp_index = self.route.index(item)
            tmp_indexes = self.future_route_indexes[route_ssp_index]

            if self.rnn_params.flag_clear_learning:
                # direct synaps emitting only
                self.neu_current_values[route_ssp_index + 1, np.logical_or(
                    self.neu_states[route_ssp_index, :, :] == -1,
                    self.neu_states[route_ssp_index, :, :] ==
                    self.common_params.refract_interval)] = \
                    self.common_params.neuron_current_value_limit

            else:
                for id in range(self.common_params.d):
                    for iq in range(self.common_params.q):
                        if self.neu_states[route_ssp_index, id, iq] == -1:
                            for ind in tmp_indexes:
                                if not self.route[ind] in self.future_SSPs:
                                    continue
                                if ind == route_ssp_index + 1:
                                    # only direct synapses
                                    self.neu_current_values[ind, np.logical_or(
                                        self.neu_states[
                                            route_ssp_index, :, :] == -1,
                                        self.neu_states[
                                            route_ssp_index, :, :] ==
                                        self.common_params.
                                        refract_interval)] += 1
                                else:
                                    self.neu_current_values[
                                        ind, :, :] += \
                                        self.snp_k[
                                        route_ssp_index, id, iq,
                                        tmp_indexes.index(ind),
                                            :, :] * self.snp_b[
                                            route_ssp_index,
                                            tmp_indexes.index(ind)]

    def learn_rnn(self):

        if not self.rnn_params.flag_learning:
            return

        # refresh g param
        for dst_ssp in self.SSPs:
            dst_route_index = self.route.index(dst_ssp)
            src_route_indexes = self.past_route_indexes[dst_route_index]

            g_inc, g_dec = 0.0, 0.0
            if self.rnn_params.gSum != -1:
                # calc gInc and gDec values automatically
                g_plus, g_minus = 0, 0
                for src_route_index in src_route_indexes:
                    if src_route_index == len(self.route) - 1:
                        continue
                    g_minus += np.sum(
                        self.neu_states[src_route_index, :, :] == 0)
                    g_plus += np.sum(
                        self.neu_states[src_route_index, :, :] == 1)
                g_plus -= 1  # direct synaps

                if g_plus == 0 or g_minus == 0:
                    # there is no possibility of potential distribution. do not
                    # train
                    pass
                else:
                    g_inc = float(self.rnn_params.gSum) / g_plus
                    g_dec = float(self.rnn_params.gSum) / g_minus
            else:
                g_inc = self.rnn_params.gInc
                g_dec = self.rnn_params.gDec

            for src_route_index in src_route_indexes:
                if src_route_index == len(self.route) - 1:
                    continue
                if dst_route_index - src_route_index == 1:
                    continue

                tmp_indexes = self.future_route_indexes[src_route_index]
                for dst_id in range(self.common_params.d):
                    for dst_iq in range(self.common_params.q):
                        if self.neu_states[dst_route_index, dst_id,
                                           dst_iq] != \
                                -1:  # if dst neu not active
                            continue

                        # if src neu waiting (was waiting)
                        if np.sum(self.neu_states[src_route_index, :, :] == 0):

                            if self.common_params.processing_type != \
                                    'Novelty filter':  # temporary solution!!!
                                self.snp_g[src_route_index,
                                           self.neu_states[src_route_index,
                                                           :,
                                                           :] == 0,
                                           tmp_indexes.index(dst_route_index),
                                           dst_id,
                                           dst_iq] -= g_dec
                                self.snp_k[src_route_index,
                                           self.neu_states[src_route_index,
                                                           :,
                                                           :] == 0,
                                           tmp_indexes.index(dst_route_index),
                                           dst_id,
                                           dst_iq] = \
                                    2.0 / (1.0 + vexp(
                                        -self.rnn_params.gamma *
                                        self.snp_g[src_route_index,
                                                   self.neu_states[
                                                       src_route_index,
                                                       :, :] == 0,
                                                   tmp_indexes.index(
                                                       dst_route_index),
                                                   dst_id,
                                                   dst_iq])) - 1.0

                        # if src neu start refract (was active)
                        if np.sum(self.neu_states[src_route_index, :, :] == 1):
                            if self.common_params.processing_type != \
                                    'Novelty filter':  # temporary solution!!!
                                self.snp_g[src_route_index,
                                           self.neu_states[src_route_index,
                                                           :,
                                                           :] == 1,
                                           tmp_indexes.index(dst_route_index),
                                           dst_id,
                                           dst_iq] += g_inc
                                self.snp_k[
                                    src_route_index,
                                    self.neu_states[
                                        src_route_index,
                                        :,
                                        :] == 1,
                                    tmp_indexes.index(dst_route_index),
                                    dst_id,
                                    dst_iq] = \
                                    2.0 \
                                    / (1.0 + vexp(
                                        -self.rnn_params.gamma *
                                        self.snp_g[src_route_index,
                                                   self.neu_states[
                                                       src_route_index,
                                                       :, :] == 1,
                                                   tmp_indexes.index(
                                                       dst_route_index),
                                                   dst_id,
                                                   dst_iq])) - 1.0
                            else:
                                self.snp_g[src_route_index,
                                           self.neu_states[src_route_index,
                                                           :,
                                                           :] == 1,
                                           tmp_indexes.index(dst_route_index),
                                           dst_id,
                                           dst_iq] = True

        if self.common_params.processing_type == 'Novelty filter':
            # calc firsttime changed synapses
            changed_snps_matrix = np.logical_and(
                self.snp_g, np.logical_not(
                    self.prev_changed_snps_matrix))  # for g_dec == 0 !!!!
            self.prev_changed_snps_matrix = np.copy(self.snp_g)
            changed_snps = np.sum(changed_snps_matrix)

            if self.sspTact == 1:
                print('changed_snps', changed_snps)
                self.weights_history.append(changed_snps)

            self.analyze_weights_history_dynamics(changed_snps_matrix)

        elif self.common_params.processing_type == 'Predict':
            self.cntr += 1
            if self.cntr == 35 * 4 or self.cntr == 40 * 4 or \
                    self.cntr == 45 * 4:
                self.signal_autoCopy.emit()

    def analyze_weights_history_dynamics(self, changed_snps_matrix):
        if len(self.weights_history) <= \
                self.common_params.initHistoryPeriod + 1:
            return
        mean_history = np.mean(
            np.array(self.weights_history[0:len(self.weights_history) - 1]))
        print('mean_history',
              int(mean_history * self.common_params.novFiltDetectBorder),
              'now history',
              self.weights_history[len(self.weights_history) - 1])
        if self.weights_history[len(
                self.weights_history) - 1] < \
                mean_history * self.common_params.novFiltDetectBorder:
            return

        if self.io_device.iterator == self.last_iterator_value:
            return
        self.last_iterator_value = self.io_device.iterator

        if self.common_params.initHistoryPeriod <= \
                self.common_params.rnn2DelayNumTacts:
            print(
                'self.common_params.initHistoryPeriod <= '
                'self.common_params.rnn2DelayNumTacts')
            return

        model_dict = dict()
        model_dict['io_device'] = self.io_device.get_io_device_state()
        model_dict['io_device']['mode'] = self.common_params.processing_type
        model_dict['SSPs'] = self.ssps_history[0]
        model_dict['sspTact'] = (self.sspTact + 1 -
                                 self.common_params.rnn2DelayNumTacts) % \
            self.common_params.ssp_interval
        model_dict['neu_states'] = np.copy(self.neu_states_history[0])
        model_dict['to_day_str'] = self.to_day_str

        model_dict['snp_k'] = np.zeros(self.snp_shape, dtype=np.float64)
        model_dict['snp_k'][changed_snps_matrix] = \
            self.common_params.novFiltWeightsGain

        if self.common_params.continuous_mode:
            self.signalNextTact.disconnect(self.process_signals)
        self.signalModel.emit(model_dict)

    def refresh_params(self, params: str):
        super(Rnn1Core, self).refresh_params(params)

        params = json.loads(params)

        self.rnn_params.gInc = params['gInc']
        self.rnn_params.gDec = params['gDec']

        self.rnn_params.flag_learning = params['flag_learning']
        self.rnn_params.flag_clear_learning = params['flag_clear_learning']

        if params['input_data_filename'] != \
                self.rnn_params.input_data_filename:
            # io_refresh_is_needed
            self.finish_process_signals()
            self.rnn_params.input_data_filename = params['input_data_filename']
            self.io_device.set_input_data_filename(
                self.rnn_params.input_data_filename)

        self.rnn_params.rewrite()
