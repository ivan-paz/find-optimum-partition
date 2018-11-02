#
import itertools

partitions =  [
[
[[(6,), {4, 6}, 'A'], [(8,), 5, 'B'], [(10,), {4, 6}, 'A']], 
[[{10, 6}, (4,), 'A'], [8, (5,), 'B'], [{10, 6}, (6,), 'A']]
], 
[[[{8}, (3,), 'A'], [8, (5,), 'B'], [{8}, (7,), 'A']]]
]

def create_combinations_from_rule_partitions(partitions):
    combinations = list(itertools.product(*partitions))
    #[print(c) for c in combinations]
    return combinations
#print(create_combinations_from_rule_partitions(partitions)) 
