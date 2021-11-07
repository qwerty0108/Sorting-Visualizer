import time

def bubble_sort(data, drawData, timeTick):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['yellow' if x == j or x == j+1 else "#A90042" for x in range(len(data))])
                time.sleep(timeTick)           # we can set time as per our speedscale now
    
    drawData(data, ['blue' for x in range(len(data))])