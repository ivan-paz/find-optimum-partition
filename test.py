#
import sys
from find_intersected_rules import find_intersected_rules
from create_rule_partitions import create_rule_partitions
from create_combinations_from_rule_partitions import create_combinations_from_rule_partitions
from partitions_volumes import partition_volumes
from compare_partitions_volumes import find_combination_with_maximum_volume

def test(l):
    l()
    sys.stdout.write('.')

def xxx():
    rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
    pattern = (7,5,'B')
    assert find_intersected_rules(pattern, rules) == [[{6,10},{4,6},'A']]
test(xxx)

def xxx():
    rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
    pattern = (8,5,'B')
    assert find_intersected_rules(pattern, rules) == [ [{6,10},{4,6},'A'],[{8},{3,7},'A'] ]
test(xxx)

def xxx():
    rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
    pattern = (8,5,'B')
    assert find_intersected_rules(pattern, rules) == [ [{6,10},{4,6},'A'],[{8},{3,7},'A'] ]
test(xxx)
 
def xxx():
    R1 = [ {1,2,3,8,11}, {4,6}, 'A' ]
    R2 = ( 5, 4, 'B')
    assert create_rule_partitions( R1, R2 ) == [[[(1, 2, 3), {4, 6}, 'A'], [(5,), 4, 'B'], [(8, 11), {4, 6}, 'A']]]
test(xxx)

def xxx():
    R1 = [ {1,2,3,8,11}, {4,6}, 'A' ]
    R2 = ( 5, 5, 'B')
    assert create_rule_partitions( R1, R2 ) == [[[(1, 2, 3), {4, 6}, 'A'], [(5,), 5, 'B'], [(8, 11), {4, 6}, 'A']], [[{8, 11, 2, 3, 1}, (4,), 'A'], [5, (5,), 'B'], [{8, 11, 2, 3, 1}, (6,), 'A']]]
test(xxx)

def xxx():
    R1 = [ {6,10}, {4,6}, 'A' ]
    R2 = ( 7, 5, 'B')
    assert create_rule_partitions( R1, R2 ) == [[[(6,), {4, 6}, 'A'], [(7,), 5, 'B'], [(10,), {4, 6}, 'A']], [[{10, 6}, (4,), 'A'], [7, (5,), 'B'], [{10, 6}, (6,), 'A']]]
test(xxx)

def xxx():
    partitions =  [[[[(6,), {4, 6}, 'A'], [(8,), 5, 'B'], [(10,), {4, 6}, 'A']], [[{10, 6}, (4,), 'A'], [8, (5,), 'B'], [{10, 6}, (6,), 'A']]], [[[{8}, (3,), 'A'], [8, (5,), 'B'], [{8}, (7,), 'A']]]]
  
    assert create_combinations_from_rule_partitions(partitions) == [([[(6,), {4, 6}, 'A'], [(8,), 5, 'B'], [(10,), {4, 6}, 'A']], [[{8}, (3,), 'A'], [8, (5,), 'B'], [{8}, (7,), 'A']]), ([[{10, 6}, (4,), 'A'], [8, (5,), 'B'], [{10, 6}, (6,), 'A']], [[{8}, (3,), 'A'], [8, (5,), 'B'], [{8}, (7,), 'A']])] 
test(xxx)

def xxx():
    
    combinations = [(
        [[(6,), {4, 6}, 'A'], [(8,), 5, 'B'], [(10,), {4, 6}, 'A']],
        [[{8}, (3,), 'A'], [8, (5,), 'B'], [{8}, (7,), 'A']]
        ),
        ([[{10, 6}, (4,), 'A'], [8, (5,), 'B'], [{10, 6}, (6,), 'A']],
            [[{8}, (3,), 'A'], [8, (5,), 'B'], [{8}, (7,), 'A']]
            )]
    assert partition_volumes(combinations) == [[[0, 0], [4, 1]], [[0, 0], [8, 1]]]
test(xxx)

def xxx():
    volumes_of_the_combinations = [[[0, 0], [4, 1]], [[0, 0], [8, 1]]]
    assert find_combination_with_maximum_volume(volumes_of_the_combinations) == 1
test (xxx)










print('\nAll passed!')

