easy_quiz = '''The club isn't the best place to find a lover\n
So the bar is where I go\n
Me and my friends at the ___1___ doing shots\n
Drinking fast and then we ___2___ slow\n
Come over and start up a ___3___ with just me\n
And trust me I'll give it a chance now\n
Take my hand, stop, put Van the Man on the jukebox\n
And then we start to ___4___, and now I'm singing like\n
"Shape of You, by Ed Sheeran"\n'''

easy_answers = ['table', 'talk', 'conversation', 'dance']

medium_quiz = '''
I wanna be the very ___1___\n
Like no one ever was\n
To catch ___5___ is my real ___2___\n
To ___3___ ___5___ is my cause\n
\n
I will ___4___ across the land\n
Searching far and wide\n
Each Pokemon to understand\n
The ___6___ that's inside\n
"Pokemon Theme, by Pokemon" X\n'''

medium_answers = ['best', 'test', 'train', 'travel', 'them', 'power']

hard_quiz = '''

I heard that ___1___ settled down\n
That ___2___ found a girl and ___1___ married now\n
I heard that your dreams came true\n
Guess she gave ___2___ things I didn't give to ___2___\n
\n
Old friend, why are ___2___ so shy?\n
Ain't like ___2___ to hold back or hide from the light\n
\n
I hate to turn up out of the blue, uninvited\n
But I ___4___ stay away, I couldn't fight it\n
I had hoped ___3___ see my face and that y___3___ be reminded\n
That for me, it isn't over\n
"Someone Like You, by Adele"\n'''

hard_answers = ["you're", 'you', "you'd", "couldn't"]

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

    print "\nCan you fill in the blanks in these song lyrics?.\n"
    print "Levels available: Easy, Medium, Hard.\n"
    quiz, answers = choose_level()
    tries = int(choose_number_of_tries())
    print "\n" + quiz
    question = 1
    while question < len(answers) + 1:
        blank = "___" + str(question) + "___"
        user_level_choice_valid = [answers[question - 1]]
        user_level_choice = "\nPlease fill in the missing song lyrics for " + blank + ": "
        chosen_answer = validate_input(user_level_choice, user_level_choice_valid, tries)
        quiz = quiz.replace(str(blank), str(chosen_answer))
        print "\n" + quiz
        question += 1
    print "\nCongratulations!!\n"
    play_again()

quiz()
