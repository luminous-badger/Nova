#!/usr/bin/python

# Attempt to do a Newton fractal in Python.
# JM Sun 21 Dec 2014 13:51:00 GMT

from PIL import Image
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list

start = timer()

X_MIN = -4.0
X_MAX =  4.0
Y_MIN = -4.0
Y_MAX =  4.0
offset     = 0.01
epsilon    = 0.01
maxiter    = 50
calc_count = 0
rnum       = nm.random.randint( 1,100,1 )
lenlc      =  len( colour_list )  

X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1
X_SIZE  = int( X_SIZE )
Y_SIZE  = int( Y_SIZE )
print 'X: ', X_SIZE ,' Y: ', Y_SIZE 

white      = (255,255,255)
randcolour = (255,255,255) # ( 90, 90, 90 )
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )
mycolour   = ( 100, 150, 200 ) 

x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		#Z = complex ( 0, 0 )
		Z = complex ( X, Y )
		iter_count = 0

		while ( abs ( Z**3 - 1 ) >= epsilon and iter_count < maxiter ):
			if ( Z ):
				Z =  Z - ( ( Z**3 - 1 ) / ( 3 * Z**2 ) )

			iter_count = iter_count + 1
		
			calc_count = calc_count + 1  
                if ( iter_count > 10 and iter_count <= 30 ):
			mycolour = colour_list[ iter_count + 56 ]
		else:
			mycolour = colour_list[ iter_count % lenlc  ]
		if ( iter_count <= 10 ):
			try:
				img.putpixel( ( x_pixel,  y_pixel ), white ) 
			except:
				print 'Err: X,Y', x_pixel,  y_pixel
				#pass
		elif ( iter_count == maxiter ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		'''
		mycolour = colour_list[ iter_count % lenlc  ]
		img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		'''
		y_pixel += 1
		
	x_pixel += 1

dt = timer() - start

print 'Newton and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count
img.show()
#img.save( 'AFoolJuliaBrot.png' )

