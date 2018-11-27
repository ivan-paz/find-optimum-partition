#
#
#       Given ( cores, new coming pattern)        
#       adjust the cores to incorporate the new instance 
#       such that the resulting cores have the maximum possible volume
#
#
from find_intersected_rules import find_intersected_rules
from create_rule_partitions import create_rule_partitions
from create_combinations_from_rule_partitions import create_combinations_from_rule_partitions
from partitions_volumes import partition_volumes
from compare_partitions_volumes import find_combination_with_maximum_volume
#If the pattern intersects a core with different class
def adjust_cores(cores,pattern):
    partitions = []
    # 1. find intersected rules
    intersected_rules = find_intersected_rules(pattern, rules)
    # 2. for each intersected rule create rule partitions
    [partitions.append(create_rule_partitions(rule,pattern)) for rule in intersected_rules]
    print('partitions')
    [print(partition) for partition in partitions]
    # 3. create all the combinations
    combinations = create_combinations_from_rule_partitions(partitions)
    print('C O M B I N A T I O N S','\n',combinations)
    # 4. find the combination with maximum volume
    # 4.1 calculate the volume of each combination
    volumes_of_the_combinations = partition_volumes(combinations) 
    print('volumes_of_the_combinations',volumes_of_the_combinations)
    index_of_max_volume = find_combination_with_maximum_volume(volumes_of_the_combinations)
    print(combinations[index_of_max_volume])


rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
pattern = (8,5,'B')
#rules = [ [{1,2}, {150},{0.721901},'1'],[{2},{100,200},{0.721901},'1'] ]
#pattern = (   2, 120,  0.721901, '2')
adjust_cores(rules,pattern) 


