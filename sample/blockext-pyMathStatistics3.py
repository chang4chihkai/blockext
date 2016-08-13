import math
import statistics
from blockext import *

class Tutorial:
    def __init__(self):
        self.light = False
        self.mymath = 0
        self.mystatistics = 0
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
    def set_mystatistics(self, myfname, p1):
        print("Get pyStatistics", myfname, p1)
        methodToCall = getattr(statistics, myfname)
        p1list = p1.split(',')
        for i in range(len(p1list)):
            p1list[i] = float(p1list[i])
        x = methodToCall(p1list)
        self.mystatistics = x
        print("Result is ", x)
    def get_mymath(self): 
        return self.mymath
    def get_mystatistics(self):
        return self.mystatistics

descriptor = Descriptor(
    name = "Tutorial Example",
    port = 5000,
    blocks = [
        Block('do_toggle_light', 'command', 'press light switch %n times',
            defaults=[1]),
        Block('is_light_on', 'predicate', 'light is on?'),
        Block('set_mymath', 'command', 'PyMath %m.mathfun with %n'),
        Block('get_mymath', 'reporter', 'PyMath result'),
        Block('set_mystatistics', 'command', 'PyStatistics %m.statfun with %s'),
        Block('get_mystatistics', 'reporter', 'PyStatistics result')
    ],
    menus = dict(
        mathfun = ['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc'],
        statfun = ['mean', 'median', 'median_grouped', 'median_high', 'median_low', 'mode', 'pstdev', 'pvariance', 'stdev', 'variance'],
        builtin = ['abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'],
        city = [25,25.5,26],
    ),
)

extension = Extension(Tutorial, descriptor)

if __name__ == '__main__':
    extension.run_forever(debug=True)
