from Core.AbstractRnnCore import AbstractRnnCore
from PyQt5.QtCore import pyqtSignal
from Core.Params import CommonParams, RnnParams
from Core.IODevice import WordConnectionsIODevice
import numpy as np
from typing import Dict


class Rnn2Core(AbstractRnnCore):

    signalFinished = pyqtSignal()

    def __init__(self, common_params: CommonParams, rnn_params: RnnParams):
        super(Rnn2Core, self).__init__(common_params, rnn_params)

        self.io_device = WordConnectionsIODevice(self.common_params.d,
                                                 self.common_params.q)

        self.SSPs = None
        self.neu_states = None
        self.sspTact = None
        self.to_day_str = None

    def emit_neurones_single_pulses(self):
        for item in self.SSPs:
            if item == self.route[len(self.route)-1]:
                continue

            route_ssp_index = self.route.index(item)
            tmp_indexes = self.future_route_indexes[route_ssp_index]

            for id in range(self.common_params.d):
                for iq in range(self.common_params.q):
                    if self.neu_states[self.route.index(item), id, iq] == -1:
                        for ind in tmp_indexes:
                            if not self.route[ind] in self.future_SSPs:
                                continue
                            if ind == route_ssp_index + 1:
                                # only direct synapses
                                self.neu_current_values[
                                    route_ssp_index + 1, np.logical_or(
                                        self.neu_states[
                                            route_ssp_index, :, :] == -1,
                                        self.neu_states[
                                            route_ssp_index, :, :] ==
                                        self.common_params.
                                        refract_interval)] += 1
                            else:
                                self.neu_current_values[ind, :, :] += \
                                    self.snp_k[route_ssp_index, id, iq,
                                               tmp_indexes.index(ind),
                                               :, :] * \
                                    self.snp_b[route_ssp_index,
                                               tmp_indexes.index(ind)]

    def learn_rnn(self):
        pass

    def analyze_rnn_state(self):
        pass

    # get copied rnn1 state
    def paste_model(self, model_dict: Dict):

        self.flag_processing = True

        self.snp_k = model_dict['snp_k']
        self.SSPs = model_dict['SSPs']
        self.neu_states = model_dict['neu_states']
        self.sspTact = model_dict['sspTact']
        if model_dict['io_device']['mode'] == 'Novelty filter':
            model_dict['io_device']['iterator'] -= 1
        self.io_device.set_io_device_state(model_dict['io_device'])
        self.to_day_str = model_dict['to_day_str']

        if model_dict['processing_type'] == 'Predict':
            self.io_device.modify_for_predict(
                model_dict['predictStepsNum'])
        elif model_dict['processing_type'] == 'Novelty filter':
            self.io_device.modify_for_novelty_filter(
                self.common_params.rnn2DelayNumTacts,
                model_dict['novFiltStepsNum'])

        if self.common_params.draw_layers:
            if self.common_params.continuous_mode:
                self.flag_draw_answer_is_needed = 2
            self.signalVisualize.emit(self.neu_states)
        if self.common_params.continuous_mode:
            if not self.common_params.draw_layers:
                self.signalNextTact.emit()

    def finish_process_signals(self):

        self.flag_processing = False

        self.clear_layers()
        if self.common_params.draw_layers:
            self.signalClearVisualize.emit()

        self.signalFinished.emit()

        if self.common_params.processing_type == 'Predict':
            self.io_device.analyze_outputs_predict(
                self.common_params.predictStepsNum, self.to_day_str)
        elif self.common_params.processing_type == 'Novelty filter':
            self.io_device.analyze_outputs_novelty_filter(
                self.common_params.novFiltStepsNum)

        self.io_device.reset()
