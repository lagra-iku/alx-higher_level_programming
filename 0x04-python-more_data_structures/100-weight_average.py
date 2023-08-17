#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_total, last_weight = 0, 0
    if len(my_list) == 0:
        return 0
    else:
        for i in my_list:
            prod_total = 1
            for j in i:
                prod_total *= j
            last_weight += j
            sum_total += prod_total
        return sum_total / last_weight
