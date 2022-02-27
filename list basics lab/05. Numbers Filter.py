
n = int(input())
ll_nums = []
ll_result = []
for i in range(n):
    num = int(input())
    ll_nums.append(num)
command = input()
for element in ll_nums:
    if command == 'even':
        if element % 2 == 0:
            ll_result.append(element)
    elif command == 'odd':
        if element % 2 != 0:
            ll_result.append(element)
    elif command == 'negative':
        if element < 0:
            ll_result.append(element)
    elif command == 'positive':
        if element >= 0:
            ll_result.append(element)
print(ll_result)
