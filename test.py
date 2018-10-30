#
from find_intersected_rules import find_intersected_rules
import sys

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




print('\nAll passed!')

