"""
In this module the functions of utils.py are tested
"""


import utils
import math


def test_calc_crf():
    """Test the function calc_crf"""
    assert math.isclose(utils.calc_crf(10, 10), 10, abs_tol=0.001)


def test_calc_self_consumption():
    """Test the function calc_self_consumption"""
    assert utils.calc_self_consumption(2, 800) == 800


def test_calc_annual_costs():
    """Test the function calc_annual_costs"""
    assert utils.calc_annual_costs(2000, 800, 0.1) == 120


def test_calc_annual_revenues():
    """Test the function calc_annual_revenues"""
    assert utils.calc_annual_revenues(800, 0.1) == 80
