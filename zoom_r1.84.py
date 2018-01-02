#!/usr/bin/python

# Attempt to do a Nova fractal in Python.
# JM Wed 23 Aug 2017 14:58:14 BST
# Use more recent colour map.
# JM Tue 29 Aug 2017 12:08:41 BST

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list

start = timer()

X_MIN = -1.25
X_MAX =  1.25
Y_MIN = -1.25
Y_MAX =  1.25
offset  = 0.001
epsilon = 0.01
maxiter = 50
calc_count = 0
rnum       = 73
lenlc      = len( colour_list )  
R          = 1.84

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

		while ( abs ( R * (Z**3 - 1) ) >= epsilon and iter_count < maxiter ):
			if ( Z ):
				Z =  Z - ( R * ( Z**3 - 1 ) / ( 3 * Z**2 ) )

			iter_count = iter_count + 1
		
			calc_count = calc_count + 1  
                if ( iter_count + rnum  >= lenlc ):
                        mycolour = colour_list[ iter_count % lenlc ]
                else:   
                        mycolour = colour_list[ iter_count + rnum  ]

		if ( iter_count <= 2 ):
			img.putpixel( ( x_pixel,  y_pixel ), white ) 

		elif ( iter_count == maxiter ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		y_pixel += 1
		
	x_pixel += 1

dt = timer() - start

MsgText = 'Nova for Z^3 = 1 ' + ' and rnum: ' + str( rnum ) + 'R: ' + str( R )
fname = 'Nova_R:' + str( R ) + '_' + str( X_MAX ) + str( X_MIN ) + '_Y:' + str( Y_MAX ) + str( Y_MIN ) + '.png'

draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/Library/Fonts/Arial.ttf", 12 )
draw.text( ( 0, 0 ),  MsgText, ( 139,0,0 ), font=font )

print 'Nova R:', R, ' and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count
print 'Fname:', fname
img.show()
img.save( fname )


