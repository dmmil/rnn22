import numpy as np
import os
from typing import List

def convert_input_to_ssps(inpt: str):
    ssp = ''
    for i in range(len(inpt)):
        if inpt[i]:
            ssp += '1'
        else:
            ssp += '0'
    return ssp


def convert_words_to_ssps(dictionary: List, words: str):

    lst = words.split('\n')
    words_splitted = []
    for entry in lst:
        if entry.strip() != '':
            words_splitted.append(entry)

    ssp = ''
    for i in range(len(dictionary)):
        if dictionary[i] in words_splitted:
            ssp += '1'
        else:
            ssp += '0'
    return ssp


def words_pe0_pe1(real_ssps: str, pred_ssps: str, field_id: int, iterator: int, to_day_str: str):
    pe0 = []
    pe1 = []
    if not len(real_ssps) == len(pred_ssps):
        print('not len(real_ssps) == len(pred_ssps)')
        return
    for i in range(len(real_ssps)):
        e0 = 0
        e1 = 0
        if not len(real_ssps[i]) == len(pred_ssps[i]):
            print('error: not len(real_ssps[i]) == len(pred_ssps[i])')
            print(f'len(real_ssps[i]): {len(real_ssps[i])}, '
                  f'len(pred_ssps[i]): {len(pred_ssps[i])}')
            return
        for j in range(len(real_ssps[i])):
            if real_ssps[i][j] == '1' and pred_ssps[i][j] == '0':
                e0 += 1
            elif real_ssps[i][j] == '0' and pred_ssps[i][j] == '1':
                e1 += 1
        pe0.append(float(e0) / len(real_ssps[i]) * 100)
        pe1.append(float(e1) / len(real_ssps[i]) * 100)

    result_str = f'step {iterator} field {field_id} result: ' \
                 f'pe0 {"%.2f" % (np.sum(pe0)/len(pe0))}%, ' \
                 f'pe1 {"%.2f" % (np.sum(pe1)/len(pe1))}%'
    print(result_str)

    if not os.path.exists('results_forecasting'):
        os.mkdir('results_forecasting')
    f = open(f'results_forecasting/results_{to_day_str}.txt', 'a')
    f.write(result_str)
    f.write('\n')
    f.close()
