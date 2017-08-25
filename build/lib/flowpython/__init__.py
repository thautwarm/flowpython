# -*- coding: utf-8 -*-
__version__ = VERSION = "0.2.1.1"
__author__  = AUTHOR  = "thautwarm"
__lisence__ = LISENCE = "MIT"
__doc__     = DOC     =    \
"""
Additional 

See flowpython grammar in https://github.com/thautwarm/flowpython

	See https://github.com/thautwarm/flowpython/blob/master/ReadMe.md
	Wiki: https://github.com/thautwarm/flowpython/wiki

	lambdef :
		.x -> .y -> x+y
		as-with x def as y def x+y
		lamdba x: lambda y : x+y
	
	multi-row lambdef:
		.x -> .y -> ret where:
			import math
			ret1 = math.exp(x-y)

	where syntax:

		# surface area of a cylinder
		from math import pi
		
		r = 1 #radius
		h = 1 #height
		
		S = (2*S_top + S_side) where:
		    S_top  = pi*r**2
		    S_side = C * h where:
		        C = 2*pi*r

	Pattern Matching:

		condic 1:
		
		+(type)
		case a:int => a+1

		[is not]   
		case 1     => assert 1 is not 1

		{.x,y->x+y == 5}
		case 4     => assert 1+4 == 5

		otherwise  => print("otherwise")
	Plus: Matching Filter:
		condic[] [1,2,3]: # use a seq as test expression , you should write "condic[] seq", "condic{} seq", "condic() seq".
			+(type)
			case (*a,b) -> a : list => sum(a)


	Arrow Transform

		>> range(5) -> map(.x->x+1, _) -> list(_)
		>> [1,2,3,4,5]


	See the tutorials with more details and exmaples about Pattern Matching in https://github.com/thautwarm/flowpython/wiki.

"""

	

class helper:
	doc      = __doc__
	version  = __version__
	author	 = __author__
	lisence  = __lisence__

	 