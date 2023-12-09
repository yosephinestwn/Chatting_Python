import os
import yaml
import random

SRC_PATH = os.path.dirname(__file__)


def load_yaml(filepath):
    with open(filepath, "r") as f:
        return yaml.safe_load(f)


QUESTION_CONFIG_FILE = os.path.join(SRC_PATH, "QnA.yaml")
QUESTIONS_CONFIGS = load_yaml(QUESTION_CONFIG_FILE)
QUESTIONS = None
for q in QUESTIONS_CONFIGS['questions']:
    string = str(q.keys())
    splitted = string.split("'")[1]
    if QUESTIONS is None:
        QUESTIONS = [splitted]
    else:
        QUESTIONS.append(splitted)


def automaticAnswer(question):
    answer = "Hey, what can I do for you?"
    index = 0
    if question is None:
        return answer

    for qe in QUESTIONS_CONFIGS['questions']:
        string1 = str(qe.keys())
        splitted1 = string1.split("'")[1]
        if splitted1 == question:
            randomNumber = random.randint(0, 1)
            if randomNumber == 0:
                answer = QUESTIONS_CONFIGS['questions'][index][splitted1][0]['response_1']
            else:
                answer = QUESTIONS_CONFIGS['questions'][index][splitted1][1]['response_2']
        index = index + 1
    return answer
