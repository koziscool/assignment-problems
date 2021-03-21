import sys
sys.path.append('../')
from monte_carlo_coin_flips import *
from math import log
from functools import reduce
from random import random

def kl_divergence(p, q):
    ret_val = 0
    for i in range(len(p)):
        if p[i] > 0 and q[i] > 0:
            ret_val += p[i] * log(p[i]/q[i])
    return ret_val

p = [0.2, 0.5, 0, 0.3]
q = [0.1, 0.8, 0.1, 0]
kl = -0.096372
assert(round(kl_divergence(p, q), 6) == kl)

num_flips = 8
true_probabilities = binomial_distribution(num_flips)

print("Computing KL Divergence for Monte Carlo simulations")
print()

num_trials = 100
print(num_trials, " trials  --> KL Divergence = ", 
       kl_divergence(monte_carlo_distribution(num_flips, num_trials), true_probabilities))

num_trials = 1000
print(num_trials, " trials  --> KL Divergence = ", 
       kl_divergence(monte_carlo_distribution(num_flips, num_trials), true_probabilities))

num_trials = 10000
print(num_trials, " trials  --> KL Divergence = ", 
       kl_divergence(monte_carlo_distribution(num_flips, num_trials), true_probabilities))

# As the number of Monte Carlo trials increases, the KL divergence approaches zero,
# because the MC distribution asymptotically approaches the true analytic distribution
