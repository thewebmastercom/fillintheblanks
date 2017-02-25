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

# Change this to take two arguments so can be reused to validate answers - TODO add guess limits

# two functions = 1. validation correct input, and limits 2. question & answer correct

def validate_input(userinput, validation):
    if userinput.lower() in validation:
        for e in validation:
            if userinput == e:
                return True
            else:
                return False
    else:
        return False

def choose_level():
    global quiz, answers
    user_level_choice_valid = ['easy', 'medium', 'hard']
    user_level_choice = raw_input("Please choose your difficulty level: ")
    print user_level_choice

    if validate_input(user_level_choice, user_level_choice_valid) == True:
        if user_level_choice == "easy":
            quiz = easy_quiz
            answers = easy_answers
        else:
            if user_level_choice == "medium":
                quiz = medium_quiz
                answers = medium_answers
            else:
                if user_level_choice == "hard":
                    quiz = hard_quiz
                    answers = hard_answers
    else:
        print "I am sorry but your choice was not a valid input"
        choose_level()

    return quiz, answers

choose_level()
print quiz
