# Create a function to eliminate the repetitive code.
def dissect(a_list):
    for item in a_list:
        print("{0}".format(item))
    print('-----------------------')


my_list = ["abacab", 575, "rex, the wonder dog", 24, 5, 6]
dissect(my_list)

my_list.append("end")
dissect(my_list)

my_list.insert(0,"begin")
dissect(my_list)

string_list = ['delta', 'charlie', 'bravo', 'alpha']
dissect(string_list)

string_list.sort()
dissect(string_list)
