# -*- coding: utf-8 -*-
"""

Function that takes a set of sets of rules, each one corresponding
to a different partition of an original connected set

e.g set1, set2, set3 . . .

and return the set (partition) with greater "volume".


"""
from copy import deepcopy
#-----------------------------------------------
# Function "compare" takes two single volumes
# that could have different volume and dimension
# [volume1, dimension1] [volume2, domension2]
# and returns the maximum considering volume
# and dimension.
#-----------------------------------------------
def compare(vol1,vol2):
    if vol1[1] > vol2[1]:
        return 1
    elif vol1[1] < vol2[1]:
        return 2
    elif vol1[0] > vol2[0]:
        return 1
    elif vol1[0] < vol2[0]:
        return 2
    else:
        return 3

#print(compare([4,1],[3,1]))

#-------------------------------------------------
#  This function takes two volumes (one beguins being the
#  winner and the other the contendent) that may have
#  different dimensions e.g [[0,0],[2,1],[2,4]] and [[3,1],[1,4]]
#  and returns:
#  1  if the winner has the bigger volume.
#  2  if the contendent has the bigger volume.
#  3  if they are tie .
#  They fight to see which one winns.
#-------------------------------------------------
def fight(winner, contendent):
    winner_copy = deepcopy(winner)
    contendent_copy = deepcopy(contendent)

    hand1 = winner[-1]
    hand2 = contendent[-1]
    result = 3

    while result == 3 and len(winner) > 0 and len(contendent) > 0:
        hand1 = winner[-1]
        del winner[-1]
        hand2 = contendent[-1]
        del contendent[-1]

        result = compare(hand1, hand2)
        if result == 1:
            return winner_copy
        if result == 2:
            return contendent_copy
        if result == 3:
            result = 3
    if result == 3:
        return winner_copy
    else:
        return result
#print( fight( [[0,0],[5,1],[4,2]], [[10,1],[4,2]]) )
#print(fight([[0,0],[1,2]],[[0,0]]))
#print(fight( [[4, 1], [0, 0]], [[8, 1], [0, 0]]))

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#   This function receives an array with the volumes of the different
#   combinations created from the different partitions of the rules 
#   -the different ways of solving the contradictions-
#   and return the index of the bigest one
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def find_combination_with_maximum_volume(volumes_of_the_combinations):
    if volumes_of_the_combinations:
        maximum_volume = volumes_of_the_combinations[0]
    for i in range(len(volumes_of_the_combinations)):
        maximum_volume = fight(maximum_volume,volumes_of_the_combinations[i])
    for i, j in enumerate(volumes_of_the_combinations):
        if j == maximum_volume:
            index = i
    print(i)
    return i
find_combination_with_maximum_volume([[[0, 0], [4, 1]], [[0, 0], [8, 1]]])

