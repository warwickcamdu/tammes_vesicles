#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 30 Jul 2018, 10:35

@author: erick
"""


def plot_results(filename):
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.ticker import MultipleLocator

    majorLocator = MultipleLocator(5)

    results = pd.read_csv(filename, index_col=0, header=None).T
    print(results)
    averages = results.mean()
    fit = np.polyfit(averages.index, averages.values, 2)
    labels = averages.index.values[0::5]

    labels = np.insert(labels, 0, 0)

    curve = np.poly1d(fit)

    axes = plt.subplot(111)
    x_fit = np.linspace(15, 51, 100)
    y_fit = curve(x_fit)
    rsquared = np.corrcoef(averages.index, averages.values)[0, 1]**2
    plt.plot(x_fit, y_fit)
    results.plot.box(ax=axes,
                     positions=averages.index.values)
    plt.text(25, 2000, 'y = ' + '{:.2f}'.format(fit[0]) +
             'x² + ' + '{:.2f}'.format(fit[1]) +
             'x + ' + '{:.2f}'.format(fit[2]),
             horizontalalignment='center',
             verticalalignment='center')
    plt.text(25, 1800, 'R² = ' +
             '{:.4f}'.format(rsquared),
             horizontalalignment='center',
             verticalalignment='center')

    axes.xaxis.set_major_locator(majorLocator)
    axes.set_xticklabels(labels)
    axes.set_xlabel(u"Vesicle radius (nm)")
    axes.set_ylabel(u"Number of proteins")
    plt.savefig("results_gpcr.png")
    plt.show()


if __name__ == "__main__":
    filename = 'tammes/results_GPCR.csv'
    plot_results(filename)
