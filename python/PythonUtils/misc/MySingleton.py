class Singleton(object): # you have to use the new object style (you cannot just use the old class Single: ...)
  _instance = None
  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs) # this has restriction in that it hard-coded the name of Singleton here, which is not extensible.
    return cls._instance                                                  # also, since Singleton will invoke __init__ of Singleton, the __new__(cls) will also call __init__? you end up have two __init__ method called.
  def __init__(self):
  	print "Singleton"

class Singleton_Derived(Singleton):
	def __init__(self):
		# the old way 
		super(self.__class_, self).__init()
		super() # this is the new Python 3. syntax which will allow you to call into super method with a simple call. 
		print "Singleton_Derived.__init__"


if __name__ == '__main__':
  singleton = Singleton()
  singleton2 = Singleton()
  if id(singleton) == id(singleton2):
  	print "The same "
  else:
    print " not the same"

  s1 = Singleton_Derived()
  s2 = Singleton_Derived()
  if id(s1) == id(s2):
  	print "The same"
  else:
  	print "Not the same"

#class Singleton(object):
#    _instance = None
#    def __new__(cls, *args, **kwargs):
#        if not cls._instance:
#            cls._instance = super(Singleton, cls).__new__(
#                                cls, *args, **kwargs)
#        return cls._instance
#
#
#if __name__ == '__main__':
#    s1=Singleton()
#    s2=Singleton()
#    if(id(s1)==id(s2)):
#        print "Same"
#    else:
#        print "Different"
