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
def getAngles():
    numOfAngles = int(input("How many angle measures do you know already?"))
    if (numOfAngles == 1):
        print("Try using the law of cosines or law of sines calculators")
        main() # add a function here that would transport the user straight ot the law of sines or cosines calculator
    if (numOfAngles == 2):
        angleA = float(input("Enter in the angle measure for the first side"))
        angleB = float(input("Enter in the angle measure for the second side"))
        angleC = 180 - (angleA + angleB)
        print("The angle measure of the unknown angle is " +
              str(angleC) + " degrees.")
def lawOfSin():
    option = input(
        "For this calculator to work you must have a) two sides and an included angle |OR| b) two angles and an included side |OR| c) n/a")
    if (option == "a"):
        angleA = float(input("Enter the degree measure for angle A"))
        sideA = float(input("Enter the side measure for side A"))
        extra = float(input("Enter the measure for the extra angle or side"))
        angleA = math.radians(angleA)
        answer = (math.degrees(math.asin(math.sin(angleA) / sideA * extra)))
        print("The measure of the angle is " + str(answer) + "degrees")
    if(option == "b"):
        angleA = float(input("Enter the degree measure for angle A"))
        sideA = float(input("Enter the side measure for side A"))
        extra = float(input("Enter the measure for the extra angle or side"))
        angleA = math.radians(angleA)
        answer = (math.sin(math.radians(extra)) * sideA) / math.sin(angleA)
        print("The measure of the side is " + str(answer) + " units")
    elif (option == "c"):
        print("Try the law of cosines calculator")
        lawOfCos()
    else:
        print("Enter a, b, or c")
        lawOfSin()

def lawOfCos():
    option = input(
        "For this calculator to work you must have a) two sides and one non-included angle |OR| b) three sides")
    if option == "a":
        angleA = float(input("Enter the degree measure for angle A"))
        sideB = float(input("Enter the side measure for side B"))
        sideC = float(input("Enter the side measure for side C"))
        x = math.sqrt(sideB ** 2 + sideC ** 2 - 2 * sideB *
                      sideC * math.cos(math.radians(angleA)))
        measureA = math.sqrt(sideB ** 2 + sideC **
                                    2 - 2 * sideB * sideC * math.cos(math.radians(angleA)))
        degB = math.degrees(math.acos((sideB ** 2 - x ** 2 - sideC ** 2) / (-2 * x * sideC)))
        degC = 180 - angleA - (math.degrees(math.acos((sideB ** 2 - x ** 2 - sideC ** 2) / (-2 * x * sideC))))
        print("The measure of side A is: " + str(measureA))
        print("The measure of angle B is: " + str(degB))
        print("The measure of angle C is: " + str(degC))
    elif option == "b":
            sideA = float(input("Enter the side measure for side A"))
            sideB = float(input("Enter the side measure for side B"))
            sideC = float(input("Enter the side measure for side C"))
            measure1 = math.degrees(math.acos((sideA **
                                            2 - sideB ** 2 - sideC ** 2) / (
                                                    -2 * sideB * sideC)))
            measure2 = math.degrees(math.acos((sideB **
                                            2 - sideA ** 2 - sideC ** 2)))
            measure3 = (180 - (math.degrees(math.acos((sideA ** 2 - sideB ** 2 - sideC ** 2) /
                                                    (-2 * sideB * sideC)))) - (math.degrees(
                math.acos((sideB ** 2 - sideA ** 2 - sideC ** 2) / (-2 * sideA * sideC)))))
            print("The measure of angle A is: " + str(measure1))
            print("The measure of angle B is: " + str(measure2))
            print("The measure of angle C is: " + str(measure3))
    else:
        print("Enter a, b, or c")
        lawOfCos()






