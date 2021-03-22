
import matplotlib.pyplot as plt
from monte_carlo_coin_flips import binomial_distribution, monte_carlo_distribution
plt.style.use('bmh')

coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH',
          'TTH', 'TTH', 'TTH', 'THT', 'TTH',
          'HTH', 'HTH', 'TTT', 'HTH', 'HTH',
          'TTH', 'HTH', 'TTT', 'TTT', 'TTT',
          'HTT', 'THT', 'HHT', 'HTH', 'TTH']
coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH',
          'THH', 'HHH', 'HHH', 'HTT', 'TTH',
          'TTH', 'HHT', 'TTH', 'HTH', 'HHT',
          'THT', 'THH', 'THT', 'TTH', 'TTT',
          'HHT', 'THH', 'THT', 'THT', 'TTT']
coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH',
          'HHT', 'HHT', 'HHH', 'TTT', 'THH',
          'HHH', 'HHH', 'TTH', 'THH', 'THH',
          'TTH', 'HTT', 'TTH', 'HTT', 'HHT',
          'TTH', 'HTH', 'THT', 'THT', 'HTH']

num_flips = 3 

def get_plot(coin):
    ret_plot = [0] * (len(coin[0]) + 1)
    for flips in coin:
        num_heads = 0
        for c in flips:
            if c == 'H':
                num_heads += 1
        ret_plot[num_heads] += 1
    return ret_plot

plot1 = get_plot(coin_1)
plot2 = get_plot(coin_2)
plot3 = get_plot(coin_3)

x_axis = [ i for i in range(num_flips + 1)]

plt.plot(x_axis, plot1, linewidth=1.5)
plt.plot(x_axis, plot2, linewidth=1.5)
plt.plot(x_axis, plot3, linewidth=1.5)

plt.legend(['Coin 1','Coin 2', 'Coin 3'])
plt.xlabel('Number of Heads')
plt.ylabel('Frequency')
plt.title('Frequency of Heads in trial of 3 Separate Coins')
plt.savefig('coin_plot.png')

#Based on the trial data, the results of coin_1 appeared biased toward tails,
# the results of coin_3 were biased toward heads, and the results of coin_2 were unbiased

# But, given the relatively small sample size and the small size of deviations, 
# I would recommend against concluding any bias of any of the coins.

