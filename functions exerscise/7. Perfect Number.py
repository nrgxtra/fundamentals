n = int(input())


def perf(a):
    ll_nums = []
    for i in range(1, a):
        if a % i == 0:
            ll_nums.append(i)
    if sum(ll_nums) == a:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


perf(n)
