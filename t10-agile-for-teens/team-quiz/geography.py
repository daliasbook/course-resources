# Geography category: three questions and a score.


def play(player_name):
    print()
    print("GEOGRAPHY")
    questions = [
        "What is the capital of Romania?",
        "What is the longest river in Europe?",
        "On which continent is Egypt?",
    ]
    answers = [
        "bucharest",
        "volga",
        "africa",
    ]
    score = 0

    for i in range(len(questions)):
        print(f"Question {i + 1}: {questions[i]}")
        answer = input("> ").strip().lower()
        if answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer was: {answers[i]}")

    print(f"{player_name}, you got {score} out of {len(questions)} in Geography.")
    return score
