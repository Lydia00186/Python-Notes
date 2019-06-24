'''
testing environment for the solver of a quadratic equation
'''
#import the quadSolver module

#from quadSolver import quadSolver


from quadSolver import quadSolver as getRoots

# simple example
a = 1
b = 0
c = 4
p = 1.0e-8







#Version 1
# modle funciotn
#result = quadSolver.quadSolver(a,b,c)


#Version 2:
#from quadSolver import

#Version 3:
#   function' allas
# module  funciotn   it's allas

# result = getRoots(a, b, c)       # with default precision
result = getRoots(a, b, c, p)     # with explicit precision

print ("result: ", result)

print ("Solution of the quadratic equation:")
print ("  %.2f * x**2 + %.2f * x + %.2f = 0" % (a, b, c))
print ("note: float precision used : %.2f" % p)

# > get tuple data with an index value starting from 0
# error case
if result[0] < 0:
    print ("implementation error: '%s'"  % result[1])

# constant case
elif result[0] == 0:
    print ("constant case: '%s'"  % result[1])

# linear case
elif result[0] == 1:
    print ("linear case: '%s"  % result[1])
    print ("x = %.4f"  % result [2])

#real quadratic case
elif result[0] == 2:
    print ("real quadratic case: '%s'"  % result[1])
    print ("x1 = %10.4f"  % result[2])
    print ("x2 = %10.4f"  % result[3])

#complex quadratic case
elif result[0] == 3:
    print ("complex quadratic case: '%s'"  % result[1])
    print ("x1 = %10.4f + i * %10.4f"  % (result[2].real, result[2].imag))
    print ("x2 = %10.4f - i * %10.4f"  % (result[3].real, result[3].imag))







