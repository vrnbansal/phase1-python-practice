import csv

score = 0

with open("questions.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        reply = input(row["question"] + " = ")
        if reply == row["answer"]:
            print("Correct!")
            score = score + 1
        else:
            print("Not quite, the answer is", row["answer"])

print("Your score:", score)