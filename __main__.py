import argparse
from chart_drawer import *
from signal_generators import *


def task_1():
    def harmonic():
        variable_initial_phase_parameters = []
        for initial_phase in [0.0, math.pi / 6, math.pi / 4, math.pi / 2, math.pi]:
            variable_initial_phase_parameters.append(HarmonicParameters(10, 2, initial_phase))

        variable_frequency_parameters = []
        for frequency in [5, 4, 2, 6, 3]:
            variable_frequency_parameters.append(HarmonicParameters(3, frequency, math.pi / 2))

        variable_amplitude_parameters = []
        for amplitude in [2, 3, 6, 5, 1]:
            variable_amplitude_parameters.append(HarmonicParameters(amplitude, 1, math.pi / 2))

        variable_parameters_choice = {'initial-phase': variable_initial_phase_parameters,
                                      'frequency': variable_frequency_parameters,
                                      'amplitude': variable_amplitude_parameters}
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--variable-parameter', action='store', required=True,
                            help='what parameter should vary', choices=variable_parameters_choice.keys(),
                            dest='parameter', type=str)
        parser.add_argument('-N', '--period', action='store', required=False, help='signal period', dest='period',
                            type=int, default=512)
        args = parser.parse_known_args()[0]

        chart_data = []
        for harmonic_params in variable_parameters_choice[args.parameter]:
            chart_data.append(LabeledChartData(list(HarmonicSignalGenerator(harmonic_params).get_signal(args.period)),
                                               ', '.join(['A: ' + str(harmonic_params.amplitude),
                                                          'f: ' + str(harmonic_params.frequency),
                                                          'phi: ' + str(harmonic_params.initial_phase)])))
        draw_charts(chart_data)

    def poly_harmonic():
        parser = argparse.ArgumentParser()
        parser.add_argument('-N', '--period', action='store', required=False, help='signal period', dest='period',
                            type=int, default=512)
        period = parser.parse_known_args()[0].period
        harmonic_parameters = [HarmonicParameters(1, 1, 0), HarmonicParameters(1, 2, math.pi / 4),
                               HarmonicParameters(1, 3, math.pi / 6), HarmonicParameters(1, 4, 2 * math.pi),
                               HarmonicParameters(1, 5, math.pi)]
        draw_chart(LabeledChartData(list(PolyHarmonicSignalGenerator(harmonic_parameters).get_signal(period)), None))

    def linear():
        parser = argparse.ArgumentParser()
        parser.add_argument('-N', '--period', action='store', required=False, help='signal period', dest='period',
                            type=int, default=512)
        parser.add_argument('-i', '--period-iterations', action='store', required=False, help='period iterations',
                            dest='period_iterations', type=int, default=1)
        parser.add_argument('-m', '--mutation', action='store', required=False, help='mutation per period',
                            dest='mutation_per_period', type=float, default=0.2)
        parser.add_argument('-ml', '--mutation-law', action='store', required=True, help='mutation law', type=str,
                            dest='mutation_law', choices=[MutationType.DECREMENT.name, MutationType.INCREMENT.name])
        args = parser.parse_known_args()[0]
        harmonic_parameters = [HarmonicParameters(1, 1, 0), HarmonicParameters(1, 2, math.pi / 4),
                               HarmonicParameters(1, 3, math.pi / 6), HarmonicParameters(1, 4, 2 * math.pi),
                               HarmonicParameters(1, 5, math.pi)]
        draw_chart(LabeledChartData(list(LinearPolyHarmonicSignalGenerator(harmonic_parameters)
                                         .get_signal(args.period, args.period_iterations, args.mutation_per_period,
                                                     MutationType[args.mutation_law])), None))

    sub_tasks_callbacks = {'harmonic': harmonic, 'poly-harmonic': poly_harmonic, 'linear': linear}

    parser = argparse.ArgumentParser()
    parser.add_argument('-st', '--sub-task', action='store', required=True, help='first tasks sub task',
                        choices=sub_tasks_callbacks.keys(), dest='sub_task', type=str)
    sub_tasks_callbacks[parser.parse_known_args()[0].sub_task]()


def task_2(): raise NotImplementedError


def main():
    tasks_callbacks = {1: task_1, 2: task_2}

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--task', action='store', required=True, help='task number',
                        choices=tasks_callbacks.keys(), dest='task', type=int)
    tasks_callbacks[parser.parse_known_args()[0].task]()


if __name__ == "__main__":
    main()
