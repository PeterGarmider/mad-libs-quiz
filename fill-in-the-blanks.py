# IPND Stage 2 Final Project - Peter Garmider

# This quiz can be run infinitely once started as long as the user wants to continue taking the quizzes.

# Regular Expression python module
import re

# Allows the user to select the level of difficulty. Each level has its own answer key.
def level_select():
    easy_quiz = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
    adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
    don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
    tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
    easy_answers = ["function", "arguments", "true", "list"]

    medium_quiz = '''A red, yellow, or green fruit that grows on trees and starts with a is an ___1___.
     A long, yellow fruit that starts with b is called a ___2___. A type of melon that starts with c is a ___3___.
      A less commonly known fruit, that takes its name from a fictional, flying, scaled reptile, 
      starting with d is ___4___. A large fruit resembles an orange but starts with a g is a ___5___.
       A fruit which takes its name from a flightless bird from New Zealand, and starts with a k is a ___6___. '''
    medium_answers = ["apple", "banana", "cantaloupe", "dragonfruit", "grapefruit", "kiwi"]

    hard_quiz = '''The city of Saskatoon is on this continent: ___1___. 
    The Taishan Station is on this continent: ___2___.
    The city of Cusco is on this continent: ___3___. The city of Samarkand is on this continent: ___4___.
    The city of Bucharest is on this continent: ___5___. The city of Adelaide is on this continent: ___6___.
    The city of Pretoria is on this continent: ___7___. This dwarf-planet was once considered a planet: ___8___. '''
    hard_answers = ["North America", "Antarctica", "South America", "Asia", "Europe", "Australia", "Africa", "Pluto"]

    # Calling the function "collect_answers" and passing the list, depending on difficulty,
    # to ask for the user's input
    diff_select = ''
    while diff_select != "Easy" or "Medium" or "Hard":
        diff_select = input("Please choose your level of difficulty (Easy, Medium, Hard): ")
        if (diff_select) == "Easy":
            collect_answers(easy_quiz, easy_answers)
            return 1
        elif (diff_select) == "Medium":
            collect_answers(medium_quiz, medium_answers)
            return 1
        elif (diff_select) == "Hard":
            collect_answers(hard_quiz, hard_answers)
            return 1
        else:
            print("You did not enter a valid difficulty level, please try again.")

# Function to determine how many answers to ask the user for.
# (ie. if 4 is your highest blank number, it will ask for 4 answers from the user
def determine_num_blanks(sample):
    x = map(int, re.findall('\d+', sample))
    return max(x)

# Collects answers from the user and sends them to the "compare_answers" function
# to validate against the "answers" list. Then uses the "return_answer_string" function to return a string filled
# with the correct values
def collect_answers(quiz_string, answers):
    print(quiz_string, '\n')
    list_of_answers = []
    final_string = quiz_string
    incorrect_answer_counter = 0
    i = 0
    while i < determine_num_blanks(quiz_string):
        # While the counter doesn't reach the number of blanks in the sample string, ask the user for answers
        list_of_answers.append(input("\n Please fill in the word for the blank(s) labelled {}: ".format(i + 1)))

        if compare_answers(list_of_answers, answers, i) == 1:
            # Uses the "return_answer_string" function to get the resulting string, with blanks filled,
            # once the answers have been entered.
            final_string = return_answer_string(list_of_answers, i, final_string)
            print(final_string)
            i = i + 1
        elif compare_answers(list_of_answers, answers, i) == 0:
            # If the entered answer is incorrect, remove it from the list, and prompt the user to try again
            # up to three times consecutively, before breaking the loop
            list_of_answers.pop(i)
            print("\n Your answer for blank {} is incorrect, please try again.".format(i + 1))
            incorrect_answer_counter = incorrect_answer_counter + 1
            if incorrect_answer_counter == 3:
                print("\n", "Sorry, you have answered incorrectly 3 times. You lost the game.", "\n")
                break
    # Only prints the winning message if the loop has gone through all of the blanks
    if i == determine_num_blanks(quiz_string):
        print("\n", "Success, you have completed the quiz!", "\n")

# Compares the list of answers collected from the user to the pre-defined answers, and passes in a value "j",
# representing the number corresponding to the blank (ie. if we are answering for blank 1, j=0)
def compare_answers(list_of_answers, answers, j):
    if list_of_answers[j] == answers[j]:
        return 1
    else:
        return 0

# Function to take the sample string, turn it into a list, replace word(s) in the list (matching the blank number)
# with the correct answer. I want it to iterate through the list and check/replace the values.
def return_answer_string(list_of_answers, k, final_string):
    # Assign the value of the final_string, as a list, split on spaces, to "replacement_list"
    replacement_list = final_string.split(" ")
    for word in replacement_list:
        if "__" + str(k+1)+ "__" in word:
            # If the for loop detects the conditions that satisfy a blank, the if statement will assign
            # the appropriate index answer within "list_of_answers" to the blank
            replacement_list[replacement_list.index(word)] = list_of_answers[k]
            # Else set the word in the replacement_list to remain as it was
        else:
            replacement_list[replacement_list.index(word)] = word
    # return the joined list as a string, joining on spaces
    return " ".join(replacement_list)

# Code which initiates the quiz and controls whether the user wants to try again or quit.
quiz_start = ''
while quiz_start != "No" or quiz_start == "no" or quiz_start == "N" or quiz_start == "n":
    quiz_start = input("Would you like to take the quiz?: ")
    if quiz_start == "Yes" or quiz_start == "yes" or quiz_start == "Y" or quiz_start == "y":
        game_status = level_select()
        # If a quiz has been completed, we want to reset the value of quiz_start so the user can answer if they want
        # to try the quiz again, or quit.
        if game_status == 1:
            quiz_start = None
    else:
        print("Please come back another time.")


