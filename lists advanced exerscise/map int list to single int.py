l = [1, 2, 3]
r = [x for x in l if x % 2 == 0]
# m = int(''.join(map(str, l)))
r = int(''.join(map(str, r)))
print(r)
