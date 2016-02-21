# author:
#  Joe 
# file:
#   find_oqlsource_dup.py
# description:
#   process the availabel columns from the CashTraderTrades.txt file
# reference:
#   for the script to work, the following tutorial on the python has been consulted.
#     xml.etree.ElementTree  - The ElementTree XML API :  http://docs.python.org/2/library/xml.etree.elementtree.html
#     mapping Operators to Functions: http://docs.python.org/2/library/operator.html#mapping-operators-to-functions

import xml.etree.ElementTree as ET
import re
import operator

tree = ET.parse("CashTraderTradesGridConfig.txt")
root = tree.getroot()

if root is None:
	raise ArgumentError("Cannot find file CashTraderTradesGridConfig.txt")


value_pattern = re.compile("\[(?P<value>[\w\.]+?)\]")
fields_list = []
for child in root:
	child_node = child.find('Value')
	if child_node is not None and not "EvaluatorFunctions" in child_node.get('value'):
		value = child.find('Value').get('value')
		match_result = value_pattern.match(value)
		if match_result:
			fields_list.append(match_result.group('value'))
		else:
			print "failed to find a pattern match, value = ", value
	else:
		if child_node is None:
			print "item do not have a Value field, dump result is ", ET.dump(child)
		elif operator.contains(child_node.get('value'), "EvaluatorFunctions"):
			print "Ignoring fields that has EvaluatorFunctions: id = ", child.find('Id').get('value')

# remove duplicate
value_set = set()
duplicate_found = False
for value in fields_list:
	if value not in value_set:
		value_set.add(value)
	else: 
		duplicate_found = True
		print "found duplicate on", value

# as is said in the Python document about hte built-in operators, the 'in' operaors maps to the 'contains' methods
#   check 
if duplicate_found:
	for value in value_set:
		print "<i value=\"" + value + "\" />" # can not call print "<i value=\"" + value + "\" />" because it join with a space
else:
	for value in fields_list:
		print "<i value=\"" + value + "\" />" # can not call print "<i value=\"" + value + "\" />" because it join with a space
