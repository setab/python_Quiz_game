import requests
import json
import random


def save_info():
    respons = requests.get("https://opentdb.com/api.php?amount=1&category=18&type=multiple")
    quiz = respons.json()

    res = str(quiz)
    print(res)
    print(type(res))
    with open('info.txt', 'a') as file:
        file.write("\n")
        file.write(res)
        # print(type(res))
    return quiz


def question():
    # print(type(quiz))
    # print(type(quiz['results']))
    quiz = save_info()
    for i in quiz['results']:
        print("Question: ", i['question'], "\n")
        a = i['correct_answer']

        b = i['incorrect_answers']
        b.append(a)
        random.shuffle(b)
        for items in b:
            print(items)
        print("\n")
        ans = input("\nanswer :").lower()
        correct_answer = i['correct_answer'].lower()
        if ans == correct_answer:
            print("\ngood job!  right answer\n")
        else:
            print("naaahh wrong\n")
            print(i['correct_answer'], "\n")


def play_again():
    responses = input("Do want to try again ?")
    responses = responses.lower()
    if responses == "yes":
        return True
    else:
        return False


question()

while play_again():

    question()
print("\nBYee")
