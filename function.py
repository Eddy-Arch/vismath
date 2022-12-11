from src.ops import val
from src.vis import trace, draw_dot
a = val(0.0, label='a')
b = val(1.0, label='b')
c = val(1.0, label='c')
d = val(50.0, label='d')


for n in range(50):
    print(n)
    n = (a**val(2)) +b*c

draw_dot(n, 'png').render(filename='img/fun2')
