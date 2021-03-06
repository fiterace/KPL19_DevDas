import csv
import math

def Problem1(input_id):
    f = open('data.csv')
    csv_f = csv.reader(f)

    ID = input_id

    x = []
    y = []
    z = []
    starID = []

    soln = []
    rows = []

    x1 = 0
    y1 = 0
    z1 = 0

    header = next(csv_f)

    distance = []

    for row in csv_f:
        rows.append(row)
        row[1] = math.degrees(float(row[1]))
        row[2] = math.degrees(float(row[2]))
        row[8] = float(row[8])
        if(math.isnan(row[8])):
            continue
        # row[8] = 10**((row[8]+5)//5)
        X = (row[8]*(math.sin(row[1]))*(math.cos(row[2])))
        x.append(X)
        Y = row[8]*(math.sin(row[1]))*(math.sin(row[2]))
        y.append(Y)
        Z = row[8]*math.cos(row[1])
        z.append(Z)
        starID.append(row[0])
        if(int(row[0]) == ID):
            x1 = X
            y1 = Y
            z1 = Z

    for row in range(len(x)):
        X = (x1 - x[row])**2
        Y = (y1 - y[row])**2
        Z = (z1 - z[row])**2
        distance.append((math.sqrt(X+Y+Z)))

    idDist = dict(zip(starID, distance))
    Starlist = sorted(idDist.items(), key=lambda x: x[1])

    return Starlist[1:6] # print(i[0],i[1])
