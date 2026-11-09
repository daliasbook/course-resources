# Sports category: three questions and a score.


def play(player_name):
    print()
    print("SPORTS")
    questions = [
        "How many players does a football team have on the field?",
        "In which sport do you score a touchdown?",
        "How many rings are on the Olympic flag?",
    ]
    answers = [
        "11",
        "american football",
        "5",
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

    print(f"{player_name}, you got {score} out of {len(questions)} in Sports.")
    return score
