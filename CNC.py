letterCoardiinates = {
    'M': ((0, 0), (0, 7), (2, 3.5), (4, 7), (4, 0)),
    'E': (
        ((4, 7), (0, 7), (0, 0), (4, 0)),
        ((0, 3.5),(3.5, 3.5))
        ),
    'C': ((4, 7), (0, 7), (0, 0), (4, 0)),
    '0': ((0,0),(0,7),(4,7),(4,0),(0,0)),
    '1': (
        ((0.5,5.5),(2,7),(2,0)),
        ((0.5,0),(3.5,0),)
        ),
    '2': ((0,7),(4,7),(4,3.5),(0,3.5),(0,0),(4,0)),
    '3': (
          ((0,7),(4,7),(4,0),(0,0)),
          ((1,3.5),(4,3.5),)
          ),
    '4': (
        ((0,7),(0,3.5),(4,3.5)),
        ((4,7),(4,0),)
        ),
    '5': ((4,7),(0,7),(0,3.5),(4,3.5),(4,0),(0,0)),
    '6': ((4,7),(0,7),(0,0),(4,0),(4,3.5),(0,3.5)),
    '7': ((0,7),(4,7),(1.5,0)),
    '8': (
        ((0,0),(0,7),(4,7),(4,0),(0,0)),
        ((0,3.5),(4,3.5),)
     ),
    '9': ((4,0),(4,7),(0,7),(0,3.5),(4,3.5))
}



SAFE_Z = 5.000
APPROCH_Z = 0.500
CUT_Z = -0.300
FEED_XY = 30.000
FEED_Z = 10.000



userInput = input("Enter your register number = ")
userInput = userInput.upper()
userInput = userInput.replace(" ", "")
userInputList = list(userInput)
for letterOrderIndex, letter in enumerate(userInputList):
    if letter not in letterCoardiinates:
        print(f"Letter not found: {letter}")
        continue

    coordinates = letterCoardiinates[letter]
    if len(coordinates) == 2:
        strokes = coordinates
    else:
        strokes = (coordinates,)

    
    
    for strokeIndex, stroke in enumerate(strokes, start=1):
        #print(f"Stroke {strokeIndex}:")
        if strokeIndex == 1:
            for index, strokeValue in enumerate (stroke,start=1):
              u, v = strokeValue
              x = 10 + 1.5 * (u + 6 * letterOrderIndex)
              y = 9.75 + 1.5 * v
              emptyList = []
              
              if index == 1:
                emptyList.append(f"G00 X{x:.3f} Y{y:.3f}")
                emptyList.append(f"G00 Z{APPROCH_Z:.3f}")
                emptyList.append(f"G01 Z{CUT_Z:.3f} F{FEED_Z:.3f}")
                print(emptyList[0] + "\n" + emptyList[1] + "\n" + emptyList[2])
              elif index == 2:
                print(f"G01 X{x:.3f} Y{y:.3f} F{FEED_XY:.3f}")
              else:
                print(f"G01 X{x:.3f} Y{y:.3f}")
            print(f"G00 Z{SAFE_Z:.3f}")
        else:
            for index, strokeValue in enumerate (stroke,start=1):
                u, v = strokeValue
                x = 10 + 1.5 * (u + 6 * letterOrderIndex)
                y = 9.75 + 1.5 * v
                emptyList = []
                if index == 1:
                    emptyList.append(f"G00 X{x:.3f} Y{y:.3f}")
                    emptyList.append(f"G00 Z{APPROCH_Z:.3f}")
                    emptyList.append(f"G01 Z{CUT_Z:.3f} F{FEED_Z:.3f}")
                    print(emptyList[0] + "\n" + emptyList[1] + "\n" + emptyList[2])
                elif index == 2:
                    emptyList.append(f"G01 X{x:.3f} Y{y:.3f} F{FEED_XY:.3f}")
                    print(emptyList[0])
                else:
                    emptyList.append(f"G01 X{x:.3f} Y{y:.3f}")
                    print(emptyList[0])
            print(f"G00 Z{SAFE_Z:.3f}")