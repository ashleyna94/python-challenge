# * Import a text file filled with a paragraph of your choosing.
# * Assess the passage for each of the following:
#   * Approximate word count
#   * Approximate sentence count
#   * Approximate letter count (per word)
#   * Average sentence length (in words)

import os


filepath = os.path.join(".", "input.txt")

word_count = {}
with open(filepath) as text:
    # text.readline() --> Reads 1 line
    # text.read() --> Reads all the line 
    
    #Appoximate word count vvv
    for row in text:
        # print(row)
        # print(row.split())
        words = row.split()
        for word in words:
            if word in word_count: 
                word_count[word] = word_count[word] + 1
            else:
                # When you saw the word for the 1st time
                word_count[word] = 1
                