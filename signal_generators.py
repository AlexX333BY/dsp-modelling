import math
from collections import namedtuple
from enum import Enum

HarmonicParameters = namedtuple('HarmonicParameters', ['amplitude', 'frequency', 'initial_phase'])


class HarmonicSignalGenerator:
    def __init__(self, harmonic_params):
        self.__params = harmonic_params

    def get_signal_part(self, n, period):
        return self.__params.amplitude * math.sin(2 * math.pi * self.__params.frequency * n / period
                                                  + self.__params.initial_phase)

    def get_signal(self, period):
        for n in range(period):
            yield self.get_signal_part(n, period)


class PolyHarmonicSignalGenerator:
    def __init__(self, harmonic_params_collection):
        self.__harmonic_generators = []
        for harmonic_params in harmonic_params_collection:
            self.__harmonic_generators.append(HarmonicSignalGenerator(harmonic_params))

    def get_signal_part(self, n, period):
        return sum([generator.get_signal_part(n, period) for generator in self.__harmonic_generators])

    def get_signal(self, period):
        for n in range(period):
            yield self.get_signal_part(n, period)


class MutationType(Enum):
    INCREMENT = 1
    DECREMENT = -1


HarmonicMutations = namedtuple('HarmonicMutations',
                               ['amplitude_mutation', 'frequency_mutation', 'initial_phase_mutation'])


class LinearPolyHarmonicSignalGenerator:
    def __init__(self, harmonic_params_collection):
        self.__harmonic_params_collection = harmonic_params_collection

    def get_signal(self, period, period_iterations, mutation_per_period, mutation_type):
        mutation_per_signal_part = mutation_per_period / period
        mutation_multiplier = mutation_type.value
        mutations = []
        for harmonic_params in self.__harmonic_params_collection:
            mutations.append(
                HarmonicMutations(harmonic_params.amplitude * mutation_per_signal_part * mutation_multiplier,
                                  harmonic_params.frequency * mutation_per_signal_part * mutation_multiplier,
                                  harmonic_params.initial_phase * mutation_per_signal_part * mutation_multiplier))
        for n in range(period * period_iterations):
            new_harmonic_params_collection = []
            for index, harmonic_params in enumerate(self.__harmonic_params_collection):
                new_harmonic_params_collection.append(
                    HarmonicParameters(harmonic_params.amplitude + mutations[index].amplitude_mutation,
                                       harmonic_params.frequency + mutations[index].frequency_mutation,
                                       harmonic_params.initial_phase + mutations[index].initial_phase_mutation))
            self.__harmonic_params_collection = new_harmonic_params_collection
            yield PolyHarmonicSignalGenerator(self.__harmonic_params_collection).get_signal_part(n, period)
