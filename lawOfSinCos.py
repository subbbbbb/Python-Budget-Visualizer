import math


def main():
    print("Welcome to the law of sines/cosin/pythagorean calculator!")
    choice = input(
        "Do you want to solve for angle measures, lengths, law of sines, or law of cosines?")
    if ("angle" in choice):
        getAngles() # this will be used for using pythagorean theorem and solving for angle measures
    elif ("length" in choice):
        getLengths() # this will be used for using pythagorean theorem and solving for side lengths
    elif ("sin" in choice):
        lawOfSin() # this will be used for using law of sines
    elif ("cos" in choice):
        lawOfCos() # this will be used for law of cosines
    else:
        print("Enter in a correct option:")
        main() # this makes the user always enter in a correct input or else it redos the main method

