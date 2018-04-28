from app.function import search, search2, searchop, create_index, docFromFile, postinglist, postinglistMP, \
    postinglistThread
import timeit
import time
from matplotlib import pyplot as plt
import numpy as np
import sys

benchmark = []


def plot_results():
    bar_labels = ['serial', '2 processes', '4 processes', '8 processes', '2 threads']

    fig = plt.figure(figsize=(15, 8))

    # plot bars
    y_pos = np.arange(len(benchmark))
    plt.yticks(y_pos, bar_labels, fontsize=16)
    bars = plt.barh(y_pos, benchmark,
                    align='center', alpha=0.4, color='g')

    # annotation and labels

    for ba, be in zip(bars, benchmark):
        plt.text(ba.get_width() + 2, ba.get_y() + ba.get_height() / 2,
                 '{0:.2%}'.format(benchmark[0] / be),
                 ha='center', va='bottom', fontsize=12)

    plt.xlabel('time in seconds', fontsize=14)
    plt.ylabel('number of processes', fontsize=14)
    t = plt.title(
        'Serial vs. Multiprocessing index construction', fontsize=18)
    plt.ylim([-1, len(benchmark) + 0.5])
    plt.xlim([0, max(benchmark) * 1.1])
    plt.vlines(benchmark[0], -1, len(benchmark) + 0.5, linestyles='dashed')
    plt.grid()

    plt.savefig('app/static/benchmark.png')
    # plt.show()


def indexScript(input1, input2):
    termList = postinglistMP(4)
    index = create_index(termList)

    s1 = input1
    s2 = input2
    posting_list1 = search(s1, index)
    posting_list2 = search2(s2, index)
    posting_listres = searchop(posting_list1, posting_list2)

    benchmark.append(timeit.Timer('postinglist()',
                                  'from app.function import postinglist').timeit(number=1))
    benchmark.append(timeit.Timer('postinglistMP(2)',
                                  'from app.function import postinglistMP').timeit(number=1))
    benchmark.append(timeit.Timer('postinglistMP(4)',
                                  'from app.function import postinglistMP').timeit(number=1))
    benchmark.append(timeit.Timer('postinglistMP(8)',
                                  'from app.function import postinglistMP').timeit(number=1))
    benchmark.append(timeit.Timer('postinglistThread(2)',
                                  'from app.function import postinglistThread').timeit(number=1))

    retObject = {"post1": posting_list1,
                 "post2": posting_list2,
                 "postr": posting_listres,
                 "serial": benchmark[0],
                 "2p": benchmark[1],
                 "4p": benchmark[2],
                 "8p": benchmark[3],
                 "2t": benchmark[4]}

    plot_results()
    return retObject
