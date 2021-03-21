
from functools import reduce
from random import random

def factorial(n):
    return reduce( lambda m,n: m*n, range(1, n+1), 1 )


def combinations(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)


def binomial_probability(num_heads, num_flips):
    possible_outcomes = 2 ** num_flips
    return combinations(num_flips, num_heads) / possible_outcomes    


def binomial_distribution(num_flips):
    ret_arr  = []
    for i in range(num_flips+1):
        ret_arr.append(binomial_probability(i, num_flips))
    return ret_arr


def probability_test(num_heads, num_flips, value):
    return binomial_probability(num_heads, num_flips) == value


def monte_carlo_probability(num_heads, num_flips):
    num_trials, trials_with_num_heads = 1000, 0
    for _ in range(num_trials):
        num_heads_in_trial = 0
        for i in range(num_flips):
            if random() > 0.5:
                num_heads_in_trial += 1
        if num_heads_in_trial == num_heads:
            trials_with_num_heads += 1
    return trials_with_num_heads / num_trials

def monte_carlo_distribution(num_flips, num_trials):
    trials_with_num_heads = 0
    ret_arr = [0] * (num_flips + 1)
    for _ in range(num_trials):
        num_heads_in_trial = 0
        for i in range(num_flips):
            if random() > 0.5:
                num_heads_in_trial += 1
        ret_arr[num_heads_in_trial] += 1
    ret_arr = list(map(lambda n: n/num_trials, ret_arr))
    return ret_arr

