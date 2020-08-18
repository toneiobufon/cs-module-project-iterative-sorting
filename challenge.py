# [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# The expected output for the above input is:
# 27
# 81
# 9
# 27
# 99
# 63
# 42
#You may use whatever programming language you wish.
a = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

def by3(a):
    b= []
    for i in a:
        if i%3 == 0:
            b.append(i)
    return b
print(by3(a))