#
#    Given a new pattern and a set of connected rules
#    find the rules intersected by the pattern
#
def same_class(r1,r2):
    if r1[-1] == r2[-1]:
        return True
    else:
        return False
#print(same_class([{1},{4},'A'],[{1},{2},'A']))
#print(same_class([{1},{4},'B'],[{1},{2},'A']))

# Create interval
def create_interval(some_input):
    if type(some_input) == int or type(some_input) == float:
        some_input = set([some_input])
    minimum = min(some_input)
    maximum = max(some_input)
    return (minimum,maximum)
#print(create_interval(1) )
#print(create_interval({4,6}))

#  True if two intervals, defined by its minimum and maximum values,
#intersect each other
def interval_intersection(int1, int2):
    if ( (int1[0]<= int2[0] <= int1[1]) or (int1[0]<= int2[1] <= int1[1]) ):
        return True
    elif ( (int2[0]<= int1[0]<= int2[1]) or (int2[0]<= int1[1] <= int2[1]) ):
        return True
    else:
        return False
#print(interval_intersection( (1,11), (9,12) ) )
#print( interval_intersection( (2,5), (1,11) ) )

# intersection of numeric intervals
def intersection(r1,r2):
    if same_class(r1,r2):
        return False
    for i in range(len(r1)-1):
        interval1 = create_interval(r1[i])
        interval2 = create_interval(r2[i])
#        print(interval1,interval2,interval_intersection(interval1,interval2))
        if not interval_intersection(interval1,interval2):
            return False
    return True
#print( intersection( [{6,10},{4,6},'A'], (7,5,'B') ) )

def find_intersected_rules(pattern,rules):
    intersected = []
    for r in rules:
        if intersection(r,pattern):
            intersected.append(r)
    return intersected

#rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
#pattern = (7,5,'B')
#print(find_intersected_rules(pattern, rules))

#rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
#pattern = (8,5,'B')
#print(find_intersected_rules(pattern, rules))


#rules = [ [{1, 2}, {150}, {0.721901},'1'],[{2},{100,200},{0.721901},'1'] ]
#pattern = (   2, 120,  0.721901, '2')
#print(find_intersected_rules(pattern,rules))
