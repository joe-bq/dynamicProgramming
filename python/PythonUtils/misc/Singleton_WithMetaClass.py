# what is a meta-class in Python: http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python

class Singleton(type):
	def __init__(cls, name, bases, dict):
		super(Singleton, cls).__init__(name, bases, dict)
		cls.instance = None
	def __call__(cls, *args, **kwargs):
		if  cls.instance is None:
			cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
		return cls.instance

class Foo:
	__metaclass__ = Singleton

if __name__ == "__main__":
	if Foo() is Foo():
		print "the Same"
	else:
		print "Different"