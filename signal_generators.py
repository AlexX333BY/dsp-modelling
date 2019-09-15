import math


class HarmonicSignalGenerator:
    def __init__(self, amplitude, frequency, initial_phase, period):
        self.__amplitude = amplitude
        self.__frequency = frequency
        self.__initial_phase = initial_phase
        self.__period = period

    def __get_next_signal_part(self, n):
        return self.__amplitude * math.sin(2 * math.pi * self.__frequency * n / self.__period + self.__initial_phase)

    def get_signal(self):
        for n in range(self.__period):
            yield self.__get_next_signal_part(n)
