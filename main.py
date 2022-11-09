import random

decks = []
card_front = []
card_back = []
front = []
back = []
def new_deck():
    name = input("Name the deck you want to create: ")
    decks.append(name)
    print("a deck has been made with the name:", name)
    card_front.append(front)
    card_back.append(back)


def add_card():
    frontCard = input("Enter the text on the front of the card: ")
    front.append(frontCard)
    backCard = input("Enter the text on the back of the card: ")
    back.append(backCard)
    print("a card has been added to the deck.")


flag = True

while flag:
    print("Create new deck (N) - View deck list (L) - Close/Exit (break)")
    inp = input()

    if inp == "break":
        flag = False
    elif inp == 'N':
        new_deck()
    elif inp == 'L':
        for i in range(0, len(decks)):
            print("{0}:".format(i + 1), decks[i])

        print("COMMANDS: edit, delete, back, view")
        command = input()

        while command != "edit" and command != "delete" and command != "back" and command != "view":
            command = input("Wrong input ")

        if command == "edit":
            target = input("select deck to edit: (number) ")
            target = int(target) - 1
            print(decks[target])
            print("Add new card (add), Delete card (delete)")
            command = input()
            if command == "add":
                add_card()
        elif command == "view":
            print("front", front)
            print("back", back)
