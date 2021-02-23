
import matplotlib.pyplot as plt

collatz = lambda n: n // 2 if n % 2 == 0 else 3 * n + 1

def collatz_iterations(n):
    if n == 1:
        return 0
    num_iterations = 0
    while n != 1:
        n = collatz(n)
        num_iterations += 1
    return num_iterations

begin, end = 1, 1000
indexes, collatzes = [], []
max_index, max_iterations = 0,0
for i in range(begin, end+1):
    indexes.append(i)
    collatzes.append(collatz_iterations(i))
    if collatz_iterations(i) > max_iterations:
        max_iterations = collatz_iterations(i)
        max_index = i

print( max_index, max_iterations)

plt.style.use('bmh')
x_coords = indexes
y_coords = collatzes 
plt.plot(x_coords, y_coords)
plt.xlabel('Starting Collatz input')
plt.ylabel('Number of iterations till 1')
plt.title('Collatz')
plt.savefig('plot.png')
