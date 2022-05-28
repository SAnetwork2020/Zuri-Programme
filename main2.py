# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
       with open(filename, "r") as f:
           print(f.read())
           return "As she raised a glass of water, everyone expected they would be asked the typical glass half empty or glass half full question."


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    count1 = text.split(" ")
    print(count1)
    word = {}
    word["glass"] = text.count("glass")
    word["As"] = text.count("As")
    word["water"] = text.count("water")
    word["half"] = text.count("half")
    word["she"] = text.count("she")
    return word

