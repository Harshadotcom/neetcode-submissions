import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(*args):
        if len(args) == 2:
            return round(math.pi * (args[1] * args[1]), 2)
        else:
            return args[1] * args[2]
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
