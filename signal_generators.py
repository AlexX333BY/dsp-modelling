import math
from collections import namedtuple

HarmonicParameters = namedtuple('HarmonicParameters', ['amplitude', 'frequency', 'initial_phase'])


class HarmonicSignalGenerator:
    def __init__(self, harmonic_params, period):
        self.__params = harmonic_params
        self.__period = period

    def __get_next_signal_part(self, n):
        return self.__params.amplitude * math.sin(2 * math.pi * self.__params.frequency * n / self.__period
                                                  + self.__params.initial_phase)

    def get_signal(self):
        for n in range(self.__period):
            yield self.__get_next_signal_part(n)
