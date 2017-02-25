easy_quiz = '''EASY - A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

easy_answers = ['easyanswer1', 'answer2', 'answer3', 'answer4']

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

print "Welcome to the fill in the blanks quiz"
print "Levels available: Easy, Medium, Hard"

def validate_user_level_choice():
    user_level_choice_valid = ['easy', 'medium', 'hard']
    user_level_choice = raw_input("Please choose your difficulty level: ")
    if user_level_choice.lower() in user_level_choice_valid:
        choose_level(user_level_choice)
    else:
        print "Sorry this answer is not correct"
        validate_user_level_choice()

def choose_level(level):
    global quiz, answers
    if level == "easy":
        quiz = easy_quiz
        answers = easy_answers
    else:
        if level == "medium":
            quiz = medium_quiz
            answers = medium_answers
        else:
            if level == "hard":
                quiz = hard_quiz
                answers = hard_answers
    return quiz, answers

validate_user_level_choice()
print quiz
print answers
