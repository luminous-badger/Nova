#!/usr/bin/python

# Attempt to do Newton method in Python. Thre cube roots of 1.
# JM Wed 27 Sep 2017 14:49:02 BST

'''
The complex roots are:
-0.5 + 0.866*i
-0.5 - 0.866*i

cos 2pi/3 + i sin 2pi/3 = -1/2 + i sqrt(3)/2

cos 4pi/3 + i sin 4pi/3 = -1/2 - i sqrt(3)/2
>>> import math
>>> math.sqrt(4)
2.0
>>> math.sqrt(3)
1.7320508075688772
>>> 1.7320508075688772 / 2.0
0.8660254037844386
'''

import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list

start = timer()

X_MIN = -0.6
X_MAX =  0.6
Y_MIN = -1.0
Y_MAX =  1.0
offset     = 0.01
epsilon    = 1e-6
maxiter    = 50
calc_count = 0
Z = complex ( 0, 0 )

for X in nm.arange ( X_MIN, X_MAX, offset ):
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( X, Y )
		iter_count = 0

		#while ( abs ( Z**3 - 1 ) >= epsilon and iter_count < maxiter ):
		while ( abs ( Z**3 - 1 ) >= epsilon ):
			if ( Z ):
				Z =  Z - ( ( Z**3 - 1 ) / ( 3 * Z**2 ) )

			#print 'X:', X, ' Y:', Y, ' Z:', Z, ' I:',iter_count, ' Abs Z3 - 1:', abs ( Z**3 - 1 ) 
			iter_count = iter_count + 1
		
			calc_count = calc_count + 1  
		print 'X:', X, ' Y:', Y, ' Z:', Z, ' I:',iter_count, ' Abs Z3 - 1:', abs ( Z**3 - 1 ) 

dt = timer() - start

print '\n\n'
print 'X:', X, ' Y:', Y, ' Z:', Z, ' I:',iter_count
print '\n\n'
print 'Newton Method created in %f s' % dt
print 'Calc: ', calc_count
