# Root Finding การหาค่ารากของสมการ
# x^3 - 2 = x^2

# f(x) = x^3 - x -2 
def f(x):
    y = x ** 3 - x - 2
    return y

# samples = [-2, -1, 0, 1, 2]
# samples = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
samples = []
a = 1.52
while a <= 1.53:
    samples.append(a)
    a = a + 0.0001

print(samples)

for s in samples:
    print(f'f({s}) = {f(s)}')

