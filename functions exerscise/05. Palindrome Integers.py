n = input().split(", ")


def palindrome(a):
    for i in range(len(a)):
        if a[i] == a[i][::-1]:
            print('True')
        else:
            print('False')


palindrome(n)
