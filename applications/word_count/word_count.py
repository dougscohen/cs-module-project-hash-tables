def word_count(s):
    # define unwanted characters to take out
    unwanted_chars ='''":;,.-+=/\|[]{}()*^&'''

    # ignore the case and make everything lower case
    lower_case = s.lower()

    # remove unwanted characters from the string
    cleaned_string = ""
    for char in lower_case:
        if char not in unwanted_chars:
            cleaned_string = cleaned_string + char

    # split the words
    word_list = cleaned_string.split()
    
    # Set empty dictionary for words (keys) and their counts (values)
    counts = {}
    
    # iterate through word list
    for word in word_list:
        # if the word exists in counts, add one to the count
        if word in counts:
            counts[word] += 1
        # otherwise, add the word as a key and make its value 1
        else:
            counts[word] = 1
            
    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))