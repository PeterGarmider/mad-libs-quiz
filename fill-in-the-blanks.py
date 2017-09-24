# IPND Stage 2 Final Project - Peter Garmider

# This quiz can be run infinitely once started as long as the user wants to continue taking the quizzes.

# Regular Expression python module
import re

#global variable to ensure no more than 3 incorrect answers can be used
max_incorrect = 3

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


def level_select():
    """
    Allows the user to select the level of difficulty. Each level has its own answer key. Initialized by quiz_start.
    Takes no input. Returns True/False for the game_status variable, letting the program know if the game is run.
    Calls the function "collect_answers" and passing the list, depending on difficulty,
    to ask for the user's input
    """
    diff_select = ''
    while diff_select not in ["easy", "medium", "hard"]:
        diff_select = input("Please choose your level of difficulty (Easy, Medium, Hard): ")
        if (diff_select.lower()) == "easy":
            collect_answers(easy_quiz, easy_answers)
            return True
        elif (diff_select.lower()) == "medium":
            collect_answers(medium_quiz, medium_answers)
            return True
        elif (diff_select.lower()) == "hard":
            collect_answers(hard_quiz, hard_answers)
            return True
        else:
            print("You did not enter a valid difficulty level, please try again.")

def determine_num_blanks(quiz_string_sample):
    """
    Function to determine how many answers to ask the user for.
    (ie. if 4 is your highest blank number, it will ask for 4 answers from the user)
    Takes the quiz string as the input, and returns the maximum number of blanks in that string
    """
    blanks_in_string = map(int, re.findall('\d+', quiz_string_sample))
    return max(blanks_in_string)


def collect_answers(quiz_string, answers):
    """
    Takes input list_of_answers from the user and sends them to the "compare_answers" function
    to validate against the "answers" list input. Then uses the "return_answer_string" function to return a string filled
    with the correct values
    """
    print(quiz_string, '\n')
    list_of_answers, final_string, incorrect_answer_counter, index = [], quiz_string, 0, 0
    while index < determine_num_blanks(quiz_string):
        list_of_answers.append(input("\n Please fill in the word for the blank(s) labelled {}: ".format(index + 1)).lower())
        # While the counter doesn't reach the number of blanks in the sample string, ask the user for
        if compare_answers(list_of_answers, answers, index) == True:
            # Uses the "return_answer_string" function to get the resulting string, with blanks filled,
            # once the answers have been entered.
            final_string = return_answer_string(list_of_answers, index, final_string)
            print(final_string)
            index = index + 1
        elif compare_answers(list_of_answers, answers, index) == False:
            # If the entered answer is incorrect, remove it from the list, and prompt the user to try again
            # up to three times consecutively, before breaking the loop
            list_of_answers.pop(index)
            incorrect_answer_counter = incorrect_answer_counter + 1
            if incorrect_answer(index, incorrect_answer_counter) == False:
                break
    # Only prints the winning message if the loop has gone through all of the blanks
    print_winning_message(quiz_string, index)

def incorrect_answer(index, incorrect_answer_counter):
    '''Input: The index of the answer and the incorrect answer counter value.
    Checks to see if the user has exceeded the maximum allowable incorrect answers.
    Output: False if you have exceeded the allowable number, True otherwise. This ties into breaking the while loop
    for the collect_answers function'''
    if incorrect_answer_counter < max_incorrect:
        print("\n Your answer for blank {} is incorrect, please try again.".format(index + 1))
        return True
    else:
        print("\n", "Sorry, you have answered incorrectly 3 times. You lost the game.", "\n")
        return False

def print_winning_message(quiz_string, index):
    '''This function takes input: quiz_string and index. Checks to see if the index value is equal to the number
    of blanks within the quiz. If so, it will then output a winning message.'''
    if index == determine_num_blanks(quiz_string):
        print("\n", "Success, you have completed the quiz!", "\n")

def compare_answers(list_of_answers, answers, index):
    '''
    Compares the list of answers collected from the user to the pre-defined answers, and passes in a value "index",
    representing the number corresponding to the blank (ie. if we are answering for blank 1, index=0).
    Returns True or False depending if the values match, which is used by the collect_answers function to output
    the correct answer, or an error message to the user
    '''
    if list_of_answers[index].lower() == answers[index].lower():
        return True
    else:
        return False


def return_answer_string(list_of_answers, index, final_string):
    '''
    Function to take the quiz string, turn it into a list, replace word(s) in the list (matching the blank number)
    with the correct answer. The for loop will iterate through the list and check/replace the values.
    The re-joined list (as a string) is returned
    '''
    # Assign the value of the final_string, as a list, split on spaces, to "replacement_list"
    replacement_list = final_string.split(" ")
    for word in replacement_list:
        if "__" + str(index+1)+ "__" in word:
            # If the for loop detects the conditions that satisfy a blank, the if statement will assign
            # the appropriate index answer within "list_of_answers" to the blank
            replacement_list[replacement_list.index(word)] = list_of_answers[index]
            # Else set the word in the replacement_list to remain as it was
        else:
            replacement_list[replacement_list.index(word)] = word
    # return the joined list as a string, joining on spaces
    return " ".join(replacement_list)

def initiate_game():
    '''This function beings the quiz and asks the user if they would like to take a quiz. Depending on their response
    the quiz will either commence, or quit'''
    quiz_start = ''
    while quiz_start != "no" or quiz_start != "n":
        quiz_start = input("Would you like to take the quiz?: ").lower()
        if quiz_start == "yes" or quiz_start == "y":
            game_status = level_select()
        # If a quiz has been completed, we want to reset the value of quiz_start so the user can answer if they want
        # to try the quiz again, or quit.
            if game_status == True:
                quiz_start = None
        else:
            print("Please come back another time.")
            if quiz_start == "no" or quiz_start == "n":
                break

initiate_game()