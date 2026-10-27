score = 0

for number in range(1, 11):
    answer = input(f"What is 3 x {number}? ")
    if int(answer) == 3 * number:
        print("Correct!")
        score = score + 1
    else:
        print(f"Wrong, it is {3 * number}")

print(f"You got {score} out of 10")

if score >= 8:
    status = "learnt"
elif score >= 4:
    status = "in progress"
else:
    status = "not started"

print(f"Status: {status}")