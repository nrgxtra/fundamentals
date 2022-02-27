
n = int(input())
highest_snowballValue = 0
h_snow = 0
h_time = 0
h_quality = 0
for i in range(n):
    snowballSnow = int(input())
    snowballTime = int(input())
    snowballQuality = int(input())
    snowballValue = (snowballSnow / snowballTime) ** snowballQuality
    if snowballValue > highest_snowballValue:
        highest_snowballValue = snowballValue
        h_snow = snowballSnow
        h_time = snowballTime
        h_quality = snowballQuality
print(f'{h_snow} : {h_time} = {int(highest_snowballValue)} ({h_quality})')

