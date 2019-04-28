def bubble_sort(list):
    new_list = list[:]
    num_pairs = len(new_list) - 1
    for j in xrange(num_pairs):
        for i in xrange(num_pairs - j):
            if new_list[i] > new_list[i+1]:
                new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
    return new_list

# test list
my_list = [20, 1043, 59, 981, 38, 2, 14, 42]
new_list = bubble_sort(my_list)
print "Here's your list of numbers:"
print my_list
print "Here's the list after bubble sort:"
print new_list
