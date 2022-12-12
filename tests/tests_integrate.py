import os
import sys
sys.path.append(os.path.join(sys.path[0], '..'))
from main_python import Main


def test_answer():

    app = Main('Predict',
               'example_data_forecasting/settings_common.ini',
               'example_data_forecasting/settings_rnn1.ini',
               'example_data_forecasting/settings_rnn2.ini')

    # init rnn1 processing
    app.rnn1.start_process_signals()

    # process rnn1
    ok = True
    while ok:
        ok = app.rnn1.process_signals()

        if app.rnn1.cntr == 35 * 4 or app.rnn1.cntr == 40 * 4 \
                or app.rnn1.cntr == 45 * 4:
            # copy model
            app.rnn2.paste_model(app.rnn1_to_rnn2(app.rnn1.copy_model()))

            # process rnn2
            ok2 = True
            while ok2:
                ok2 = app.rnn2.process_signals()
            app.rnn2.finish_process_signals()

            # info about rnn2 finished, then can continue
            app.rnn1.rnn2finished()
    app.rnn1.finish_process_signals()

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
            # copy model
            app.rnn2.paste_model(app.rnn1_to_rnn2(app.rnn1.novelty_state))

            # process rnn2
            ok2 = True
            while ok2:
                ok2 = app.rnn2.process_signals()
            app.rnn2.finish_process_signals()

            # info about rnn2 finished, then can continue
            app.rnn1.rnn2finished()
    app.rnn1.finish_process_signals()

    assert True
