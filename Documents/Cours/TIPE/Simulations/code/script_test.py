#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to test "tests_natural_selection" module

@author: Tregoat Johanne
"""

import tests_natural_selection as ns

nb_simulations = 100000

# Simulate
never_betray = ns.never_betray(nb_simulations)
always_betray = ns.always_betray(nb_simulations)
betray_when_betrayed_1 = ns.betray_if_betrayed_deterministic(0, always_betray)
betray_when_betrayed_2 = ns.betray_if_betrayed_deterministic(0, never_betray)

# Calculate costs
# never_betray vs always betray
never_score, always_score = ns.cost(never_betray, always_betray)

# Always betrayed vs betray when betrayed
always_score_2, betray_when_score = ns.cost(always_betray, betray_when_betrayed_1)

# Never betray vs betray when betrayed
never_score_2, betray_when_score_2 = ns.cost(never_betray, betray_when_betrayed_2)
