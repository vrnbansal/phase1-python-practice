import csv


def check_answer(reply, correct):
    return reply.strip() == correct


score = 0
total = 0

try:
    with open("questions.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            reply = input(row["question"] + " = ")
            total = total + 1
            if check_answer(reply, row["answer"]):
                print("Correct!")
                score = score + 1
            else:
                print("Not quite, the answer is", row["answer"])
except FileNotFoundError:
    print("I could not find questions.csv. Check you are in the phase1 folder.")
else:
    print("Your score:", score, "out of", total)
    with open("results.txt", "a") as results:
        results.write("Score: " + str(score) + " out of " + str(total) + "\n")
    print("Score saved to results.txt")