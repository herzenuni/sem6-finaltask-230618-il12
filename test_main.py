from main import transform
import pytest

class TestTransform:

    def test_null(self):
        assert(transform(0) == 'Ноль')

    def test_one(self):
        assert(transform(1) == 'Один')

    def test_two(self):
        assert(transform(2) == 'Два')

    def test_three(self):
        assert(transform(3) == 'Три')

    def test_four(self):
        assert(transform(4) == 'Четыре')

    def test_five(self):
        assert(transform(5) == 'Пять')

    def test_six(self):
        assert(transform(6) == 'Шесть')

    def test_seven(self):
        assert(transform(7) == 'Семь')

    def test_eight(self):
        assert(transform(8) == 'Восемь')

    def test_nine(self):
        assert(transform(9) == 'Девять')

    def test_oct(self):
        assert(transform('0o25') == '25')

    def test_bin(self):
        assert(transform('0b00100101') == '00100101')

    def test_hex(self):
        assert(transform('0x15') == '15')


