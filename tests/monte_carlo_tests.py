
import sys
sys.path.append('../')
from monte_carlo_coin_flips import *

assert probability_test(5, 8, .21875)
print( binomial_probability(5,8))
for _ in range(5):
    print( monte_carlo_probability(5,8))