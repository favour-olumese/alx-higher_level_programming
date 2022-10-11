st_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        while True:
            division = 0
            try:
                division = my_list_1[i]/my_list_2[i]
            except ZeroDivisionError:
                print('division by 0')
            except TypeError:
                print('wrong type')
            except IndexError:
                print('out of range')
            finally:
                new_list.append(division)
            break

    return new_list
