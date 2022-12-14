import os
import sys
sys.path.append(os.path.join(sys.path[0], '..'))
from Core.Rnn1Core import Rnn1Core
from Core.Rnn2Core import Rnn2Core
from Core.Params import CommonParams, Rnn1Params, Rnn2Params

def test_answer():

    # module test 1: params classes

    params1_predict = CommonParams('examples/example_data_forecasting/'
                                   'settings_common.ini')
    params2_predict = CommonParams('examples/example_data_forecasting/'
                                   'settings_common.ini')
    params1_predict.rewrite()
    assert params1_predict.__dict__ == params2_predict.__dict__, \
        'Uncorrect predict CommonParams rewrite'

    params1_novelty = CommonParams('examples/example_data_noveltyFiltering/'
                                   'settings_common.ini')
    params2_novelty = CommonParams('examples/example_data_noveltyFiltering/'
                                   'settings_common.ini')
    params1_novelty.rewrite()
    assert params1_novelty.__dict__ == params2_novelty.__dict__, \
        'Uncorrect novelty CommonParams rewrite'

    rnn1_params1_predict = Rnn1Params('examples/example_data_forecasting/'
                              'settings_rnn1.ini', params1_predict)
    rnn1_params2_predict = Rnn1Params('examples/example_data_forecasting/'
                              'settings_rnn1.ini', params1_predict)
    rnn1_params1_predict.rewrite()
    assert rnn1_params1_predict.__dict__ == rnn1_params2_predict.__dict__, \
        'Uncorrect predict Rnn1Params rewrite'

    rnn1_params1_novelty = Rnn1Params(
        'examples/example_data_noveltyFiltering/settings_rnn1.ini',
        params1_novelty)
    rnn1_params2_novelty = Rnn1Params(
        'examples/example_data_noveltyFiltering/settings_rnn1.ini',
        params1_novelty)
    rnn1_params1_novelty.rewrite()
    assert rnn1_params1_novelty.__dict__ == rnn1_params2_novelty.__dict__, \
        'Uncorrect novelty Rnn1Params rewrite'

    rnn2_params1_predict = Rnn2Params('examples/example_data_forecasting/'
                              'settings_rnn2.ini', params1_predict)
    rnn2_params2_predict = Rnn2Params('examples/example_data_forecasting/'
                              'settings_rnn2.ini', params1_predict)
    rnn2_params1_predict.rewrite()
    assert rnn2_params1_predict.__dict__ == rnn2_params2_predict.__dict__, \
        'Uncorrect predict Rnn2Params rewrite'

    rnn2_params1_novelty = Rnn2Params(
        'examples/example_data_noveltyFiltering/settings_rnn2.ini',
        params1_novelty)
    rnn2_params2_novelty = Rnn2Params(
        'examples/example_data_noveltyFiltering/settings_rnn2.ini',
        params1_novelty)
    rnn2_params1_novelty.rewrite()
    assert rnn2_params1_novelty.__dict__ == rnn2_params2_novelty.__dict__, \
        'Uncorrect novelty Rnn2Params rewrite'

    # module test 2: rnn1_predict

    params1_predict.continuous_mode = False
    params1_predict.draw_layers = False

    rnn1_predict = Rnn1Core(params1_predict, rnn1_params1_predict)
    rnn1_predict.start_process_signals()
    ok = True
    i = 0
    while ok:
        i += 1
        if i == 30:
            m = rnn1_predict.copy_model()
        rnn1_output_data_predict = rnn1_predict.io_device.output_samples_dict
        ok = rnn1_predict.process_signals()
    rnn1_predict.finish_process_signals()
    with open('tests/files_predict/rnn1_output_data_correct.txt', 'r') as f:
        correct_rnn1_output_data_predict = f.read()

    assert " ".join(rnn1_output_data_predict[1]) == \
           correct_rnn1_output_data_predict, \
        'uncorrect rnn1 predict mode output'

    rnn1_predict.clear_layers()
    rnn1_predict.clear_rnn()

    # module test 3: rnn2_predict

    rnn2_predict = Rnn2Core(params1_predict, rnn2_params1_predict)
    m['processing_type'] = 'Predict'
    m['predictStepsNum'] = params1_predict.predictStepsNum
    rnn2_predict.paste_model(m)
    ok = True
    while ok:
        rnn2_output_data_predict = rnn2_predict.io_device.output_samples_dict
        ok = rnn2_predict.process_signals()
    rnn2_predict.finish_process_signals()
    rnn2_predict.clear_layers()
    rnn2_predict.clear_rnn()
    with open('tests/files_predict/rnn2_output_data_correct.txt', 'r') as f:
        correct_rnn2_output_data_predict = f.read()
    assert " ".join(rnn2_output_data_predict[1]) == \
           correct_rnn2_output_data_predict, \
        'uncorrect rnn2 predict mode output'

    # module test 4: rnn1_novelty

    params1_novelty.continuous_mode = False
    params1_novelty.draw_layers = False

    rnn1_novelty = Rnn1Core(params1_novelty, rnn1_params1_novelty)
    rnn1_novelty.start_process_signals()
    ok = True
    i = 0
    while ok:
        i += 1
        if i == 120:
            m = rnn1_novelty.copy_model()
        rnn1_output_data_novelty = rnn1_novelty.io_device.output_samples_dict
        ok = rnn1_novelty.process_signals()
    rnn1_novelty.finish_process_signals()
    with open('tests/files_novelty/rnn1_output_data_correct.txt', 'r') as f:
        correct_rnn1_output_data_novelty = f.read()

    assert " ".join(rnn1_output_data_novelty[1]) == \
           correct_rnn1_output_data_novelty, \
        'uncorrect rnn1 novelty mode output'

    rnn1_novelty.clear_layers()
    rnn1_novelty.clear_rnn()

    # module test 5: rnn2_novelty

    rnn2_novelty = Rnn2Core(params1_novelty, rnn2_params1_novelty)
    m['processing_type'] = 'Novelty filter'
    m['novFiltStepsNum'] = params1_novelty.novFiltStepsNum
    rnn2_novelty.paste_model(m)
    ok = True
    while ok:
        rnn2_output_data_novelty = rnn2_novelty.io_device.output_samples_dict
        ok = rnn2_novelty.process_signals()
    rnn2_novelty.finish_process_signals()
    rnn2_novelty.clear_layers()
    rnn2_novelty.clear_rnn()
    with open('tests/files_novelty/rnn2_output_data_correct.txt', 'r') as f:
        correct_rnn2_output_data_novelty = f.read()
    assert " ".join(rnn2_output_data_novelty[1]) == \
           correct_rnn2_output_data_novelty, \
        'uncorrect rnn2 novelty mode output'

    assert True

test_answer()
