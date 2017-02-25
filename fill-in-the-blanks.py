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

print "Welcome to the fill in the blanks quiz"
print "Levels available: Easy, Medium, Hard"

# Change this to take two arguments so can be reused to validate answers - TODO add guess limits

# two functions = 1. validation correct input, and limits 2. question & answer correct

def validate_input(userinput, validation, tries):
    index = 0
    while index < tries:
        this_input = raw_input(userinput)
        if this_input.lower() in validation:
            for e in validation:
                if this_input.lower() == e:
                    print this_input.lower()
                    return this_input.lower()
        else:
            print "I am sorry but your choice was not a valid input."
            index += 1
            print "You have used " + str(index) + " of 5 tries."
    failure_message = "You have had too many tries. You are an idiot. Terminating."
    print failure_message
    return failure_message

def choose_level():
    user_level_choice_valid = ['easy', 'medium', 'hard']
    user_level_choice = "Please choose your difficulty level: "
    quiz_chozen = validate_input(user_level_choice, user_level_choice_valid, 5)
    if quiz_chozen == "easy":
        quiz_chozen = easy_quiz
        answers = easy_answers
    else:
        if quiz_chozen == "medium":
            quiz_chozen = medium_quiz
            answers = medium_answers
        else:
            if quiz_chozen == "hard":
                quiz_chozen = hard_quiz
                answers = hard_answers
            else:
                quit()
    return [quiz_chozen, answers]
choose_level_results = choose_level()
quiz_chozen = choose_level_results[0]
answers = choose_level_results[1]

def quiz():
    question = 1
    updated = quiz_chozen
    while question < 5:
        blank = "___" + str(question) + "___"
        user_level_choice_valid = [answers[question - 1]]
        user_level_choice = "Please fill in the blank for " + blank + ": "
        chosen_answer = validate_input(user_level_choice, user_level_choice_valid, 5)
        updated = updated.replace(blank, chosen_answer)
        print updated
        question += 1
    return updated
quiz()
print "Congratulations!!"
