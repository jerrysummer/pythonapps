import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter U if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "the word doesn't exist, please double check it"
        else:
            return "We didn't understand your entry."
    else:
        return "word doesn't exist"

word = input("enter word: ")

output = translate(word)

for item in output:
    print(item)