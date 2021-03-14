
estimate_derivative = lambda f, c, delta: (f(c + delta / 2) - f(c - delta / 2)) / delta

def zero_of_tangent_line(f, c, delta):
    m = estimate_derivative(f, c, delta)
    return(m * c - f(c)) / m

def estimate_solution( f, initial_guess, delta, precision ):
    new_estimate = zero_of_tangent_line( f, initial_guess, delta )
    if abs(initial_guess - new_estimate) < precision:
        return new_estimate
    else:
        return estimate_solution(f, new_estimate, delta, precision)

f = lambda x: x**3 + x - 1

answer = estimate_derivative(f, 0.5, 0.001)
print(round(answer, 6))

answer = zero_of_tangent_line(f, 0.5, 0.001)
print(round(answer, 6))

answer = estimate_solution(f, 0.5, 0.001, 0.01)
print(round(answer, 6))
