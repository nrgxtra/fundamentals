num = int(input())
num1 = int(input())
num2 = int(input())


def smallest(a, b, c):
    ll_n = [num, num1, num2]
    ll_sm = sorted(ll_n)

    return ll_sm[0]


print(smallest(num, num1, num2))
