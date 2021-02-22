
# i think the sqrt fn is supposed to be implicitly hardcoded here
# otherwise, I'd pass in the fn (and value) as parameters


def update_bounds(bounds):
    midpoint = (bounds[0] + bounds[1]) / 2
    if midpoint * midpoint > 2:
        bounds[1] = midpoint
    else:
        bounds[0] = midpoint


def estimate_root(prescision):
    bounds = [1, 2]
    while bounds[1] - bounds[0] > prescision:
        update_bounds(bounds)

    return (bounds[0] + bounds[1]) / 2

print(estimate_root(0.1))
