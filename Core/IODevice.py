import datetime
import numpy as np
import os
from Support.words_support import convert_input_to_ssps, \
    convert_words_to_ssps, words_pe0_pe1


class AbstractIODevice:

    def __init__(self, d: int, q: int):
        self.input_sample = []
        self.output_samples_dict = dict()
        self.iterator = 0
        self.d = d
        self.q = q

        self.reset()

        self.etalon_sample = None

    def get_io_device_state(self):
        pass

    def set_io_device_state(self, state):
        pass

    def encode(self, sample):
        pass

    def decode(self, ssp):
        pass

    def get_ssp_from_input(self):
        pass

    def send_ssp_to_output(self, output_field, ssp):
        pass

    def set_input_data_filename(self, filename):
        pass

    def set_dictionary_filename(self, filename):
        pass

    def reset(self):
        self.iterator = 0
        self.output_samples_dict = dict()

    def modify_for_predict(self, num):
        self.etalon_sample = []
        if len(self.input_sample) >= (self.iterator + num) * self.d * self.q:
            self.etalon_sample = np.copy(
                self.input_sample[self.iterator *
                                  self.d * self.q:
                                  (self.iterator + num) * self.d * self.q])
        self.input_sample = self.input_sample[0:
                                              self.iterator * self.d * self.q]
        self.input_sample = np.concatenate(
            (self.input_sample, np.zeros(num * self.d * self.q)))

    def modify_for_novelty_filter(self, shift, num):
        self.input_sample = self.input_sample[0:min(
            (self.iterator + num) * self.d * self.q, len(self.input_sample))]


class WordConnectionsIODevice(AbstractIODevice):

    def __init__(self, d: int, q: int):
        super(WordConnectionsIODevice, self).__init__(d, q)

        self.words_dictionary = []

    def set_dictionary_filename(self, dictionary_file):
        with open(dictionary_file, "r") as dict_file:
            lst = dict_file.read().split('\n')
            self.words_dictionary = []
            for entry in lst:
                if entry.strip() != '':
                    self.words_dictionary.append(entry)

    def get_io_device_state(self):

        return {'input_sample': np.copy(self.input_sample),
                'iterator': self.iterator,
                'words_dictionary': self.words_dictionary}

    def set_io_device_state(self, state):
        self.input_sample = state['input_sample']
        self.output_samples_dict = dict()
        self.iterator = state['iterator']
        self.words_dictionary = state['words_dictionary']

    def encode(self, sample):
        if len(sample) < self.d * self.q:
            print('uncorrect input data')
            return []
        return np.reshape(sample, (self.d, self.q))

    def decode(self, ssp):
        ssp_reshaped = ssp.copy().reshape(self.d * self.q)
        ssp_decoded = ''
        for i in range(len(ssp_reshaped)):
            if ssp_reshaped[i] == -1:
                ssp_decoded += '\n'
                ssp_decoded += self.words_dictionary[i]
        return ssp_decoded

    def get_ssp_from_input(self):
        print('iterator = ', self.iterator)
        if self.iterator >= len(self.input_sample) / (self.d * self.q):
            return []
        ret = self.encode(
            self.input_sample[self.d * self.q * self.iterator:
                              self.d * self.q * (self.iterator + 1)])
        self.iterator += 1
        return ret

    def send_ssp_to_output(self, output_field_route_index, ssp):
        if output_field_route_index not in self.output_samples_dict.keys():
            self.output_samples_dict[output_field_route_index] = []
        print(
            'output step',
            self.iterator,
            'in field',
            output_field_route_index)
        self.output_samples_dict[output_field_route_index].append(
            self.decode(ssp))

    def set_input_data_filename(self, input_data_filename):
        self.reset()
        print(input_data_filename)
        if not os.path.exists(input_data_filename):
            print('ERROR: file', input_data_filename, ' not exists')
            return
        with open(input_data_filename) as f:
            file_data = f.read()
            self.input_sample = []
            for i in range(len(file_data)):
                if file_data[i] == "0":
                    self.input_sample.append(0)
                elif file_data[i] == "1":
                    self.input_sample.append(1)

    def analyze_outputs_predict(self, last_steps_num, to_day_str):
        print('analyzing predict...')
        for field_id in self.output_samples_dict.keys():
            len0 = len(self.output_samples_dict[field_id])
            if len0 < last_steps_num or not len0:
                print(
                    f'in field {field_id} not '
                    f'enough output data samples for analyzing')
                continue
            if len0 > len(self.input_sample):
                print('cannot calc accuracy forecasting: '
                      'len0 > len(self.input_sample)')
                continue
            output_last_steps = \
                self.output_samples_dict[field_id][len0 -
                                                   last_steps_num:len0]
            pred_ssps = []
            real_ssps = []
            for i in range(len(output_last_steps)):
                pred_ssps.append(
                    convert_words_to_ssps(
                        self.words_dictionary,
                        output_last_steps[i]))
                real_ssps.append(convert_input_to_ssps(
                    self.input_sample[i * self.d * self.q:
                                      (i + 1) * self.d * self.q]))

            words_pe0_pe1(
                real_ssps,
                pred_ssps,
                field_id,
                self.iterator -
                last_steps_num -
                1,
                to_day_str)

    def analyze_outputs_novelty_filter(self, last_steps_analyzed):
        print('analyzing novelty filter...')
        for field_id in self.output_samples_dict.keys():
            len0 = len(self.output_samples_dict[field_id])
            if len0 < last_steps_analyzed or not len0:
                print(
                    f'in field {field_id} not '
                    f'enough output data samples for analyzing')
                continue
            field_last_steps = \
                self.output_samples_dict[field_id][len0 -
                                                   last_steps_analyzed:len0]
            today = datetime.datetime.today()
            to_day_str = today.strftime("%Y-%m-%d-%H-%M-%S")
            if not os.path.exists('results_noveltyFiltering'):
                os.mkdir('results_noveltyFiltering')
            f = open(f'results_noveltyFiltering/results_{to_day_str}.txt', 'w')

            for i in range(len(field_last_steps)):
                print(
                    f'\n\nfield {field_id} step {self.iterator + i} results:')
                print(field_last_steps[i])
                print('\n')
                f.write(f'field {field_id} step {self.iterator + i} results:')
                f.write(field_last_steps[i])
                f.write('\n')
            f.close()
