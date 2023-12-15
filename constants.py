# This module is made to parse the configuration file and to create the botchat reponds


import os
import yaml
import random
from datetime import datetime

SRC_PATH = os.path.dirname(__file__)


def load_yaml(filepath):  # A function to open the .yaml configuration files
    with open(filepath, "r") as f:
        return yaml.safe_load(f)


QUESTION_CONFIG_FILE = os.path.join(SRC_PATH, "QnA.yaml")  # Saving the configuration file path
QUESTIONS_CONFIGS = load_yaml(QUESTION_CONFIG_FILE)  # Load the configuration file
QUESTIONS = None  # A list for the prompted user chat / questions / responds
for q in QUESTIONS_CONFIGS['questions']:  # Filling the list with the user questions in the configuration files
    string = str(q.keys())
    splitted = string.split("'")[1]
    if QUESTIONS is None:
        QUESTIONS = [splitted]
    else:
        QUESTIONS.append(splitted)


def automaticAnswer(question):
    answer = "Hey, what can I do for you?"  # A default respond of teh chatbot
    index = 0
    if question is None:
        return answer  # If the user does not choose a prompted question of the dropdown, then return defult respond

    for qe in QUESTIONS_CONFIGS['questions']:
        dt = datetime.now()  # Saving the current time for the questions related to time
        string1 = str(qe.keys())  # Load the questions from the configuration files
        splitted1 = string1.split("'")[1]
        if splitted1 == question:
            randomNumber = random.randint(0, 1)  # Give a random number (either 0 or 1) to determine which version of
            # the answer will be displayed
            if randomNumber == 0:  # If the random number is 0, then display the first version of the answer
                if splitted1 == "What day is today?":  # For the question related to current day of the week
                    answer = QUESTIONS_CONFIGS['questions'][index][splitted1][0]['response_1'] + " " + dt.strftime('%A')
                elif splitted1 == "Could you please tell the time?":  # For the question related to the current time
                    answer = QUESTIONS_CONFIGS['questions'][index][splitted1][0]['response_1'] + " " + dt.strftime(
                        "%H:%M")
                elif splitted1 == "Can you tell the date?":  # For the question of the current date
                    answer = QUESTIONS_CONFIGS['questions'][index][splitted1][0]['response_1'] + " " + dt.strftime(
                        "%B %d, %Y")
                else:  # Other questions
                    answer = QUESTIONS_CONFIGS['questions'][index][splitted1][0]['response_1']
            else:  # If the random number is 1, then display the second version of the answer
                if qe == "What day is today?":  # For the question related to current day of the week
                    answer = QUESTIONS_CONFIGS['questions'][index][splitted1][1]['response_2'] + " " + dt.strftime('%A')
                elif splitted1 == "Could you please tell the time?":  # For the question related to the current time
                    answer = QUESTIONS_CONFIGS['questions'][index][splitted1][1]['response_2'] + " " + dt.strftime(
                        "%H:%M")
                elif splitted1 == "Can you tell the date?":  # For the question of the current date
                    answer = QUESTIONS_CONFIGS['questions'][index][splitted1][1]['response_2'] + " " + dt.strftime(
                        "%B %d, %Y")
                else:  # Other questions
                    answer = QUESTIONS_CONFIGS['questions'][index][splitted1][1]['response_2']
            break
        index = index + 1  # Iterate through the list of questions
    return answer
