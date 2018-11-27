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
def adjust_cores(cores,pattern):
    partitions = []
    # 1. find intersected rules
    intersected_rules = find_intersected_rules(pattern, rules)
    # 2. for each intersected rule create rule partitions
    [partitions.append(create_rule_partitions(rule,pattern)) for rule in intersected_rules]
    print('these the partitions of the intersected rules: ')
    [print(partition) for partition in partitions]
    # 3. create all the combinations
    combinations = create_combinations_from_rule_partitions(partitions)
    print('C O M B I N A T I O N S','\n',combinations)
    # 4. find the combination with maximum volume
    # 4.1 calculate the volume of each combination
    volumes_of_the_combinations = partition_volumes(combinations) 
    print('volumes_of_the_combinations',volumes_of_the_combinations)
    index_of_max_volume = find_combination_with_maximum_volume(volumes_of_the_combinations)
    result = combinations[index_of_max_volume]
    print('....................................')
    adjusted_cores = []
    [adjusted_cores.append(rule) for combination in result for rule in combination if rule not in adjusted_cores]
    print(adjusted_cores)
    # Convert rules into  [ set, . . . set, class] format


#    If the pattern intersects a core of different class, there are two possibilities:
#    1. inside the core
#    One dimension
#Example 1
rules = [ [{8},{3,5},'A'] ]
pattern =  (8,   4,  'B')
#Example 2
rules = [ [{8},{3,5,7},'A'] ]
pattern =  (8,   4,  'B')
#    Two dimensions
#Example 3
rules = [ [{8,11},{3,5},'A'] ]
pattern =  (9,   4,  'B')
#Example 4
rules = [ [{8,11,14},{3,5},'A'] ]
pattern =  (9,   4,  'B')

#    2. on the border
#Example 5
rules = [ [{8,10},{3,5,7},'A'] ]
pattern =  (9,  3,  'B')

# Two rules intersected by a new pattern inside the cores.
#Example 6
rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
pattern = (8,5,'B')


adjust_cores(rules,pattern) 

