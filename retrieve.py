import preprocess

def getDateWaitTimes(table, date):
    for row in table:
        if date in row[0]:
            print(row)


def main():
    table = preprocess.readFile("wait_time_dates")
    getDateWaitTimes(table, "01/03/2012")

main()


    