from src.ops import val
from src.vis import trace, draw_dot
a = val(0.0, label='a')
b = val(1, label='b')
# equation
while b.data < 100:
    print(b)
    a, b = b, a+b

draw_dot(b,'png').render(filename='img/goldenratio')
