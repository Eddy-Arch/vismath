# vismath
A cute little visual maths lib that helps build
and visualize equations.


It can do:
- Addition
- Multiplication
- divison
- subtraction

The following is an example of how the library can be used
to graph out the golden ratio sequence.

```
from src.ops import val
from src.vis import trace, draw_dot
a = val(0.0, label='a')
b = val(1, label='b')
# equation
while b.data < 100:
    print(b)
    a, b = b, a+b

draw_dot(b).render(filename='img/g1')
```
and here is the graph for the example
![Golden ratio graphed using vismath](https://cdn.discordapp.com/attachments/902436729758310451/1015417800845701130/unknown.png)
