import os
import sys
sys.path.append(os.path.join(sys.path[0], '..'))
from Core.Rnn1Core import Rnn1Core
from Core.Rnn2Core import Rnn2Core
from Core.Params import CommonParams, Rnn1Params, Rnn2Params


def test_answer():

    sys.path.append(os.path.join(sys.path[0], '..'))

    params = CommonParams('example_data_forecasting/settings_common.ini')
    params.rewrite()

    rnn1_params = Rnn1Params('example_data_forecasting/settings_rnn1.ini', params)
    rnn1_params.rewrite()

    rnn2_params = Rnn2Params('example_data_forecasting/settings_rnn2.ini', params)
    rnn2_params.rewrite()

    rnn1 = Rnn1Core(params, rnn1_params)
    rnn1.start_process_signals()
    rnn1.process_signals()
    m = rnn1.copy_model()
    rnn1.finish_process_signals()
    rnn1.clear_layers()
    rnn1.clear_rnn()

    rnn2 = Rnn2Core(params, rnn2_params)
    if params.processing_type == 'Predict':
        m['processing_type'] = 'Predict'
        m['predictStepsNum'] = params.predictStepsNum
    elif params.processing_type == 'Novelty filter':
        m['processing_type'] = 'Novelty filter'
        m['novFiltStepsNum'] = params.novFiltStepsNum
    rnn2.paste_model(m)
    rnn2.process_signals()
    rnn2.finish_process_signals()
    rnn2.clear_layers()
    rnn2.clear_rnn()

    assert True

test_answer()