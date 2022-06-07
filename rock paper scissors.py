import random

a = input("please enter start:")
while a != "Stop":
    word = random.choice(["Rock", "Paper", "Scissors"])

    a = input("Rock, Paper, Scissors? ").capitalize()
    try:
        assert a == "Rock" or a == "Paper" or a == "Scissors" or a == "Stop"
    except AssertionError:
        print("type rock or paper or scissors!!")

    if word == "Rock" and a == "Paper":
        print(f"PC = {word}, you won!")
    elif word == "Rock" and a == "Scissors":
        print(f"PC = {word}, you lost!")
    elif word == "Paper" and a == "Rock":
        print(f"PC = {word}, you lost!")
    elif word == "Paper" and a == "Scissors":
        print(f"PC = {word}, you won!")
    elif word == "Scissors" and a == "Rock":
        print(f"PC = {word}, you won!")
    elif word == "Scissors" and a == "Paper":
        print(f"PC = {word}, you lost!")
    elif word == a:
        print(f"PC ={word}, draw!")
