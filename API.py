print ("right now __name__ is " + __name__)


#提供了像是函式（Function）、模組（Module）、類別（Class）與套件等支援
def max(a, b):
    return a if a > b else b

print(max(3,5))

min = lambda a,b: a if a < b else b
print(min(3,5))


import xmath
print('# import xmath')
print(xmath.pi)
print(xmath.max(10, 5))
print(xmath.sum(1, 2, 3, 4, 5))

print('# import xmath as math')
import xmath as math # 為 xmath 模組取別名為 math
print(math.e)

print('# from xmath import min')
from xmath import min  # 將 min 複製至目前模組，不建議 from modu import *，易造>成名稱衝突
print(min(10, 5))
