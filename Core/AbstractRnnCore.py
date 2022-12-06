import json
import numpy as np

from PyQt5 import QtCore
from Core.Params import CommonParams
from Core.SupportFunctions import init_route
from PyQt5.QtCore import pyqtSignal
import math

vexp = np.vectorize(math.exp)


# abstract class with general RNN functionality
class AbstractRnnCore(QtCore.QObject):
    signalVisualize = pyqtSignal(np.ndarray)
    signalClearVisualize = pyqtSignal()
    signalNextTact = pyqtSignal()
    signalModel = pyqtSignal(dict)

    def __init__(self, common_params: CommonParams, rnn_params):
        super(AbstractRnnCore, self).__init__()

        self.SSPs = None
        self.future_SSPs = None
        self.current_border = None
        self.sspTact = 0
        self.neu_current_values = None
        self.neu_states = None

        self.common_params = common_params
        self.rnn_params = rnn_params

        self.route = init_route(
            self.common_params.route_type,
            self.common_params.L,
            self.common_params.M)
        self.output_fields = []

        # init layers and ssps
        self.clear_layers()

        # future_fields_combinations
        self.future_route_indexes = dict()
        for i in range(len(self.route) - 1):
            field_indexes_next_tact = (i + 1) % self.common_params.ssp_interval
            tmp_route_indexes = []
            for j in range(
                field_indexes_next_tact, len(
                    self.route), self.common_params.ssp_interval):
                tmp_route_indexes.append(j)
            self.future_route_indexes[i] = tmp_route_indexes

        # past_fields_combinations
        self.past_route_indexes = dict()
        for i in range(1, len(self.route)):
            field_indexes_prev_tact = (i - 1) % self.common_params.ssp_interval
            tmp_route_indexes = []
            for j in range(
                field_indexes_prev_tact, len(
                    self.route), self.common_params.ssp_interval):
                tmp_route_indexes.append(j)
            self.past_route_indexes[i] = tmp_route_indexes

        # max_connected_route_indexes
        self.max_connected_route_indexes = 0
        for i in range(len(self.future_route_indexes)):
            if len(self.future_route_indexes[i]
                   ) > self.max_connected_route_indexes:
                self.max_connected_route_indexes = len(
                    self.future_route_indexes[i])

        self.snp_shape = (len(self.route),
                          self.common_params.d,
                          self.common_params.q,
                          self.max_connected_route_indexes,
                          self.common_params.d,
                          self.common_params.q)

        # synaps
        self.snp_k = np.zeros(self.snp_shape, dtype=np.float64)

        # init gain distance coeffs (snp_b)
        self.snp_b = np.zeros(
            (len(
                self.route),
                self.max_connected_route_indexes),
            dtype=np.float64)
        self.init_distance_gain_coeffs()

        # connects
        self.signalNextTact.connect(
            self.process_signals,
            QtCore.Qt.QueuedConnection)
        self.flag_draw_answer_is_needed = 0  # synchronize with graphics module

        self.flag_processing = True

    def init_distance_gain_coeffs(self):
        for i in range(len(self.route) - 1):
            if i == len(self.route) - 1:
                l_shift = self.route[0]['L'] - \
                    self.route[len(self.route) - 1]['L']
                m_shift = self.route[0]['M'] - \
                    self.route[len(self.route) - 1]['M']
            else:
                l_shift = self.route[i + 1]['L'] - self.route[i]['L']
                m_shift = self.route[i + 1]['M'] - self.route[i]['M']

            for j in range(len(self.future_route_indexes[i])):
                y_distance = self.route[self.future_route_indexes[i][
                    j]]['L'] - self.route[i]['L'] - l_shift
                x_distance = self.route[self.future_route_indexes[i][
                    j]]['M'] - self.route[i]['M'] - m_shift

                distance = (((y_distance * self.common_params.d)**2) +
                            ((x_distance * self.common_params.q)**2))**0.5

                self.snp_b[i, j] = \
                    1.0 / (1.0 + self.rnn_params.alpha *
                           (distance**(1.0 / self.rnn_params.h)))

    def start_process_signals(self):
        self.finish_process_signals()

        self.flag_processing = True

        self.get_next_ssp()

        if self.common_params.draw_layers:
            if self.common_params.continuous_mode:
                self.flag_draw_answer_is_needed = 2
            self.signalVisualize.emit(self.neu_states)
        if self.common_params.continuous_mode:
            if not self.common_params.draw_layers:
                self.signalNextTact.emit()

    def process_signals(self):

        if not self.flag_processing:
            self.finish_process_signals()
            return False

        if not len(self.SSPs):
            self.finish_process_signals()
            return False

        # step 1: get outputs
        for item in self.rnn_params.output_fields:
            if item in self.SSPs:
                self.io_device.send_ssp_to_output(self.route.index(
                    item), self.neu_states[self.route.index(item), :, :])

        # Step 1.5: define next tact ssps fields
        self.future_SSPs = []
        for item in self.SSPs:
            new_ssp_index = self.route.index(item) + 1
            if new_ssp_index < len(self.route):
                self.future_SSPs.append(self.route[new_ssp_index])

        # step 2: emitting signals
        self.emit_neurones_single_pulses()

        # step3
        self.SSPs = self.future_SSPs

        # step 4: Define borders
        self.calc_borders()

        # step 5: neu states refresh
        self.neu_states[self.neu_states > 0] += 1
        self.neu_states[self.neu_states > 0] %= (
            self.common_params.refract_interval + 1)
        self.neu_states[self.neu_states == -1] = 1
        self.neu_states[np.logical_and(
            self.neu_current_values >
            self.current_border, self.neu_states == 0)] = -1
        self.neu_current_values[:, :, :] = 0

        # step 6: learn
        self.learn_rnn()

        # step 7: next ssp submit
        self.get_next_ssp()

        # step8: analyze rnn state (for novelty filer)
        self.analyze_rnn_state()

        if self.common_params.draw_layers:
            if self.common_params.continuous_mode:
                self.flag_draw_answer_is_needed = 2
            self.signalVisualize.emit(self.neu_states)
        if self.common_params.continuous_mode:
            if not self.common_params.draw_layers:
                self.signalNextTact.emit()

        return True

    def drawed(self):
        if self.common_params.continuous_mode:
            if self.flag_draw_answer_is_needed != 0:
                self.flag_draw_answer_is_needed -= 1
                if self.flag_draw_answer_is_needed == 0:
                    self.signalNextTact.emit()

    def finish_process_signals(self):

        self.flag_processing = False

        self.clear_layers()
        if self.common_params.draw_layers:
            self.signalClearVisualize.emit()

    def clear_layers(self):
        self.SSPs = []
        self.future_SSPs = []
        self.sspTact = 0  # if 0, than it tact for new ssp subbitting
        # neurones
        self.neu_current_values = np.zeros(
            (len(
                self.route),
                self.common_params.d,
                self.common_params.q),
            dtype=np.float64)
        # 0 - waiting, -1 - active, 1...N - refract
        self.neu_states = np.zeros(
            (len(
                self.route),
                self.common_params.d,
                self.common_params.q),
            dtype=np.int8)

    def clear_rnn(self):
        self.finish_process_signals()

        self.snp_k = np.zeros(
            (len(
                self.route),
                self.common_params.d,
                self.common_params.q,
                self.max_connected_route_indexes,
                self.common_params.d,
                self.common_params.q),
            dtype=np.float64)

    def get_next_ssp(self):
        if self.sspTact == 0:
            ssp = self.io_device.get_ssp_from_input()
            if len(ssp):
                self.neu_states[0, self.neu_states[0] ==
                                0] = ssp[self.neu_states[0] == 0] * -1
                self.SSPs.append(self.route[0])
        self.sspTact = (self.sspTact + 1) % self.common_params.ssp_interval

    def calc_borders(self):
        if self.rnn_params.flag_clear_learning:
            self.current_border = \
                self.common_params.neuron_current_value_limit - 1.0
            return
        if self.rnn_params.border_type == 'Const':
            self.current_border = self.rnn_params.border_Const_value
        elif self.rnn_params.border_type == 'Concurrent':

            self.current_border = \
                self.common_params.neuron_current_value_limit - 1.0

            # for each ssp define neus with max neu_current_values
            for ssp in self.SSPs:

                if self.rnn_params.border_Concurrent_winners <= 0:
                    self.neu_current_values[self.route.index(ssp)] = 0
                    continue

                if self.rnn_params.border_Concurrent_winners >= \
                        self.common_params.data_block_size:
                    self.neu_current_values[self.route.index(
                        ssp)] = self.common_params.neuron_current_value_limit
                    continue

                local_current_vals = self.neu_current_values[self.route.index(
                    ssp), :, :]
                if np.abs(
                        np.max(local_current_vals) -
                        np.min(local_current_vals)) < 1e-10:
                    print('all neurones have equal current values, '
                          'nothing to activate')
                    self.neu_current_values[self.route.index(ssp), :, :] = 0
                    continue

                local_current_vals_sorted = np.sort(
                    local_current_vals.reshape(
                        self.common_params.data_block_size))

                current_border_index = self.common_params.data_block_size - \
                    self.rnn_params.border_Concurrent_winners
                current_border_value = \
                    local_current_vals_sorted[current_border_index]

                index_min = current_border_index
                index_max = current_border_index
                while np.abs(
                        current_border_value -
                        local_current_vals_sorted[index_min]) < \
                        1e-10 and index_min > 0:
                    index_min -= 1
                while np.abs(current_border_value -
                             local_current_vals_sorted[index_max]) < \
                        1e-10 and index_max < \
                        self.common_params.data_block_size - 1:
                    index_max += 1

                # nearest
                if current_border_index - index_min <= \
                        index_max - current_border_index:
                    index2 = index_min
                else:
                    index2 = index_max

                # border_value
                calculated_border = (local_current_vals_sorted[index2] +
                                     local_current_vals_sorted
                                     [current_border_index]) / 2.0
                self.neu_current_values[self.route.index(ssp),
                                        self.neu_current_values
                                        [self.route.index(ssp), :, :] >=
                                        calculated_border] = \
                    self.common_params.neuron_current_value_limit

        else:
            print('ERROR: Uncorrect border type')

    def refresh_processing_params(self, params: str):

        params = json.loads(params)

        self.common_params.processing_type = params['processing_type']
        self.common_params.predictStepsNum = params['predictStepsNum']
        self.common_params.novFiltWeightsGain = params['novFiltWeightsGain']
        self.common_params.novFiltDetectBorder = params['novFiltDetectBorder']
        self.common_params.novFiltStepsNum = params['novFiltStepsNum']

    def refresh_params(self, params: str):

        params = json.loads(params)

        betas_refresh_is_needed = False
        if self.rnn_params.alpha != params['alpha']:
            betas_refresh_is_needed = True
            self.rnn_params.alpha = params['alpha']
        if self.rnn_params.h != params['h']:
            betas_refresh_is_needed = True
            self.rnn_params.h = params['h']
        if betas_refresh_is_needed:
            self.init_distance_gain_coeffs()

        self.rnn_params.border_type = params['border_type']
        self.rnn_params.border_Const_value = params['border_Const_value']
        self.rnn_params.border_Concurrent_winners = \
            params['border_Concurrent_winners']

        self.rnn_params.rewrite()
