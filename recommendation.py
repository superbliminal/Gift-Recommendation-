# Implementing an autocomplete that, based on a user’s input,
# returns a list of possible categories based on the beginning of a word.
# You should use the data created in the last step to create the autocomplete.
# It is up to you how to properly store and retrieve the data.

from restaurantData import types


def autocomplete():
    intro = input("\n\nWhat kind of food suits your fancy tonight? Type the first letter of the type of food you would like to eat.\n")
    foods = []

    for type in types:
        if type[0] == intro:
            foods.append(type)
        # else:
        #     return "There are no foods that start with that letter. Please choose again"

    print("\nHere are the types of foods you can choose from:\n\n" + '\n'.join(foods))
    refine = input("\nWhich type of food would you like to see options for?\n\n")
    for food in foods:
        if refine == food:
            return "You selected " + food
        else:
            return "That is not an option. Please choose again."









#Retrieving and displaying all of the data related to the category
# selected by the user. It is up to you how to properly store and
# retrieve the data.

print(autocomplete())
