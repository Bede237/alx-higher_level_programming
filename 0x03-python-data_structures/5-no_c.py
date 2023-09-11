#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if (my_string[i] == 'c'):
            if i == (len(my_string) - 1):
                my_string = my_string[:i]
                return my_string
            my_string = my_string[:i] + my_string[(i + 1):]
    return (my_string)
