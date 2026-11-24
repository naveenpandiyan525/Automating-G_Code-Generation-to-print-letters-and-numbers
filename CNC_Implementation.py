import CNC_Interface

class CNCImplementation(CNC_Interface.CNCInterface):

    def __init__(self,GV):
        # Initialize any necessary attributes or variables here
        self.GV = GV

    def calculate_stroke_1(self, stroke, letterOrderIndex):
         # Implement the logic for calculating stroke 1
        try: 
            for index, strokeValue in enumerate (stroke,start=1):
                u, v = strokeValue
                x = 10 + 1.5 * (u + 6 * letterOrderIndex)
                y = 9.75 + 1.5 * v
                emptyList = []
                      
                if index == 1:
                    emptyList.append(f"G00 X{x:.3f} Y{y:.3f}")
                    emptyList.append(f"G00 Z{self.GV.APPROCH_Z:.3f}")
                    emptyList.append(f"G01 Z{self.GV.CUT_Z:.3f} F{self.GV.FEED_Z:.3f}")
                    print(emptyList[0] + "\n" + emptyList[1] + "\n" + emptyList[2])
                elif index == 2:
                    emptyList.append(f"G01 X{x:.3f} Y{y:.3f} F{self.GV.FEED_XY:.3f}")
                    print(emptyList[0])
                else:
                    emptyList.append(f"G01 X{x:.3f} Y{y:.3f}")
                    print(emptyList[0])
            emptyList.append(f"G00 Z{self.GV.SAFE_Z:.3f}")
            print(emptyList[1])

            return None
        
        except Exception as e:
            return e

    
    def calculate_stroke_2(self, stroke, letterOrderIndex):

        # Implement the logic for calculating stroke 2
        try:
            for index, strokeValue in enumerate (stroke,start=1):
                u, v = strokeValue
                x = 10 + 1.5 * (u + 6 * letterOrderIndex)
                y = 9.75 + 1.5 * v
                emptyList = []
                if index == 1:
                    emptyList.append(f"G00 X{x:.3f} Y{y:.3f}")
                    emptyList.append(f"G00 Z{self.GV.APPROCH_Z:.3f}")
                    emptyList.append(f"G01 Z{self.GV.CUT_Z:.3f} F{self.GV.FEED_Z:.3f}")
                    print(emptyList[0] + "\n" + emptyList[1] + "\n" + emptyList[2])
                elif index == 2:
                    emptyList.append(f"G01 X{x:.3f} Y{y:.3f} F{self.GV.FEED_XY:.3f}")
                    print(emptyList[0])
                else:
                    emptyList.append(f"G01 X{x:.3f} Y{y:.3f}")
                    print(emptyList[0])
            emptyList.append(f"G00 Z{self.GV.SAFE_Z:.3f}")
            print(emptyList[1])

            return None
        
        except Exception as e:
            return e