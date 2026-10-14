numStops = int(input())
stops = list(map(int, input().split()))
 
 
shortest = 100000000
store = 0
for i in range(numStops - 2):
    distance = stops[i+2] - stops[i]
    if distance < shortest:
        shortest = distance
        store = i+1
        
stops.remove(stops[store])
 
length = len(stops)
for i in range (length-1):
    distance = stops[i+1] - stops[i]
    if distance > shortest:
        shortest = distance
 
 
print(shortest)