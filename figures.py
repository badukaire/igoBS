#!/bin/bash



gListOfficialLineSizes = [ 6, 9, 13, 19, \
    28, 41, 61, 91, 136, \
]
"""
[
    203, 304, 455, 682, \
    1021, 1531, 2296, 3444, \
    5166, 7749, 11623, 17434, \
    26151, 39226, 58839, 88258, \
]
"""


gListSizes = []

liLines0 = 0
liSize0 = 0
liStones0 = 0
liArea0 = 0
liArea1 = 0
liDiffLines = 0
liDiffSize = 0
lfRatioLines = .0
lfRatioSize = .0
liDiffStones = 0
liDiffArea = 0
lfRatioStones = .0
lfRatioArea = .0
lfRatioStones2 = .0
lfRatioArea2 = .0
for liLines in gListOfficialLineSizes :
    liSize = liLines - 1
    print "board lines: %2d => size: %2d" % (liLines, liSize)
    liStones = liLines * liLines
    liArea = liSize * liSize
    print "stones: %3d, area: %3d" % (liStones, liArea)
    if not liLines0 == 0 :
        liDiffLines = liLines - liLines0
        liDiffSize = liSize - liSize0
        lfRatioLines = float(liLines) / liLines0
        lfRatioSize = float(liSize) / liSize0
        liDiffStones = liStones - liStones0
        liDiffArea = liArea - liArea0
        lfRatioStones = float(liStones) / liStones0
        lfRatioArea = float(liArea) / liArea0
        print "compare with previous :"
        print "- diff  lines : %4d, size: %4d" % (liDiffLines, liDiffSize)
        print "- ratio lines : %.4f, size: %.4f" % (lfRatioLines, lfRatioSize)
        print "- diff  stones: %4d, area: %4d" % (liDiffStones, liDiffArea)
        print "- ratio stones: %.4f, area: %.4f" % (lfRatioStones, lfRatioArea)
        if not liArea1 == 0 :
            print "compare with previous-previous :"
            lfRatioStones2 = float(liStones) / liStones1
            lfRatioArea2 = float(liArea) / liArea1
            print "- ratio stones: %.4f, area: %.4f" % (lfRatioStones2, lfRatioArea2)
        liStones1 = liStones0
        liArea1 = liArea0
    liLines0 = liLines
    liSize0 = liSize
    liStones0 = liStones
    liArea0 = liArea

    lTup = ( liLines, liSize, liStones, liArea, liDiffSize, liDiffStones, lfRatioStones, lfRatioSize, liDiffArea, lfRatioArea, lfRatioStones2, lfRatioArea2, )
    gListSizes.append(lTup)

    liRows = len( lTup )
    print "rows:", liRows
    print "--"


for liCol in range( liRows ) :
    lsRow = "|"
    for lListSize in gListSizes :
        xCol = lListSize[ liCol ]
        #print xCol.__class__
        if isinstance(xCol, float) :
            lsCol = " %1.4f |" % xCol if not xCol == .0 else "    --  |"
        else :
            lsCol = " %5d  |" % xCol if not xCol == 0 else "    --  |"
        #print "col:", lsCol
        lsRow += lsCol
        #print "-"
    print lsRow

