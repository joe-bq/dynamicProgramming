import sys
import re

f = sys.stdin



def printItem(item):
   if item != '':
     print("<i value=\"{}\" />".format(item))

	 
def printInputTransformItem(item):
  if item <> '': # <> is kept as a backward compatability  only measure http://docs.python.org/2/library/stdtypes.html
     print('''<i model="Sonic.Tabular.ColumnMapping:1">
    <InputColumnName value="{0}"/>
    <OutputColumnName value="{0}"/>
    <OutputColumnType type="type" value="string"/>
</i>'''.format(item)) # you cannot us the r'''stirng contents''' because the triple quotes cannot work with the r directive  


def printOutputItem(item):
  if item != "":
    print('''   <i model="Sonic.Tabular.ColumnDefinition:1">
   <Name value="{0}"/>
   <Type type="type" value="string"/>
</i>'''.format(item))


if __name__ == "__main__":
   #reg = re.compile('\[(\w+?)\]')
   reg = re.compile('\[(?P<field>\w+?)\]')
   for line in f:
      m = reg.search(line)
      if m:
         field = m.group('field') # you can also write as m.group(1)
         if not field == "":
            printOutputItem(field)
      else:
         print "did not found"
         break

		 
		 
