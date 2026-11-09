# Science category: three questions and a score.


def play(player_name):
    print()
    print("SCIENCE")
    questions = [
        "What gas do plants absorb from the air?",
        "What is the closest planet to the Sun?",
        "At how many degrees Celsius does water boil?",
    ]
    answers = [
        "carbon dioxide",
        "mercury",
        "100",
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

    print(f"{player_name}, you got {score} out of {len(questions)} in Science.")
    return score
