"""
Calculation of net present value of a residential PV-system
"""

import utils

investment_costs = 1200  # in €/kWp
int_rate = 0.05
installed_capacity = 5  # in kWp
lifetime = 20  # in years
full_load_hours = 1000  # in h
annual_load = 3500  # in kWh
feedin_tarif = 0.08  # in €/kWh
supply_tarif = 0.15  # in €/kWh

crf = utils.calc_crf(int_rate, lifetime)
self_consumption = utils.calc_self_consumption(installed_capacity, full_load_hours)
annual_costs = utils.calc_annual_costs(annual_load, self_consumption, supply_tarif)
annual_revenues = utils.calc_annual_revenues(self_consumption, feedin_tarif)

npv = utils.calc_npv(
    investment_costs, installed_capacity, crf, annual_costs, annual_revenues
)

print("NPV at the end of life: " + str(round(npv[lifetime - 1], 4)) + " €")
