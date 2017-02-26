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
            print "I am sorry but your choice was not a valid input."
            print "You have used " + str(index) + " of 5 tries."
    print "You have had too many tries. You are an idiot. Terminating."

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
    elif quiz_chosen == "hard":
        quiz_chosen = hard_quiz
        answers = hard_answers
    else:
        quit()
    return (quiz_chosen, answers)

def quiz():
    print "Welcome to the fill in the blanks quiz"
    print "Levels available: Easy, Medium, Hard"
    quiz_chosen, answers = choose_level()
    print quiz_chosen
    question = 1
    while question < 5:
        blank = "___" + str(question) + "___"
        user_level_choice_valid = [answers[question - 1]]
        user_level_choice = "Please fill in the blank for " + blank + ": "
        chosen_answer = validate_input(user_level_choice, user_level_choice_valid, 5)
        quiz_chosen = quiz_chosen.replace(blank, chosen_answer)
        print quiz_chosen
        question += 1
    print "Congratulations!!"
    play_again = validate_input('Play Again? Choose "yes" or "no": ', ['yes', 'no'], 5)
    if play_again == "yes":
        quiz()
    else:
        print "Thanks for playing. Bye!"
        quit()
quiz()
