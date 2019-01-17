from sympy import symbols, diff

a = 7
b = 6
c = 6

a0 = 7.02
b0 = 5.97
c0 = 5.99

x, y, z = symbols('x y z', real=True)
f = (x**2 + y**2 + z**2)**(1/2.0)
par_x = diff(f, x)
par_y = diff(f, y)
par_z = diff(f, z)

par_x = par_x.subs([(x, 7), (y, 6), (z, 6)])
par_y = par_y.subs([(x, 7), (y, 6), (z, 6)])
par_z = par_z.subs([(x, 7), (y, 6), (z, 6)])

L = f.subs([(x, 7), (y, 6), (z, 6)]) + par_x*(a0 - a) + par_y*(b0-b) + par_z*(c0-c)

print (L)
