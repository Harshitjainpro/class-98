def CountWordsFromFile():
    filename = input("Enter File Name: ")
    file = open(filename,'r+')
    wordCount = 0
    for line in file:
        words = line.split()
        wordCount += len(words)
    print("number of words in file")
    print(wordCount)

CountWordsFromFile()