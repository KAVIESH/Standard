import csv
import math
with open('data.csv', newline = '') as F:
    reader = csv.reader(F)
    file_data = list(reader)
data = file_data[0]
#Finding Mean

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += x

    mean = total/n
    return mean
squaredList = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squaredList.append(a)
sum = 0
for i in squaredList:
    sum = sum + i
result = sum/(len(data)-1)
standardDaviation = math.sqrt(result)
print(standardDaviation)
