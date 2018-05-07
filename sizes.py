#!/bin/bash

import sys

if len(sys.argv) < 2 :
    print "need a parameter"
    sys.exit(1)

lsParam = sys.argv[ 1 ]
print "param:", lsParam

try :
    liParam = int(lsParam)
except :
    print "need a numerical parameter"
    sys.exit(1)



giBase = 8

print "liParam:%d, giBase:%d" % (liParam, giBase)

giValue = giBase
giPrev = 0

for iLoop in range(liParam + 1) :

    giHalf = giPrev / 2
    giValue += giHalf
    print "#%d: %d + %d = %d" % (iLoop, giPrev, giHalf, giValue)
    print "--"

    giPrev = giValue

print "giValue:%d" % (giValue)


