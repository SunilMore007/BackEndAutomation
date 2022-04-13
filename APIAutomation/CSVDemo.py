import csv

with open('C:\\Users\\Sunil.more\\PycharmProjects\\BackEndAutomation\\Utilities\\LoanApp.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    # print(csvReader)
    # print(list(csvReader))

    names = []
    status = []

    for row in csvReader:
        names.append(row[0])
        status.append(row[1])
        # print(row[1])

print(names)
print(status)

Index = names.index("sunil")

print(status[Index])


with open('C:\\Users\\Sunil.more\\PycharmProjects\\BackEndAutomation\\Utilities\\LoanApp.csv', 'a') as writeCsvFile:
    write = csv.writer(writeCsvFile)
    write.writerow(['amars', 'approveds'])
