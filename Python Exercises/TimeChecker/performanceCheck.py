'''
check the performance of tuples and lists

'''

from TimeChecker import TimeChecker

# create TimeChecker object
tc = TimeChecker()

# containers for append check
t = ()    # tuple immutable data type
l = []   # list  mutable data type
n = 100000   # number of items

# check the list
tc.set()  # set a time point

for i in range(n): l += (i,)

pL = tc.get()  # get time span in seconds
print ("create list with %d items in %.3f s." % (n,pL))

# check the tuple

for i in range(n): t += (i,)

pL = tc.get()  # get time span in seconds
print "create list with %d items in %.3f s." % (n,pL)



