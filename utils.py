"""
This module defines the functions required for calculating net present value.
The parameters are defined in main.py
"""


import numpy as np


def calc_crf(int_rate, lifetime):
    '''Calculation of capital ercovery factor'''
    crf = ((1 + int_rate)**lifetime * int_rate)/((1 + int_rate)**lifetime-1)
    return crf

def calc_self_consumption(installed_capacity, full_load_hours):
    '''Calculation of self-consumption per yeaar with the assumption that 
    50% of the energy generated is consumed'''
    self_consumption = installed_capacity * full_load_hours * 0.5
    return self_consumption

def calc_annual_costs(annual_load, self_consumption, supply_tarif):
    '''Calculation of annual electricity costs'''
    annual_costs = (annual_load - self_consumption) * supply_tarif
    return annual_costs

def calc_annual_revenues(self_consumption, feedin_tarif):
    '''Calculation of annual revenues'''
    annual_revenues = self_consumption * feedin_tarif
    return annual_revenues

def calc_npv(investment_costs, int_rate, installed_capacity, lifetime,
             full_load_hours, annual_load, feedin_tarif, supply_tarif):
    '''Calculation of net present value over the lifetime'''
    crf = calc_crf(int_rate, lifetime)
    self_consumption = calc_self_consumption(installed_capacity, full_load_hours)
    annual_costs = calc_annual_costs(annual_load, self_consumption, supply_tarif)
    annual_revenues = calc_annual_revenues(self_consumption, feedin_tarif)

    npv = np.zeros(lifetime)
    npv[0] = - (investment_costs*installed_capacity)
    for i in range(1, lifetime):
        npv[i] = npv[i-1] + 1/crf * (annual_revenues-annual_costs)
    return npv
