#
from calculate_volume_of_a_ruleset import volume_of_the_ruleset, sum_equal_dimensions

#combinations = [(
#    [[(6,), {4, 6}, 'A'], [(8,), 5, 'B'], [(10,), {4, 6}, 'A']], [[{8}, (3,), 'A'], [8, (5,), 'B'], [{8}, (7,), 'A']]
#    ), 
#    ([[{10, 6}, (4,), 'A'], [8, (5,), 'B'], [{10, 6}, (6,), 'A']], [[{8}, (3,), 'A'], [8, (5,), 'B'], [{8}, (7,), 'A']]
#        )]
def partition_volumes(combinations):
    combinations_volumes = []
    for combination in combinations:
        combination_volume = []
        print('combination\n', combination)
        # Each partition is the partition of a rule
        for partition in combination:
            volume_of_the_partition = volume_of_the_ruleset(partition)
            [combination_volume.append(x) for x in volume_of_the_partition]
#        print('combination volume',combination_volume)
        combination_volume = sum_equal_dimensions(combination_volume)
#        print('combination volume',combination_volume)
        combinations_volumes.append(combination_volume)
    return combinations_volumes
#print(partition_volumes(combinations))
