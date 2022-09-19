import math

def quad_eq(a, b, c):
    #по определению квадратного уравнения считаем, что a != 0
    if (math.isclose(a, 0) == True):
        print("Error. It's not quadratic equation.")
        return -1
    #считаем дискриминант
    D = b*b - 4*a*c
    if D > 0:
        x_1 = (-b + math.sqrt(D))/(2*a)
        x_2 = (-b - math.sqrt(D))/(2*a)
        return (x_1, x_2)
    elif math.isclose(D, 0) == True:
        x_1 = -b/(2*a)
        return (x_1, x_1)
    else:
        return None
    
assert quad_eq(0, 3, -4) == -1
    
assert quad_eq(4, 0 , -1) == (0.5, -0.5)
assert quad_eq(4, 0 , 1) == None
assert quad_eq(1, -10, 25) == (5.0, 5.0)
assert quad_eq(1, -4, 3) == (3.0, 1.0)
assert quad_eq(1, 4, 3) == (-1.0, -3.0)
assert quad_eq(1, 4, 3) == (-1.0, -3.0)
assert quad_eq(6, -1, -1) == (0.5, -1/3)
assert quad_eq(4, 12, 9) == (-1.5, -1.5)