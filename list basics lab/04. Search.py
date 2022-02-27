
n = int(input())
word = input()

ll_strings = []
ll_filtered = []

for i in range(n):
    cs = input()
    ll_strings.append(cs)
    if word in cs:
        ll_filtered.append(cs)
print(ll_strings)
print(ll_filtered)
