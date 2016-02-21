############################################################
#
#  balanced_parentheses.py
#
# enumerate all the possible balanced parentheses for all expressions
#
############################################################


def parenthesized(exprs):
	if len(exprs) == 1:
		yield exprs[0]
	else:
		first_exprs = []
		last_exprs = list(exprs)
		while 1 < len(last_exprs):
			first_exprs.append(last_exprs.pop(0))
			for x in parenthesized(first_exprs):
				if 1 < len(first_exprs):
					x = '(%s)' % x
				for y in parenthesized(last_exprs):
					if 1 < len(last_exprs):
						y = '(%s)' % y
					yield '%s%s' % (x, y)


for x in parenthesized(['a', 'b', 'c', 'd']):
	print x


"""

there is a concise p0ython code as follow. 

http://stackoverflow.com/questions/6447289/how-to-print-all-possible-balanced-parentheses-for-an-expression


"""

def associations(seq, **kw):
    """
        >>> associations([1,2,3,4])
        [(1, (2, (3, 4))), (1, ((2, 3), 4)), ((1, 2), (3, 4)), ((1, (2, 3)), 4), (((1, 2), 3), 4)] 
    """
    grouper = kw.get('grouper', lambda a,b:(a,b))
    lifter = kw.get('lifter', lambda x:x)

    if len(seq)==1:
        yield lifter(seq[0])
    else:
        for i in range(len(seq)):
            left,right = seq[:i],seq[i:] # split sequence on index i

            # return cartesian product of left x right
            for l in associations(left,**kw):
                for r in associations(right,**kw):
                    yield grouper(l,r)