import math
from collections import namedtuple

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

    def get_signal(self, period):
        for n in range(period):
            yield sum([generator.get_signal_part(n, period) for generator in self.__harmonic_generators])
