# Open-Source-Energy-Modeling-2024

[![license](https://img.shields.io/badge/license-Apache%202.0-black)](https://github.com/ReginaTUWien/Open-Source-Energy-Modeling-2024/blob/main/LICENSE)

## This method is used to calculate the net present value of a residential PV-system.

Author: Regina Kéri, 11813852

For these calculations are some parameters and assumptions are required 
(these can be edited in main.py):

- Investment costs: 1200 €/kWp
- Interest rate: 5 %
- Installed capacity: 5 kWp
- Lifetime: 20 years
- Annual load of the household: 3500 kWh
- Feedin tarif: 8 ct/kWh
- Electricity costs: 15 ct/kWh

It is also assumed that half of the energy generated is fed into the grid.

Functions:

- calc_crf: Calculation of capital ercovery factor
- calc_self_consumption: Calculation of self-consumption per yeaar with the assumption that 50% of the energy generated is consumed
- calc_annual_costs: Calculation of annual electricity costs
- calc_annual_revenues: Calculation of annual revenues
- calc_npv: Calculation of net present value over the lifetime
