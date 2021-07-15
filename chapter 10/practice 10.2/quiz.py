# In this programming exercise, you will create a simple trivia game for two players. 
import question


def main():
    q1 = question.Question("If soccer is called football in England, What is American football called in England? ",
                           "A. American football", "B. Combball", "C. Handball", "D. Touchdown", "A")

    q2 = question.Question("What is the largest country in the world? ", "A. Russia", "B. Canada", "C. China",
                           "D. United States", "A")

    q3 = question.Question("An organic compound is considered an alcohol if it has what functional group?",
                           "A. Hydroxyl", "B. Carbonyl", "C. Alkyl", "D. Aldehyde", "A")

    q4 = question.Question("what is the 100th digit of pi?", "A. 9", "B. 4", "C. 7", "D. 2", "A")

    q5 = question.Question("A doctor with a PhD is a doctor of what?", "A. Philosophy", "B. Psychology",
                           "C. Phrenology", "D. Physical Therapy", "A")

    q6 = question.Question("What year did World War I begin?", "A. 1914", "B. 1905", "C. 1919", "D. 1925", "A")

    q7 = question.Question("What is the tallest mountain in Canada?", "A. Mount Logan", "B. Mont Tremblant",
                           "C. Whistler Mountain", "D. Blue Mountain", "A")

    q8 = question.Question("Which of these is a stop condon in DNA?", "A. TAA", "B. ACT", "C. ACA", "D. GTA",
                           "A")

    q9 = question.Question("Which of these countries in Not a part of the Asian continent?", "A. Suriname",
                           "B. Georgia", "C. Russia", "D. Singapore", "A")

    q10 = question.Question("What country saw a world record 315 million voters turn out for elections on May 20, "
                            "1991?", "A. India", "B. United States of American", "C. Soviet Union", "D. Poland",
                            "A")

    set_1 = [q1, q2, q3, q4, q5]

    set_2 = [q6, q7, q8, q9, q10]

    player1 = 0
    player2 = 0

    print("\nPlayer1 turn.")
    for query in set_1:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter of the correct answer: ")
        if guess.upper() == query.get_answer():
            print("You are right!!")
            player1 += 1
        else:
            print("You're wrong!!")
            print("Right answer is " + query.get_answer())

    print("\nPlayer2 turn.")
    for query in set_2:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter of the correct answer: ")
        if guess.upper() == query.get_answer():
            print("You are right!!")
            player2 += 1
        else:
            print("You're wrong!!")
            print("Right answer is " + query.get_answer())

    print("Player1 earned: " + str(player1) + " points.")
    print("Player2 earned: " + str(player2) + " points.")

    if player1 < player2:
        print("Player1 WON.")
    elif player2 < player1:
        print("Player2 WON.")
    elif player1 == player2:
        print("It's a tie.")
    else:
        print("System broke.")


main()
