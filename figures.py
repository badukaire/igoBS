#!/bin/bash



gListOfficialLineSizes = [ 7, 9, 13, 19, 28, 41 ]


liLines0 = 0
liSize0 = 0
liStones0 = 0
liArea0 = 0
liArea1 = 0
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
        print "- ratio lines : %.2f, size: %.2f" % (lfRatioLines, lfRatioSize)
        print "- diff  stones: %4d, area: %4d" % (liDiffStones, liDiffArea)
        print "- ratio stones: %.4f, area: %.4f" % (lfRatioStones, lfRatioArea)
        if not liArea1 == 0 :
            print "compare with previous-previous :"
            lfRatioStones = float(liStones) / liStones1
            lfRatioArea = float(liArea) / liArea1
            print "- ratio stones: %.4f, area: %.4f" % (lfRatioStones, lfRatioArea)
        liStones1 = liStones0
        liArea1 = liArea0
    liLines0 = liLines
    liSize0 = liSize
    liStones0 = liStones
    liArea0 = liArea
    print "--"


