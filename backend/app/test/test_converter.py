from backend.app.converter import Converter


def test_c_f():
    celcius_fahrenheit_converter = Converter("C", "F")
    assert celcius_fahrenheit_converter.convert(0) == 32
    assert celcius_fahrenheit_converter.convert(10) == 50.0
    assert celcius_fahrenheit_converter.convert(-25) == -13.0


def test_c_k():
    celcius_kelvin_converter = Converter("C", "K")
    assert celcius_kelvin_converter.convert(0) == 273
    assert celcius_kelvin_converter.convert(10) == 283
    assert celcius_kelvin_converter.convert(-25) == 248


def test_f_k():
    fahrenheit_kelvin_converter = Converter("F", "K")
    assert fahrenheit_kelvin_converter.convert(0) == 255.22
    assert fahrenheit_kelvin_converter.convert(10) == 260.78
    assert fahrenheit_kelvin_converter.convert(-25) == 241.33


def test_f_c():
    fahrenheit_celcius_converter = Converter("F", "C")
    assert fahrenheit_celcius_converter.convert(32) == 0
    assert fahrenheit_celcius_converter.convert(50) == 10
    assert fahrenheit_celcius_converter.convert(-13.0) == -25


def test_k_c():
    kelvin_celcius_converter = Converter("K", "C")
    assert kelvin_celcius_converter.convert(0) == -273
    assert kelvin_celcius_converter.convert(10) == -263
    assert kelvin_celcius_converter.convert(-25) == -298


def test_k_f():
    kelvin_fahrenheit_converter = Converter("K", "F")
    assert kelvin_fahrenheit_converter.convert(0) == -459.4
    assert kelvin_fahrenheit_converter.convert(10) == -441.4
    assert kelvin_fahrenheit_converter.convert(-25) == -504.4
