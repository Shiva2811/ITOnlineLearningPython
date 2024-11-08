#create a function that takes a string of text as input

def inputText(text):
    # Initialize an empty dictionary to store word freqiencies
    frequency ={}

    #Define a helper recursive function to update frequency
    def update_frequency(words):
        #Base case : if there are no more words to process, retirn 
        if not words:
            return
        
        #Take the first word
        word = words[0]

        #update the dictionary with word frequency
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
        
        #Recursive call wiht the rest of the words
        update_frequency(words[1:])
    
    #special case : handle empty input
    if not text:
        return "Input is empty!"
    
    #prosess the text into word (lowercase and split with whitespace)
    words = text.lower().split()

    #start recursive processing of words
    update_frequency(words)

    return frequency

#Example usage : 
text = "Hello we are performing word frequency counter."
print(inputText(text))