import math
def print_love(scale_factor):
   for y in range(scale_factor * 2, -scale_factor * 2, -1):
       row = ''
       for x in range(-scale_factor * 2, scale_factor * 2, 1):
           equation = ((x * 0.05)**2 + (y * 0.1)**2 - 1)**3 - (x * 0.05)**2 * (y * 0.1)**3
           if equation > 0 or math.pow(equation, 3) > 0:
               row += '  +'
           else:
               row += "+"
       print(row)
print_love(40)