# import time
# import sys

# for i in range(100):
#     time.sleep(1)
#     sys.stdout.write("\r.............................%d%%Completed" % i)
#     sys.stdout.flush()

from time import sleep
import sys
var = 1 

for i in range(21):
    sys.stdout.write('\r')
    # the exact output you're looking for:
    print "one"
    if var==1:
    	break
    sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
    sys.stdout.flush()
    sleep(0.25)