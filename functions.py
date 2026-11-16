def times(a, b):
    return a * b


def check_answer(reply, correct):
    if reply.strip() == correct:
        return True
    else:
        return False


print(times(3, 4))
print(times(7, 8))
print(check_answer("12", "12"))
print(check_answer(" 12", "12"))
print(check_answer("13", "12"))