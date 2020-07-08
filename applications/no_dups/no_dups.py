def no_dups(s):
    
    # split the string into a list of words
    words = s.split()
    
    # get unique words with no duplicates by putting in a set
    unique_words = set(words)
    
    # sort the unique words by their original positions
    sorted_words = sorted(unique_words, key=words.index)
    
    # join words into back into one string with no duplicates
    no_dups = " ".join(sorted_words)

    return no_dups



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))