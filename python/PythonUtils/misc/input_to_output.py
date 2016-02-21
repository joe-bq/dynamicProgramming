import sys
import re
'''
this program does 

  python input_to_output.py < input > output 

  line by line copy of the content 

'''

class Transcriber:
	def __init__(self, fin = sys.stdin, fout = sys.stdout):
		self.fin = fin
		self.fout = fout
	def execute(self):
		if self.fin is not None:
			for line in self.fin:
				self.fout.write(line + "\n")

class LineUtil:
	@staticmethod
	def is_null_or_empty(line):
		if line is None or line == '': 
			True
		else:
			False


class LayoutProcessor:
	class Layout:
		class Document:
			def __init__(self, layout, fin = sys.stdin, fout = sys.stdout, ferr = sys.stderr):
				self.layout = layout
				self.fin = fin
				self.fout = fout
				self.ferr = ferr
				self.guid = ""
				self.name = ""
				self.prodider_type = None
				self.prefetched_line = ''
			def next(self):
				if self.guid is not None and self.guid != "" and self.name != '':
					self.fout.write(self.guid + ", " + self.name + "\n")
				while self.fin:
					line = self.fin.readline()
					if line == '':
						break
					if LineUtil.is_null_or_empty(line):
						break
					if self.seek_prefetch(line):
						self.layout.prefetched_line = line
						break
			def seek_prefetch(self, line):
				'''Seek with prefected lines it should delegate the job to the parent to determine if 
				the prefetched line is something shall be hanlded by the parent'''
				if line is None or line == '':
					return False
				else:
					return self.layout.seek_prefetch(line)
					# support certains type of prefetch and rolling up the chain

		def __init__(self, layoutProcessor, fin = sys.stdin, fout = sys.stdout, ferr = sys.stderr, print_only_match = True):
			self.layoutProcessor = layoutProcessor
			self.fin = fin
			self.fout = fout
			self.ferr = ferr
			self.doc_reg = re.compile("Name value=\"(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})\"")
			self.doc_displayname_reg = re.compile("DisplayName value=\"([^\"]+)\"")
			self.print_only_match = print_only_match
			self.doc = None
			self.prefetched_line = ''
		def next_document(self):
			def step_next_document(obj, line):
					if line == '':
						return
					match = self.doc_reg.search(line)
					if match is not None:
						if not self.doc:
							self.doc = LayoutProcessor.Layout.Document(self, self.fin, self.fout, self.ferr)
						self.doc.name = match.group(1)
					else:
						match = self.doc_displayname_reg.search(line)
						if match:
							if not self.doc:
								self.doc = LayoutProcessor.Layout.Document(self, self.fin, self.fout, self.ferr)
							self.doc.guid = match.group(1)
					if self.doc is not None and self.doc.guid != '' and self.doc.name != '':
						self.doc.next()						

			while self.fin:
				line = self.fin.readline()
				if line == '':
					break
				self.pretched_line = ''
				## JOE 
				## since the function step_next_document is defined nested in next_document, its scope is local to the 
				#   next_document method, so ther is no need to do self.step_next_document() and it is error to do self.step_next_document()
				step_next_document(self, line)
				## While __is_match method is defined in the class where 'next_document' is defined, so that the self.next_document has to be qualified
				if not LineUtil.is_null_or_empty(self.prefetched_line):
					if self.__is_match(self.prefetched_line):
						step_next_document(self, self.prefetched_line)
					elif self.seek_prefetch(self.prefetched_line):
						self.layoutProcessor.prefetched_line = self.prefetched_line
						break

				
		def seek_prefetch(self, line):
			if line is None or line == '':
				return False
			else:
				if not self.__is_match(line):
					return self.layoutProcessor.seek_prefetch(line)
				else:
					return True
		def __is_match(self, line):
			search = self.doc_reg.search(line)
			return  True if search is not None else (
						True if self.doc_displayname_reg.search(line) else (
							False))
	def __init__(self, fin = sys.stdin, fout = sys.stdout, ferr = sys.stderr):
		self.fin = fin
		self.fout = fout
		self.ferr = ferr
		self.name = ""
		self.layout_reg = re.compile("Element category=\"Onyx:Risk:Viewer:LayoutConfig\" id=\"([^\"]+)\"")
		self.prefetched_line = ''

	def next_layout(self):
		def step_next_layout(obj, line):
			if line == '':
				return
			#self.fout.write("Layout: {0}".format(line))
			match = obj.layout_reg.search(line)
			if match is not None:
				layout = LayoutProcessor.Layout(obj, obj.fin, obj.fout, obj.ferr)
				layout.name = match.group(1)
				layout.next_document()

		while self.fin:
			line = self.fin.readline()
			if line == '':
				break
			self.prefeched_line = ''
			step_next_layout(self, line)
			if not LineUtil.is_null_or_empty(self.prefetched_line):
				if self.__is_match(self.prefeched_line):
					step_next_layout(self, self.prefetched_line)


	def seek_prefetch(self, line):
		if LineUtil.is_null_or_empty(line):
			return False
		else:
			return self.__is_match(line)
	# Joe : 
	#  Private Methods: 
	#   http://www4.ncsu.edu/~kaltofen/courses/Languages/PythonExamples/python-lectures/_build/html/lectures/three.html#private-methods
	def __is_match(self, line):
		search = self.layout_reg.search(line)
		# True if search is not None else False
		if search is not None:
			return True
		else:
			return False
	def __search_get_name(self, line):
		search = self.layout_reg.search(line)
		return search.Group(1) if search is not None else None


if __name__ == '__main__':
	lp = LayoutProcessor()
	lp.next_layout()