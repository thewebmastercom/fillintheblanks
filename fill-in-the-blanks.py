easy_quiz = '''EASY - A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

easy_answers = ['easy', 'answer2', 'answer3', 'answer4']

medium_quiz = '''MEDIUM - A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

medium_answers = ['mediumanswer1', 'answer2', 'answer3', 'answer4']

hard_quiz = '''HARD - A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

hard_answers = ['hardanswer1', 'answer2', 'answer3', 'answer4']

def validate_input(userinput, validation, tries):
    index = 0
    while index < tries:
        this_input = raw_input(userinput)
        if this_input.lower() in validation:
            for e in validation:
                if this_input.lower() == e:
                    return this_input.lower()
        else:
            index += 1
            print "\nI am sorry but your choice was not a valid input."
            print "You have used " + str(index) + " of " + str(tries) + " tries."
    print "\nYou have had too many tries. You are an idiot. Terminating.\n"
    quit()

def choose_level():
    user_level_choice_valid = ['easy', 'medium', 'hard']
    user_level_choice = "Please choose your difficulty level: "
    quiz_chosen = validate_input(user_level_choice, user_level_choice_valid, 5)
    if quiz_chosen == "easy":
        quiz_chosen = easy_quiz
        answers = easy_answers
    elif quiz_chosen == "medium":
        quiz_chosen = medium_quiz
        answers = medium_answers
    else:
        quiz_chosen = hard_quiz
        answers = hard_answers
    return (quiz_chosen, answers)

def choose_number_of_tries():
    user_level_choice_valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    user_level_choice = "Please choose the number of tries per question between 1 and 10: "
    number_of_tries = validate_input(user_level_choice, user_level_choice_valid, 5)
    return number_of_tries

def quiz():
    print "\nWelcome to the fill in the blanks quiz.\n"
    print "Levels available: Easy, Medium, Hard.\n"
    quiz_chosen, answers = choose_level()
    tries = int(choose_number_of_tries())
    print "\n" + quiz_chosen
    question = 1
    while question < 5:
        blank = "___" + str(question) + "___"
        user_level_choice_valid = [answers[question - 1]]
        user_level_choice = "\nPlease fill in the blank for " + blank + ": "
        chosen_answer = validate_input(user_level_choice, user_level_choice_valid, tries)
        quiz_chosen = quiz_chosen.replace(str(blank), str(chosen_answer))
        print "\n" + quiz_chosen
        question += 1
    print "\nCongratulations!!\n"
    play_again = validate_input('Play Again? Choose "yes" or "no": ', ['yes', 'no'], 5)
    if play_again == "yes":
        quiz()
    else:
        print "Thanks for playing. Bye!"
        quit()
quiz()
