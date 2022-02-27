def trib(a):
    ll = []
    for i in range(1, a + 1):

        if i < 3:
            print(1, end=" ")
            ll.append(1)
        elif i == 3:
            print(2, end=" ")
            ll.append(2)
        elif i > 3:

            s = sum(ll[-3:])
            print(s, end=" ")
            ll.append(s)


trib(int(input()))
