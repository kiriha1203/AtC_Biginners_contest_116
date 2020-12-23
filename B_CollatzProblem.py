s = int(input())

#  n/2
#  3n + 1


def odd(n):
    return int(3 * n + 1)

def even(n):
    return int(n/2)

def has_duplicates(seq):
    return len(seq) != len(set(seq))

list = []

list.append(s)

count = 1

while s < 10000:
    count+=1
    if s % 2 == 0:
        list.append(even(s))
        s = even(s)
    else:
        list.append(odd(s))
        s = odd(s)

    if has_duplicates(list):
        break

print(count)
