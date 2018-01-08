#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Improved speed implementation of natural selection module.

@author: Tregoat Johanne
"""
import numpy as np


def cost(choices_1, choices_2, costs=[1, 20, 10]):
    """
Calculates the overall time spent in prison over a set of simulations.
Choices is a vector of booleans, 0 means not betray, 1 means betray.

    :param choices_1: individual 1's choices (betray or not). Must be numpy array.
    :param choices_2:  individual 2's choices (betray or not). Must be numpy array.
    :param costs: cost[0]= none betray, cost[1] = one betrays the other, cost[2] = betray each other.
        costs[0] must be inferior to costs[1].
    :return: cost_for_individual_1, cost_for_individual_2 (both integers)

    """
    # Compute differences in chocies
    diff = choices_1 - choices_2
    # When they made the same choices
    same_choices = choices_1[np.where(diff == 0)[0]]  # Every choice that was the same for the 2
    cost_of_same_choices = np.sum((costs[2]-costs[0]) * same_choices + costs[0])  # e.g. [10, 1, 1, 10, 1], 10 when betray, else 1.

    # Compute total cost for each individual and return
    # When -1 then 1 was betrayed, ind. 1 gets costs[1] years in jail and ind. 2 gets 0. When 1, other way around.
    return int(cost_of_same_choices + len(np.where(diff == -1)[0]) * costs[1]), int(cost_of_same_choices +
                                                    len(np.where(diff == 1)[0]) * costs[1])


def never_betray(nb_of_sim):
    """
    Simulates someone that never betrays.

    :param nb_of_sim: number of simulations (i.e. length of vector)
    :return: vector of 0
    """
    return np.zeros(nb_of_sim)


def always_betray(nb_of_sim):
    """
    Simulates someone that always betrays.

    :param nb_of_sim: number of simulations (i.e. length of vector)
    :return: vector of 1
    """
    return np.ones(nb_of_sim)



def random_guess(nb_of_sim, p):
    """
    Simulates someone that always chooses randomly.

    :param nb_of_sim: number of simulations (i.e. length of vector)
    :param p: probability of betrayal.
    :return: vector of random 1 and 0.
    """
    if p > 1 or p < 0:
        raise Exception("p must be a probability, hence between 0 and 1.")
    return np.array(np.random.rand(nb_of_sim)> p, dtype=int)


def betray_if_betrayed_deterministic(initial_value, choices_2):
    """
    Betrays if was betrayed in the previous round. Else will not betray. Will do
        as many simulations as there are elements in chocies_2 (which length must be
        at least 2)

    :param initial_value: first action it will take ( betray = 1, else 0)
    :param choices_2: choice(s) made by the other individual
    :return: choices of the individual with this strategy. Type is numpy array.
    """
    # Check if arguments are of correct format
    if str(type(choices_2)) != "<class 'numpy.ndarray'>":
        raise Exception("choices_2 must be a numpy array of length at least 2.")
    if len(choices_2) < 2:
        raise Exception("choices_2 must be a numpy array of length at least 2.")

    # Initialize
    nb_sim = len(choices_2)
    decisions = np.zeros(nb_sim, dtype=int)

    # Betray
    decisions[np.where(choices_2[0:nb_sim-1] == 1)[0]+1] = 1
    return decisions
