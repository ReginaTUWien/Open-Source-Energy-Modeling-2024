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


npv = utils.calc_npv(
    investment_costs,
    int_rate,
    installed_capacity,
    lifetime,
    full_load_hours,
    annual_load,
    feedin_tarif,
    supply_tarif,
)
print("NPV at the end of life: " + str(round(npv[lifetime - 1], 4)) + " €")
