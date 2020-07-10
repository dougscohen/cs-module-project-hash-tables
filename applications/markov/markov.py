import random

# Read in all the words in one go
with open("C:\\Users\\dougcohen\\Repos\\CS\\cs-module-project-hash-tables\\applications\\markov\\input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here


# words = 'Cats and dogs and birds and fish dogs birds'

def markov(text):
    
    words = text.split()
    
    cache = {}

    for i, word in enumerate(words):
        
        if i == (len(words) - 1):
            break
        if word not in cache:
            cache[word] = [words[i + 1]]
        else:
            cache[word].append(words[i + 1])
        
    stop_words = []
    
    for i in cache:
        if i[-1] in '.?!':
            stop_words.append(i)
            
    return stop_words
# words = words.split()
# print(len(words))

# TODO: construct 5 random sentences
# Your code here




print(markov(words))

