import CNC_Interface

class CNCImplementation(CNC_Interface.CNCInterface):

    def __init__(self, GV, output_file):
        self.GV = GV
        self.output_file = output_file

    def calculate_stroke_1(self, stroke, letterOrderIndex):
        # Implement the logic for calculating stroke 1
        try: 
            for index, strokeValue in enumerate (stroke,start=1):
                u, v = strokeValue
                x = 10 + 1.5 * (u + 6 * letterOrderIndex)
                y = 9.75 + 1.5 * v
                      
                if index == 1:
                    self.print_gcode(
                        f"G00 X{x:.3f} Y{y:.3f}",
                        f"G00 Z{self.GV.APPROCH_Z:.3f}",
                        f"G01 Z{self.GV.CUT_Z:.3f} F{self.GV.FEED_Z:.3f}",
                    )
                elif index == 2:
                    self.print_gcode(f"G01 X{x:.3f} Y{y:.3f} F{self.GV.FEED_XY:.3f}")
                else:
                    self.print_gcode(f"G01 X{x:.3f} Y{y:.3f}")
            self.print_gcode(f"G00 Z{self.GV.SAFE_Z:.3f}")

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
                if index == 1:
                    self.print_gcode(
                        f"G00 X{x:.3f} Y{y:.3f}",
                        f"G00 Z{self.GV.APPROCH_Z:.3f}",
                        f"G01 Z{self.GV.CUT_Z:.3f} F{self.GV.FEED_Z:.3f}",
                    )
                elif index == 2:
                    self.print_gcode(f"G01 X{x:.3f} Y{y:.3f} F{self.GV.FEED_XY:.3f}")
                else:
                    self.print_gcode(f"G01 X{x:.3f} Y{y:.3f}")
            self.print_gcode(f"G00 Z{self.GV.SAFE_Z:.3f}")

            return None
        
        except Exception as e:
            return e


    def print_gcode(self, *lines):
        for line in lines:
            #print(line)
            if self.output_file is not None:
                self.output_file.write(line + "\n")