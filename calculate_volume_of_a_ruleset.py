#
#
#
#
#         Functions to calculate the volume of a set of rules 
#
#
#
#
from operator import itemgetter

#    FUNCTION TO CALCULATE THE VOLUME OF A PARAMETER
def parameter_volume(parameter):
    if type(parameter) == int or type(parameter) == float:
        minimum = maximum = parameter
    else:
        minimum = min(parameter)
        maximum = max(parameter)
    volume = abs(maximum - minimum)
    return volume
#print(parameter_volume((5,)))
#print(parameter_volume((11,13,16)))
#print(parameter_volume({11,13,16}))

#Function to calculate the volume of a rule
def rule_volume(rule):
    volume = []
    dimension = 0
    for parameter in range(0,len(rule) -1 ):
        parameter_contribution = parameter_volume(rule[parameter])
        if parameter_contribution != 0:
            dimension = dimension + 1
            volume = volume + [parameter_contribution]
            #print('volume:',volume)
    volume = sum(volume)
    return [volume,dimension]
#print(rule_volume([{12}, {10, 13}, 'B']))
#print(rule_volume([{12,13}, {10, 13}, 'B']))
#print(rule_volume([{8}, (3,), 'A']))
#print(rule_volume([8, (5,), 'B']))
#print(rule_volume([{8}, (7,), 'A']))



#-------------------------------------------------------------------
# Function that receives an array with the [volume,dimension] for a set of rules
# and return the global [volume, dimension] for each dimension
#    [   VOLUME,  DIMENSION  ]
#    [   VOLUME,  DIMENSION  ]
#    [   VOLUME,  DIMENSION  ]
def sum_equal_dimensions(volumes):
    dimensions = {}
    result = []
 #   print(volumes)
    for volume in volumes:
        key = str(volume[1])
 #       print(type(key))
 #       print(key)
        if key not in dimensions:
            dimensions[key] = [0,int(key)]
#    print('the dimensions are:',dimensions)
    while len(volumes) > 0:
        temporal = volumes[0]
        volumes.remove(temporal)
        temporalkey = str(temporal[1])
        suma = dimensions[temporalkey]
        suma[0] = suma[0] + temporal[0]
        dimensions[temporalkey] = suma
    #print(dimensions)
    for key in dimensions:
        result.append(dimensions[key])
    return result    
#print(sum_equal_dimensions( [ [4.0, 2], [3.0, 1], [1.0, 1]  ] ) )
#print(sum_equal_dimensions([[3.0, 1], [4.0, 2], [1.0, 1]]) )
#print(sum_equal_dimensions([[0,0],[0,0],[0,0]]))
#print(sum_equal_dimensions([[2, 1], [0, 0], [2, 1], [0, 0], [0, 0], [0, 0]]))
#-------------------------------------------------------------------
#Function that takes an array of arrays and sort them by its second entrance
#from operator import itemgetter

def sort_volumes(volumes):
    volumes = sorted(volumes,key=itemgetter(1))
    return volumes
#sort_volumes([[4.0, 1], [4.0, 2]])
#sort_volumes([[4.0, 2], [4.0, 1]])
#print(sort_volumes([[1.0, 2], [3.0, 2], [4.0, 4]]))
#print(sort_volumes([[1.0, 2], [3.0, 2], [4.0, 4]]) )
#print(sort_volumes([[0, 0]]))
#-------------------------------------------------------------------
#Function to calculate the volume of a set of rules
# For each rule in the set
    #calculate its volume
#retur the sum of the volumes
def volume_of_the_ruleset(rules):
    volumes = []
    for rule in rules:
        print(rule)
        volume = rule_volume(rule)
        print('aportacion de la regla', volume)
        volumes = volumes + [volume]
#    print('volumes',volumes)
    volumes = sum_equal_dimensions(volumes)
    volumes = sort_volumes(volumes)
    return volumes
#print(partition_volume([[(12,), {10, 13}, 'B'], [{11, 13}, {11, 13}, 'D'], [{12,13},(10,),'B'] ]))
#print(volume_of_the_ruleset( [[(6,), {4, 6}, 'A'], [(8,), 5, 'B'], [(10,), {4, 6}, 'A'], [{8}, (3,), 'A'], [8, (5,), 'B'], [{8}, (7,), 'A'] ] ) )










