'''
function to solve a quadratic equation

a*x**2 + b*x + c = 0

result will we returned in a tuple

b = 0?  -> type = 0; (type, message,)           constant case
a = 0?  -> type = 1; (type, message, x)         linear case
d >= 0?  -> type = 2; (type, message, x1,x2)   real quadratic case
d < 0?  -> type = 3; (type, message, x1,x2)    complex quadratic case
'''
#    optimal parameter for the precision
def quadSolver(a,b,c,p = 1.0e-8):

    #check input parameters
    a = float(a)
    b = float(b)
    c = float(c)

    #not the quadratic case
    if abs(a) < p:

        #not a linear case
        if abs(b) < p:

            #infinite solutions
            if abs(c) < p:
                return (0, "infinit solutions")

            #no sulution
            else:
                return (0,"no solution available")

        #linear solution
        else:
            return (1, "linear case", -c/b)

    #quadratic case
    else:
        d = b**2 - 4*a*c

        #real case
        if d > 0:
            from math import sqrt as rsqrt
            x1 = (-b + rsqrt(d)) / (2 * a)
            x2 = (-b - rsqrt(d)) / (2 * a)
            return (2, "real quadratic case", x1,x2)

        #complex case
        else:
            from cmath import sqrt as csqrt
            x1 = (-b + csqrt(d)) / (2 * a)
            x2 = (-b - csqrt(d)) / (2 * a)
            return (3, "complex quadratic case", x1, x2)


    return (-1, "case not implented!")


