# file =open("test.txt")
# file.close()

# read line and store in the list
# reverse the list
# Write back to test file

with open("test.txt", 'r') as reader:
    content = reader.readlines()  # ["firstLine", "secondline", "thirdline", "forthline"]
    reversedList = reversed(content)  # reverse method to reverse the list
    
    with open("test.txt", 'w') as writer:
        for line in reversedList:
            writer.write(line)      # forthline , thirdline , secondline , firstLine

