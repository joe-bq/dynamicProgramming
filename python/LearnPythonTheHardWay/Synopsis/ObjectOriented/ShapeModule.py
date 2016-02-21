'''
Created on 2012-10-25

@author: Administrator
'''

import Synopsis.ObjectOriented.Shape as Shape

if __name__ == '__main__':
    c1 = Shape.Circle()
    c2 = Shape.Circle(5, 15, 20)
    
    print(c1)
    print(c2)
    print(c2.area())
    c2.move(5, 6)
    print(c2)