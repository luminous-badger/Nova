#!/usr/bin/python

# Attempt to do a Newton fractal in Python.
# JM Sun 21 Dec 2014 13:51:00 GMT
# Newton fractal for any power of Z.
# JM Wed 13 Sep 2017 13:32:10 BST
'''
Traceback (most recent call last):
File "./npower.py", line 53, in <module>
while ( abs ( Z**ZPower - 1 ) >= epsilon and iter_count < maxiter ):
OverflowError: complex exponentiation

got an error for Zpower = 10.
moving the epsilon comparison inside the loop,with a break, seemed to cure it.
'''

import numpy as nm
import cmath
from timeit import default_timer as timer

start = timer()

X_MIN = -0.1
X_MAX =  0.5
Y_MIN = -0.8
Y_MAX =  1.1
offset     = 0.01
epsilon    = 0.01
maxiter    = 150
calc_count = 0
rnum       = nm.random.randint( 1,100,1 )
rnum       = 81
ZPower     = 10

X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1
X_SIZE  = int( X_SIZE )
Y_SIZE  = int( Y_SIZE )
print 'X: ', X_SIZE ,' Y: ', Y_SIZE, 'ZPower:', ZPower


x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		#Z = complex ( 0, 0 )
		Z = complex ( round( X, 3 ), round( Y, 3 ) )
		iter_count = 0

		print 'X,Y,Z:', X,Y,Z
		print ' X:  {0:3f}'.format( X ),
		print ' Y:  {0:3f}'.format( Y )
		print ' Round X:,', round ( X, 3 ),
		print ' Round Y:,', round ( Y, 3 )
		print ' ZP:', Z**ZPower, ' ABS ZP:',  abs ( Z**ZPower  ), ' ABS Minus1 Brk:', abs ( (Z**ZPower) - 1 ), ' ABS Minus1:', abs ( Z**ZPower - 1 ) 

		#while ( abs ( Z**ZPower - 1 ) >= epsilon and iter_count < maxiter ):
		while ( iter_count < maxiter ):
			if ( Z ):
				Z =  Z - ( ( Z**ZPower - 1 ) / ( ZPower * Z**( ZPower - 1 ) ) )

			iter_count = iter_count + 1
		
			calc_count = calc_count + 1  
			try:
				if ( abs ( Z**ZPower - 1 ) >= epsilon ):
					break
			except:		
				print 'ERROR X,Y,Z:', X,Y,Z
				pass
		y_pixel += 1
		
	x_pixel += 1

dt = timer() - start

MsgText = 'Newton for Z^' + str( ZPower ) + ' + ' + ' and rnum: ' + str( rnum )
fname = 'Newton_Z^' + str( ZPower ) + '_X:' + str( X_MAX ) + str( X_MIN ) + '_Y:' + str( Y_MAX ) + str( Y_MIN ) + '.png'


print MsgText
print 'Created in %f s' % dt
print 'Calc: ', calc_count
print 'Fname:', fname
