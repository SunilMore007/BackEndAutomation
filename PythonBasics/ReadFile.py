fileobject = open("test.txt")
#print(fileobject.read())   #reads all the contents from the file

#print(fileobject.read(12))   #reads first 12 charactres  from the file
#print(fileobject.readline())   #reads the firstline from the file
#print(fileobject.readline())

#print line by line using readLine method

# line= fileobject.readline()
# while line!="":
#     print(line)
#     line=fileobject.readline()

#print line by line using readLines method
#values =["FirstLine", "secondline", "thirdline", "forthline"]
for line in fileobject.readlines():     # reads all the lines are list
    print(line)

fileobject.close()