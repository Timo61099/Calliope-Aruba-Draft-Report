#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:15:36 2024

@author: timoscheepmaker
"""

import calliope
import os

calliope.set_log_verbosity('INFO', include_solver_output=False)

model = calliope.Model("model.yaml", scenario='Scenario_20%_FF_2050')
#model = calliope.Model("model.yaml")
model.run()

model.to_netcdf('Aruba_test.nc')