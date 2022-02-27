
n = int(input())

ll_positives = []
ll_negatives = []

for i in range(n):
    num = int(input())
    if num >= 0:
        ll_positives.append(num)
    else:
        ll_negatives.append(num)
print(ll_positives)
print(ll_negatives)
print(f'Count of positives: {len(ll_positives)}. Sum of negatives: {sum(ll_negatives)}')
