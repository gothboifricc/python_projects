import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("Please enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

def translate(word):
    if results:
        for word in results:
            print(word[1])
    elif len(get_close_matches(word, results[0])) > 0:
        check = input("Did you mean %s instead? If Yes please enter Y or if No please enter N: " % get_close_matches(word, results[0])[0])
        if check == "Y" or "y":
            return results[get_close_matches(word, results.keys())[0]]
        elif check == "N" or "n":
            return "Oops, we did not understand your word. Please try again."
        else:
            return "We did not understand your query :)"
    else:
        print("No such word found!")

output = translate(word)
print(output)