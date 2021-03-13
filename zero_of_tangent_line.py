
def zero_of_tangent_line(c):
    my_function = lambda x: x * x * x + x - 1
    derivative = lambda x: 3 * x * x + 1

    y0 = my_function(c)
    m = derivative(c)

    return(m * c - y0) / m

def estimate_solution( initial_guess, precision ):
    new_estimate = zero_of_tangent_line( initial_guess )
    if abs(initial_guess - new_estimate) < precision:
        return new_estimate
    else:
        return estimate_solution(new_estimate, precision)


answer = zero_of_tangent_line(0.5)
print(round(answer, 6))

answer = estimate_solution(0.5, 0.01)
print(round(answer, 6))
