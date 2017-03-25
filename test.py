__author__ = 'zhanghengyang'


test_q = "GGBBBGBGB"

def func(q):

    flag = 1
    index_list = []
    oppo_index_list = []
    index_skip = -1
    n = 0
    cost_1 = 0 
    cost_2 = 0

    print 1
    while(flag != -1):
        temp = q.find('G', index_skip+1 )
        flag = temp

        if flag != -1:
            index_list.append(flag)
            index_skip = index_list[n]
            n += 1

    for i in range(len(q)):
        if i not in index_list:
            oppo_index_list.append(i)

    for i,j in enumerate(index_list):
        cost_1 += j-i
    for i,j in enumerate(oppo_index_list):
        cost_2 += j-i
    print index_list
    print oppo_index_list
    print cost_1, cost_2
    return min([cost_1,cost_2])

print func(test_q)


