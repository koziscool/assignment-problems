

import matplotlib.pyplot as plt
from monte_carlo_coin_flips import binomial_distribution, monte_carlo_distribution
plt.style.use('bmh')

num_plots, num_flips, num_trials = 5, 8, 100
true_probabilities = binomial_distribution(num_flips)
plots = []
for _ in range(num_plots):
    plots.append( monte_carlo_distribution(num_flips, num_trials) )

x_axis = [ i for i in range(num_flips + 1)]

plt.plot( x_axis,true_probabilities, linewidth=2.5)
for i in range(num_plots):
    plt.plot(x_axis, plots[i], linewidth=0.75)

plt.legend(['True','MC 1','MC 2', 'MC 3', 'MC 4', 'MC 5'])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('True Distribution vs Monte Carlo Simulations for 8 Coin Flips')
plt.savefig('mc_plot.png')
