'''
Created on Oct 17, 2013

@author: wangboqi

REFERENCES: 
Errors and Exceptions: http://docs.python.org/2/tutorial/errors.html
'''


# the old way
try:
    raise ValueError("deliberate")
except Exception, e:
    print "Caught Exception"

# the morden way
try:
    raise ValueError("Deliberate")
except Exception as e:
    print "Caught Exception"

# catch multiple exceptions
try:
    raise ValueError("Deliberate")
except (Exception, ValueError) as e:
    print "Caught Exception"

# omit the exception name, to serve as wildcard
try:
    raise ValueError("Deliberate")
except (Exception, ValueError):
    print "Caught Exception"

# catch-call

try:
    raise ValueError("Deliberate")
except:
    print "Caught Exception"
# else-parts (*optional)
try:
    pass
except (Exception, ValueError):
    print "Caught Exception"
else:
    print "No exception"

# finally-part (*optional)
try:
    pass
except (Exception, ValueError):
    print "Caught Exception"
else:
    print "No exception"
finally:
    print "Finally clean-up"
    