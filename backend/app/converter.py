"""
Rules for conversion
•	Celsius to Fahrenheit F = 9/5 ( C) + 32
•	Kelvin to Fahrenheit F = 9/5 (K - 273) + 32
•	Fahrenheit to Celsius C = 5/9 ( F - 32)
•	Celsius to Kelvin K = C + 273
•	Kelvin to Celsius C = K - 273
•	Fahrenheit to Kelvin K = 5/9 (F - 32) + 273
"""
offset_factor_map = {
    "C_F": ((9/5), 0, 32),
    "K_F": ((9/5), -273, 32),
    "F_C": ((5/9), -32, 0),
    "C_K": (1, 0, 273),
    "K_C": (1, 0, -273),
    "F_K": ((5/9), -32, 273)
}


def generate_offset_factor(unit_from: str, unit_to: str) -> (float, int, int):
    """
    Returns the factor, offset for the value and offset for the conversion
    :param unit_from: a string (either "C", "F" or "K")
    :param unit_to: a string (either "C", "F" or "K")
    :return: a tuple containing a factor (float), value offset (int) and offset (int)
    """
    return offset_factor_map[f"{unit_from}_{unit_to}"]


class Converter:
    def __init__(self, unit_from: str, unit_to: str):
        self.unit_from = unit_from
        self.unit_to = unit_to
        self.factor, self.offset_value, self.offset = generate_offset_factor(unit_from, unit_to)

    def description(self) -> str:
        """
        Describes the converter
        :return: a string
        """
        return 'Convert ' + self.unit_from + ' to ' + self.unit_to

    def convert(self, value: float) -> float:
        """
        Performs the conversion of the given value using the rules set for the 'unit_from' and 'unit_to' values
        :param value: the value to be converted (float)
        :return: conversion (float)
        """
        return round((value + self.offset_value) * self.factor + self.offset, 2)
