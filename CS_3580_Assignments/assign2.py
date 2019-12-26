#!/usr/bin/env python3

print("\nDaniel Salmond")

import csv

states = frozenset([
    'Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana',
    'Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska',
    'Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania',
    'Rhode Island','South Carolina','Tennessee','Texas','Utah','Vermont','Virginia','Washington','Wisconsin','West Virginia','Wyoming'
])

with open("acs2015_county_data.csv", encoding='latin-1') as f:
    reader = csv.reader(f)
    header_counties = next(reader)
    counties = list(reader)

class CountyIndices():
    pass

i = CountyIndices()
i.state = header_counties.index("State")
i.total = header_counties.index("TotalPop")
i.unemployed = header_counties.index("Unemployment")
i.hispanic = header_counties.index("Hispanic")
i.white = header_counties.index("White")
i.black = header_counties.index("Black")
i.native = header_counties.index("Native")
i.asian = header_counties.index("Asian")
i.pacific = header_counties.index("Pacific")

stats = {}

for row in counties:
    if row[i.state] not in states:
        continue
    try:
        stats[row[i.state]]
    except KeyError:
        stats[row[i.state]] = {"total": 0,"unemployed":0,"hispanic":0,"white":0,
            "black":0,"native":0,"asian":0,"pacific":0}

    totalPop = int(row[i.total])

    stats[row[i.state]]["total"] += totalPop
    stats[row[i.state]]["unemployed"] += totalPop * (float(row[i.unemployed])/100)
    stats[row[i.state]]["hispanic"] += totalPop * (float(row[i.hispanic])/100)
    stats[row[i.state]]["white"] += totalPop * (float(row[i.white])/100)
    stats[row[i.state]]["black"] += totalPop * (float(row[i.black])/100)
    stats[row[i.state]]["native"] += totalPop * (float(row[i.native])/100)
    stats[row[i.state]]["asian"] += totalPop * (float(row[i.asian])/100)
    stats[row[i.state]]["pacific"] += totalPop * (float(row[i.pacific])/100)

races = []
unemployment = []

for k, v in stats.items():
    races.append((k, v["hispanic"]/v["total"], v["white"]/v["total"], v["black"]/v["total"], v["native"]/v["total"],
        v["asian"]/v["total"], v["pacific"]/v["total"]))
    unemployment.append((k, v["unemployed"]/v["total"]))

print("\nPart 1:")
print("Hispanic:", max(races, key=lambda r: r[1])[0])
print("White:", max(races, key=lambda r: r[2])[0])
print("Black:", max(races, key=lambda r: r[3])[0])
print("Native:", max(races, key=lambda r: r[4])[0])
print("Asian:", max(races, key=lambda r: r[5])[0])
print("Pacific:", max(races, key=lambda r: r[6])[0])

print("\nPart 2:")
print("Highest Unemployment:", max(unemployment, key=lambda p: p[1])[0])
print("Lowest Unemployment:", min(unemployment, key=lambda p: p[1])[0])

del counties, header_counties, stats, races, unemployment


print("\nPart 3:")
#Average income greater or equal to $50,000
#Average poverty greater than 50%

with open("acs2015_census_tract_data.csv",encoding='latin-1') as f:
    next(f)
    for line in f:
        line = line.strip()
        column = line.split(',')  
        if (str(column[13]) == "" or str(column[17]) == ""):
            continue 
        #try:


        if(float(column[13]) >= float(50000) and float(column[17]) > float(50)):
            print("Census Tract ID:" + str(column[0]) + ", State: " + str(column[1]) + ", County: " + str(column[2]) + ", Races: ", end=' ')
            if(float(column[6]) > 1):
                print("Hispanic", end=' ')
            if(float(column[7]) > 1):
                print("White", end=' ')
            if(float(column[8]) > 1):
                print("Black", end=' ')
            if(float(column[9]) > 1):
                print("Native", end=' ')
            if(float(column[10]) > 1):
                print("Asian", end=' ')
            if(float(column[11]) > 1):
                print("Pacific", end=' ')

            print()

        #except ValueError:
         #   continue

print("\nPart 4:")
#percentage of woman greater than 57%
#total population is at least 10,000

with open("acs2015_census_tract_data.csv",encoding='latin-1') as f:
    next(f)
    for line in f:
        line = line.strip()
        column = line.split(',')

        try:

            if(float(column[3]) > 9999 and (float(column[5])/float(column[3])) > 0.57):
                print("Census Tract ID:" + str(column[0]) + ", State:" + str(column[1]) + ", County:" + str(column[2]) + ", Races:", end=' ')
                if(float(column[6]) > 1):
                    print("Hispanic", end=' ')
                if(float(column[7]) > 1):
                    print("White", end=' ')
                if(float(column[8]) > 1):
                    print("Black", end=' ')
                if(float(column[9]) > 1):
                    print("Native", end=' ')
                if(float(column[10]) > 1):
                    print("Asian", end=' ')
                if(float(column[11]) > 1):
                    print("Pacific", end=' ')
                print()

        except ValueError:
            continue




print("\nPart 5:")
#of the 6 race categories at least four of them each have 15%.
#For example, White is 25%, Black is 16%, Hispanic is 18%, Pacific is 20%

with open("acs2015_census_tract_data.csv",encoding='latin-1') as f:
    next(f)
    for line in f:
        line = line.strip()
        column = line.split(',')

        try:
            
            dCounter = 0
            races = []
            if(float(column[6]) > 1):
                races.append("Hispanic")
                if(float(column[6]) >= 15):
                    dCounter += 1

            if(float(column[7]) > 1):
                races.append("White")
                if(float(column[7]) >= 15):
                    dCounter += 1

            if(float(column[8]) > 1):
                races.append("Black")
                if(float(column[8]) >= 15):
                    dCounter += 1

            if(float(column[9]) > 1):
                races.append("Native")
                if(float(column[9]) >= 15):
                    dCounter += 1

            if(float(column[10]) > 1):
                races.append("Asian")
                if(float(column[10]) >= 15):
                    dCounter += 1

            if(float(column[11]) > 1):
                races.append("Pacific")
                if(float(column[11]) >= 15):
                    dCounter += 1

            if(dCounter < 4):
                continue
            else:
                print("Census Tract ID:", str(column[0]), "State:", str(column[1]), "County:", str(column[2]), "Races:", end=" ")
                print(" ".join(races))

        except ValueError:
            continue