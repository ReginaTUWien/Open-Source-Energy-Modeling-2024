"""
In this module the functions of utils.py are tested
"""


import utils


def test_calc_crf():
    '''Test the function calc_crf'''
    assert round(utils.calc_crf(0.02, 25), 3) == 0.071

def test_calc_self_consumption():
    '''Test the function calc_self_consumption'''
    assert utils.calc_self_consumption(2, 800) == 800

def test_calc_annual_costs():
    '''Test the function calc_annual_costs'''
    assert utils.calc_annual_costs(2000, 800, 0.1) == 120

def test_calc_annual_revenues():
    '''Test the function calc_annual_revenues'''
    assert utils.calc_annual_revenues(800, 0.1) == 80

# def test_calc_npv():
#     '''Test the function calc_npv'''
#     assert utils.calc_npv(1000, 0.02, 2, 25, 800, 2000, 0.1, 0,1)
#     utils.calc_npv(investment_costs, int_rate, installed_capacity, lifetime, full_load_hours, annual_load, feedin_tarif, supply_tarif)
