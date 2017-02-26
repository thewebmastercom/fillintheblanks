easy_quiz = '''EASY - A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

easy_answers = ['easy', 'easy', 'easy', 'easy']

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

default_tries = 5 # This sets the number of user input tries by default i.e. for choosing level, or playing again.

def validate_input(userinput, validation, tries):

# This function takes in 3 inputs, the user input, a list of valid user inputs,
# and the number of attempts the user can take in trying to add a valid input.
# This function is used throughout, from verifying user level choice, to validating
# quiz questions, or play again choice.
# It returns the number of tries, and total number of allowed tries. If user exceeds
# the number of allowed tries the quiz ends, and the user can decide whether to
# play again.
# This validation can work on lower and upper case, as if converts everything to
# lower case before validation.

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
    play_again()

def choose_level():

# This function allows the user to choose the level of quiz, and returns the
# appropriate quiz and answers to be used in the main quiz function.

    user_level_choice_valid = ['easy', 'medium', 'hard']
    user_level_choice = "Please choose your difficulty level: "
    quiz_chosen = validate_input(user_level_choice, user_level_choice_valid, default_tries)
    if quiz_chosen == "easy":
        quiz = easy_quiz
        answers = easy_answers
    elif quiz_chosen == "medium":
        quiz = medium_quiz
        answers = medium_answers
    else:
        quiz = hard_quiz
        answers = hard_answers
    return (quiz, answers)

def choose_number_of_tries():

# This function enables the user to set the number of tries for each quiz
# question. It is validated by the validate_input funtion, and returns the result.

    user_level_choice_valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    user_level_choice = "Please choose the number of tries per question between 1 and 10: "
    number_of_tries = validate_input(user_level_choice, user_level_choice_valid, default_tries)
    return number_of_tries

def play_again():

# This function asks if the user wishes to play the quiz again. If yes, it
# restarts the quiz. If not the program ends.

    play_again = validate_input('Play Again? Choose "yes" or "no": ', ['yes', 'no'], default_tries)
    if play_again == "yes":
        quiz()
    else:
        print "\nThanks for playing. Bye!\n"
        quit()

def quiz():

# This function plays the quiz, and calls all the other functions. First
# the user is asked to choose a level, then number of tries with their respective
# functions. Then it prints the chosen quiz, and loops throug the questions,
# validating each answer via the validate_input function.
# Finally, it calls the play_again function to see if user wants to play again.

    print "\nWelcome to the fill in the blanks quiz.\n"
    print "Levels available: Easy, Medium, Hard.\n"
    quiz, answers = choose_level()
    tries = int(choose_number_of_tries())
    print "\n" + quiz
    question = 1
    while question < len(answers) + 1:
        blank = "___" + str(question) + "___"
        user_level_choice_valid = [answers[question - 1]]
        user_level_choice = "\nPlease fill in the blank for " + blank + ": "
        chosen_answer = validate_input(user_level_choice, user_level_choice_valid, tries)
        quiz = quiz.replace(str(blank), str(chosen_answer))
        print "\n" + quiz
        question += 1
    print "\nCongratulations!!\n"
    play_again()
quiz()
