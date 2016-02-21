'''
Created on 2012-11-17

@author: Administrator
file: AssertDemo.py 
descripition: AssertDemo.py will demonstrate the use of the assert in python, assertion is one of the following.
'''

def demo_assert():
    x = (1, 2, 3)
    assert len(x) < 5, "the length of the list should be less than 3"

def demo_assert_failed():
    x = (1, 2, 3)
    assert len(x) > 5, "the assertion should failed!"


if __name__ == '__main__':
    demo_assert()
    try:
        demo_assert_failed()
    except AssertionError as e:
        print("Caught exception {0}".format(e))