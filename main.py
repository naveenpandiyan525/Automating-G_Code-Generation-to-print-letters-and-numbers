import CNC_Implementation as CI
from Global_Var import GlobalVariables as GV
import json

class main:

    def __init__(self):
        #Read LetterCooardinates Json File
        with open ("letterCoardinates.json","r") as file:
            self.__letterCoardinates = json.load(file)

    def Gcode_generation(self,userInputList, output_file):
        for letterOrderIndex, letter in enumerate(userInputList):
            try:
            #Check letter and number is present in the Json or not
             if letter in self.__letterCoardinates:
                #print(f"letter not found: {letter}")
                pass
            except Exception as e:
                print(e)    

            strokes = self.strokes(letter)

            CNCImplementation = CI.CNCImplementation(GV(), output_file)
            #calling the calculate_stroke_1 and calculate_stroke_2 abstract methods from CNCImplementation class based on the stroke index
            for strokeIndex, stroke in enumerate(strokes, start=1):
                try:
                    if strokeIndex == 1:
                         CNCImplementation.calculate_stroke_1(stroke,letterOrderIndex)
                    else:
                         CNCImplementation.calculate_stroke_2(stroke,letterOrderIndex)
                except Exception as e:
                    print("Error Occured",e)

    def strokes(self,letter):
        #Fetch the coordinates for the letter or number from the Json
        coordinates = self.__letterCoardinates[letter]
        if len(coordinates) == 2:
            strokes = coordinates
            return strokes
        else:
            strokes = (coordinates,)
            return strokes



#Getting UserInput
userInput = input("Enter your register number =")
UserInputForFileName = input("Enter the Output file name =") 
userInput = userInput.upper()
userInput = userInput.replace(" ", "")
userInputList = list(userInput)

try:
    main = main()

    with open(f"{UserInputForFileName}.txt", "w", encoding="utf-8") as output_file:
        output_file.write("G21\n")
        output_file.write("G90\n")
        main.Gcode_generation(userInputList, output_file)
        print("File Generation successfull")
except Exception as e:
    print("Error Occured :",e)