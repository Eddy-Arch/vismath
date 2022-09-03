from src.ops import val
from src.vis import trace, draw_dot
a = val(5.0, label='a')
b = val(-2.0, label='b')
# equation
c = a * b; c.label = 'C' 
d = c - a + b

print(d)
draw_dot(d).render(filename='img/g1')
