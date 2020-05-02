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

def getLengths():
    print("Keep in mind, this code only works for right triangles")
    typeOfTriangle = input(
        "Do you want to solve for the hypotenuse or a leg of the triangle?")
    if (typeOfTriangle == "hypotenuse"):
        sideA = float(input("Enter in the length for the first side"))
        sideB = float(input("Enter in the length for the second side"))
        sideC = math.sqrt(math.pow(sideA, 2) + math.pow(sideB, 2))
        print("Your hypotenuse is " + str(sideC) + " units.")
    if (typeOfTriangle == "leg"):
            hypotenuse = float(input("Enter in the length of the hypotenuse"))
            leg2 = float(input("Enter in the length of the leg that you know of"))
            leg1 = math.sqrt(math.pow(hypotenuse, 2) - math.pow(leg2, 2))
            print("The length of your leg is " + str(leg1) + " units.")

