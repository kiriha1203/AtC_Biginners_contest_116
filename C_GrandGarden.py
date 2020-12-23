n = int(input())
h = list(map(int, input().split()))
# list2 = [maxh()) - n for n in h]
# list2 = map(lambda x : max(h) - x, h)
# print(sum(list2))

print(sum(map(lambda x : max(h) - x, h)))