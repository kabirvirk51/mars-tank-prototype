from pyPS4Controller.controller import Controller
from roboclaw_3 import Roboclaw
import sys

if __name__ == "__main__":
    
    # Motor controller configuration
    address = 0x80  # Hexadecimal address for a specific Roboclaw
    roboclaw = Roboclaw("/dev/ttyS0", 38400)  # Specify the source file and baud rate
    roboclaw.Open() 

class MyController(Controller):
    
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
        roboclaw.ForwardM1(address, 100)
        roboclaw.ForwardM2(address, 100)
        print("Forward")
        
    def on_down_arrow_press(self):
        roboclaw.BackwardM1(address, 100)
        roboclaw.BackwardM2(address, 100)
        print("Backward")
        
    def on_left_arrow_press(self):
        roboclaw.ForwardM1(address, 100)
        roboclaw.BackwardM2(address, 70)
        print("Left Turn")
        
    def on_right_arrow_press(self):
        roboclaw.BackwardM1(address, 70)
        roboclaw.ForwardM2(address, 100)
        print("Right Turn")
        
    def on_left_right_arrow_release(self):
        roboclaw.BackwardM1(address, 0)
        roboclaw.BackwardM2(address, 0)
        print("STOP")
        
    def on_up_down_arrow_release(self):
        roboclaw.BackwardM1(address, 0)
        roboclaw.BackwardM2(address, 0)
        print("STOP")
        
    def on_square_press(self):
        sys.exit()

# Create a controller instance and start listening for input
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# You can start listening before the controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
