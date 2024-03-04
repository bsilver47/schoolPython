def main():
    print("For the following questions, please answer honestly.")
    print("The Rosenberg Test is taken by scaling each answer to the following questions")
    print('as "Strongly Disagree", "Disagree", "Agree", "Strongly Agree".')
    print("For the sake of this test, please type your answer as a whole")
    print("number 1-4, with 1 being Strongly Disagree, and 4 being Strongly Agree.")
    print("Please remember that this test is purely for informational and metacognative")
    print("purposes only.")
    print("Whatever the outcome, please do not take the results too hard.")
    print("If you are ready, we will start now.")

    q_one = int(input("1. I feel that I am a person of worth, at least on an equal plane with others. "))
    q_two = int(input("2. I feel that I have a number of good qualities. "))
    q_three = int(input("3. All in all, I am inclined to feel that I am a failure. "))
    q_four = int(input("4. I am able to do things as well as most other people. "))
    q_five = int(input("5. I feel I do not have much to be proud of. "))
    q_six = int(input("6. I take a positive attitude toward myself. "))
    q_seven = int(input("7. On the whole, I am satisfied with myself. "))
    q_eight = int(input("8. I wish I could have more respect for myself. "))
    q_nine = int(input("9. I certainly feel useless at times. "))
    q_ten = int(input("10. At times I think I am no good at all. "))

    score = one_two(q_one)
    score += one_two(q_two)
    score += three_five(q_three)
    score += one_two(q_four)
    score += three_five(q_five)
    score += one_two(q_six)
    score += one_two(q_seven)
    score += three_five(q_eight)
    score += three_five(q_nine)
    score += three_five(q_ten)

    if score < 15:
        print("I am sorry to say that, based on the results of your test, you may have low self-esteem.")
        print(f"Evidentally, your numerical results are that you scored: {score}")
    else:
        print("Well done!")
        print(f"Your ultimate score was {score}")



def one_two(question):
    if question == 1:
        score = 0
    elif question == 2:
        score = 1
    elif question == 3:
        score = 2
    else:
        score = 3
    
    return score

def three_five(question):
    if question == 1:
        score = 3
    elif question == 2:
        score = 2
    elif question == 3:
        score = 1
    else:
        score = 0

    return score
    

main()