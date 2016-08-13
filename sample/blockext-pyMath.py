import math
from blockext import *

class Tutorial:
    def __init__(self):
        self.light = False
        self.mymath = 0
    def do_toggle_light(self, times):
        for i in range(times):
            self.light = not self.light
    def is_light_on(self):
        return self.light
    def set_mymath(self, myfname, p1): 
        print("Get pymath", myfname, p1)
        methodToCall = getattr(math, myfname)
        x = methodToCall(float(p1))
        self.mymath = x
        print("Result is ", x)
        
    def get_mymath(self): 
        return self.mymath

descriptor = Descriptor(
    name = "Tutorial Example",
    port = 5000,
    blocks = [
        Block('do_toggle_light', 'command', 'press light switch %n times',
            defaults=[1]),
        Block('is_light_on', 'predicate', 'light is on?'),
        Block('set_mymath', 'command', 'PyMath %s with %n'),
        Block('get_mymath', 'reporter', 'PyMath result')
    ],
    menus = dict(
        day = ["sqrt", "floor"],
        city = [25,25.5,26],
    ),
)

extension = Extension(Tutorial, descriptor)

if __name__ == '__main__':
    extension.run_forever(debug=True)
