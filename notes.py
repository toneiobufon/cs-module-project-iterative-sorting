def foo(n):
    sq_root = int(math.sqrt(n))
    for i in range(0, sq_root):
        print(i)
#B. Problem Two
#36 ->6
# 100 -> 10
# 10000 -> 100
# O(log(n)

##############################################################
def bar(x):
    sum = 0
    for i in range(0, 1463):
        i += 1
        for j in range(0, x):
                for k in range(x, x + 15):
                    sum += 1

##############################################################

#C. Problem Three


def baz(array):
    print(array[1])
    midpoint = len(array) // 2
    for i in range(0, midpoint):
        print(array[i])
    for _ in range(1000):
        print('hi')
#Do both of these functions have the same runtime? (Notice the difference between their inputs)



def make_num_pairs(n):
    for num_one in range(n):
        for num_two in range(n):
            print(num_one, num_two)



def make_item_pairs(items):
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)