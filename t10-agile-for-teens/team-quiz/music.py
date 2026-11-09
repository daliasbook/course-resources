# Music category: three questions and a score.


def play(player_name):
    print()
    print("MUSIC")
    questions = [
        "How many strings does a standard guitar have?",
        "How many lines are there in a music staff?",
        "Which instrument has black and white keys?",
    ]
    answers = [
        "6",
        "5",
        "piano",
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

    print(f"{player_name}, you got {score} out of {len(questions)} in Music.")
    return score
