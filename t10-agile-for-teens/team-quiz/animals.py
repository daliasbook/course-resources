# Animals category: three questions and a score.


def play(player_name):
    print()
    print("ANIMALS")
    questions = [
        "What is the largest animal on Earth?",
        "How many legs does a spider have?",
        "Which mammal can fly?",
    ]
    answers = [
        "blue whale",
        "8",
        "bat",
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

    print(f"{player_name}, you got {score} out of {len(questions)} in Animals.")
    return score
