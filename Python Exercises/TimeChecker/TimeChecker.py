'''
class to fet a performance check
'''
#                            alias name

from datetime import datetime as time

#     |captal
#         |came| case
class TimeChecker:

    #  _a private
    #  _a public
    #  _a german private  (like 130k/h max on german highways)

    # constructor
    #            |instance pointer
    def  __init__(self):
        # attributes of instances are created by self
        self._stack = []   # stack memory implemented as list

    # set time point
    def set (self):
        self._stack.append(time.now())

    # get last time point from stack memory
    # and return timespan in seconds
    def get(self):
        tStart = self._stack.pop()
        tEnd   = time.now()
        return self.getTime(tEnd-tStart)



    # calculate seconds from time object
    #                | time object
    def getTime(self,t):
        s = float (t.microseconds/1.e6) \
           + float (t.seconds) \
           + float (t.days)*24.*60.*60.
        return s
