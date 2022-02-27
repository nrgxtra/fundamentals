
n = int(input())
cc = 0
for i in range(n):
    cl = int(input())
    cc += cl
    if cc > 255:
        print('Insufficient capacity!')
        cc -= cl
print(cc)
