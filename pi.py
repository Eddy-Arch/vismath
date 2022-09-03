from src.ops import val
from src.vis import trace, draw_dot
s = val(0.0, label='A')
k = val(1, label='B')
g = val(4, label = "4 constant")
# equation

for i in range(50):

    # even index elements are positive
    if i % 2 == 0:
        s += g/k
    else:

        # odd index elements are negative
        s -= g/k

    # denominator is odd
    k += val(2)

print(s)
draw_dot(s).render(filename='img/g1')
