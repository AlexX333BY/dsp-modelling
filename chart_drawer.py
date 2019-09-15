from matplotlib import pyplot
from collections import namedtuple

LabeledChartData = namedtuple('LabeledChartData', ['data', 'label'])


def draw_charts(chart_data_collection):
    pyplot.rcParams['toolbar'] = 'None'

    for chart_data in chart_data_collection:
        pyplot.plot(chart_data.data, label=chart_data.label)

    pyplot.legend()
    pyplot.grid(True)
    pyplot.show()


def draw_chart(chart_data):
    draw_charts([chart_data])
