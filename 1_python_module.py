import math
import inspect

print("square root of 16", math.sqrt(16))

dec_number = 1.5
print('round up number: ', math.ceil(dec_number))
print('round down number: ', math.floor(dec_number))
print('original number: ', dec_number)

# print(dir(math))

print(inspect.getfile(math))
