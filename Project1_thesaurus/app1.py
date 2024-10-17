import json
from difflib import get_close_matches

data = json.load(open("Project_thesaurus/data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff = 0.8)) > 0:
        check = input("Did you mean %s instead? If Yes press Y or if No then press N: " % get_close_matches(word, data.keys(), cutoff = 0.8)[0
        ])
        if check == "Y" or "y":
            return data[get_close_matches(word, data.keys(), cutoff = 0.8)[0]]
        elif check == "N" or "n":
            return "Oops, we did not understand your word. Please try again."
        else:
            return "We did not understand your query :)"
    else: 
        return "This word doesn't exist. Please double check again :)"

word = input("Please enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
