words = {}

wordList = ['hello', 'hello', 'world', 'hi', 'lol']

def fillWords(words, wordList):
    for word in wordList:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words


def numOccurancesInDict(words):
    res = []
    for word in words:
        res.append(words.get(word,0))
    
    return res


words = fillWords(words, wordList)
numOccurances = numOccurancesInDict(words)

print(words)
print(numOccurances)