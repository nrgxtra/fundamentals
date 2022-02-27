n = int(input())
l_room = []
for i in range(n):
    room = input().split(' ')
    chairs = room[0]
    count_chairs = len(chairs)
    taken = int(room[1])
    l_room.append([count_chairs, taken])
free_chairs = 0
enough = True
for j in range(len(l_room)):
    r1 = l_room[j]
    total = r1[0]
    occuped = r1[1]
    if total - occuped < 0:
        print(f'{abs(total - occuped)} more chairs needed in room {j + 1}')
        enough = False
    else:
        free_chairs += (total - occuped)
if enough:
    print(f'Game On, {free_chairs} free chairs left')
