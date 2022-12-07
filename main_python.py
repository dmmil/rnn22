from Core.Rnn1Core import Rnn1Core
from Core.Rnn2Core import Rnn2Core
from Core.Params import CommonParams, Rnn1Params, Rnn2Params
import matplotlib.pyplot as plt
import argparse
from typing import Dict


# main class, python api using example
class Main:

    def __init__(self, proc_type, settings_common_file_path,
                 settings_rnn1_file_path, settings_rnn2_file_path):
        super(Main, self).__init__()

        self.proc_type = proc_type

        # load common settings
        params = CommonParams(settings_common_file_path)
        self.params = params
        self.params.continuous_mode = False
        self.params.draw_layers = False

        # rnn1
        rnn1_params = Rnn1Params(settings_rnn1_file_path, params)
        self.rnn1 = Rnn1Core(params, rnn1_params)

        # rnn2
        rnn2_params = Rnn2Params(settings_rnn2_file_path, params)
        self.rnn2 = Rnn2Core(params, rnn2_params)

    # copying rnn1 state to rnn2
    def rnn1_to_rnn2(self, rnn1_to_rnn2_data: Dict):

        if self.proc_type == 'Predict':
            rnn1_to_rnn2_data['processing_type'] = 'Predict'
            rnn1_to_rnn2_data['predictStepsNum'] = \
                self.params.predictStepsNum
        elif self.proc_type == 'Novelty filter':
            rnn1_to_rnn2_data['processing_type'] = 'Novelty filter'
            rnn1_to_rnn2_data['novFiltStepsNum'] = \
                self.params.novFiltStepsNum
        else:
            print('selected not provide processing type')
            return

        return rnn1_to_rnn2_data


if __name__ == '__main__':

    # parse args from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', default='Novelty',
                        help='mode of system funtioning: Predict/Novelty')
    args = parser.parse_args()
    vv = vars(args)

    if vv['mode'] == 'Predict':
        app = Main('Predict',
                   'example_data_forecasting/settings_common.ini',
                   'example_data_forecasting/settings_rnn1.ini',
                   'example_data_forecasting/settings_rnn2.ini')

        # init rnn1 processing
        app.rnn1.start_process_signals()

        # process rnn1
        ok = True
        while ok:
            ok = app.rnn1.process_signals()  # working tact of rnn processing

            # for example, we want to predict for tacts 35, 40, 45
            if app.rnn1.cntr == 35 * 4 or app.rnn1.cntr == 40 * 4 \
                    or app.rnn1.cntr == 45 * 4:
                # copy rnn1 state to rnn2
                app.rnn2.paste_model(app.rnn1_to_rnn2(app.rnn1.copy_model()))

                # process rnn2
                ok2 = True
                while ok2:
                    # while data on rnn2 layers
                    ok2 = app.rnn2.process_signals()
                # analyze results of processing
                app.rnn2.finish_process_signals()

                # info about rnn2 finished, then can continue
                app.rnn1.rnn2finished()
        app.rnn1.finish_process_signals()  # analyze results of processing

    elif vv['mode'] == 'Novelty':
        app = Main('Novelty filter',
                   'example_data_noveltyFiltering/settings_common.ini',
                   'example_data_noveltyFiltering/settings_rnn1.ini',
                   'example_data_noveltyFiltering/settings_rnn2.ini')

        # init rnn1 processing
        app.rnn1.start_process_signals()

        # process rnn1
        ok = True
        while ok:
            ok = app.rnn1.process_signals()

            if len(app.rnn1.novelty_state.keys()):
                # copy rnn1 state to rnn2
                app.rnn2.paste_model(app.rnn1_to_rnn2(app.rnn1.novelty_state))

                # process rnn2
                ok2 = True
                while ok2:
                    ok2 = app.rnn2.process_signals()
                app.rnn2.finish_process_signals()

                # info about rnn2 finished, then can continue
                app.rnn1.rnn2finished()
        app.rnn1.finish_process_signals()

        plt.plot(app.rnn1.novelty_plot_data)
        plt.show()

    else:
        raise 'Unknown processing type. ' \
              'Please choose between Predict and Novelty'

    print('finished')
