# Preprocess the datasets that are given 

import statistics as stats

rideFileNames = ["7_dwarfs_train", "alien_saucers", "dinosaur", "expedition_everest", "flight_of_passage", "kilimanjaro_safaris", "pirates_of_caribbean", "rock_n_rollercoaster", "slinky_dog", "soarin", "toy_story_mania"]

def readFile(filename):
    table = []
    inFile = open(filename+".csv", "r")
    lines = inFile.readlines()
    for line in lines:
        line = line.strip()
        values = line.split(',')
        convert2Num(values)
        table.append(values)
    inFile.close()
    print(len(table))
    return table[1:]

def handleMissingAttributes(table):
    for row in table:
        if row[2] == '' and row[3] == '':
            table.remove(row)
        if row[2] == '':
            row[2] = row[3]
        if row[3] == '':
            row[3] = row[2]
        if row[2] >= 240 or row[2] < 0:
            table.remove(row)

def statsPerDay(table):
    allStats = []
    dayValues = []
    dayStats = []
    parkDay = table[1][0]
    dayTracker = 0
    for row in table:
        dayTracker += 1
        if parkDay == row[0]:
            dayValues.append(row[2])
        else:
            convert2Num(dayValues)
            dayStats = [parkDay, len(dayValues), max(dayValues), min(dayValues), stats.mean(dayValues)]
            dayValues = []
            dayValues.append(row[2])
            allStats.append(dayStats)
            dayStats = []
            parkDay = table[dayTracker][0]
        # get values per day, then get high/low/avg
    return allStats


def convert2Num(values):
    for i in range(len(values)):
        try:
            numericValue = float(values[i])
            values[i] = numericValue
        except ValueError:
            continue

def writeData(table, filename):
    outfile = open(filename, "w")
    for row in table:
        for i in range(len(row) -1):
            outfile.write(str(row[i]) + ',')
        outfile.write(str(row[-1]) + "\n")
    outfile.close()

def main():
    table = readFile("dinosaur")
    handleMissingAttributes(table)
    allStats = statsPerDay(table)
    writeData(allStats, "wait_time_dates.csv")

main()