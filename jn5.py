#!/usr/bin/python

# Attempt to do a Newton Julia fractal in Python.
# JM Sun 21 Dec 2014 13:51:00 GMT
# Newton Julia for arbitrary power of Z.
# JM Thu  7 Sep 2017 10:44:17 BST

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list

start = timer()

X_MIN = -2.0
X_MAX =  2.0
Y_MIN = -2.0
Y_MAX =  2.0
offset     = 0.01
epsilon    = 0.01
maxiter    = 50
calc_count = 0
rnum       = 43
lenlc      = len( colour_list )  
C          = complex ( 0.00175,  0.001 )
ZPower     = 5

X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1
X_SIZE  = int( X_SIZE )
Y_SIZE  = int( Y_SIZE )
print 'X: ', X_SIZE ,' Y: ', Y_SIZE 

white      = (255,255,255)
randcolour = ( 90, 90, 90 )
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )
mycolour   = ( 100, 150, 200 ) 

x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( X, Y )
		iter_count = 0

		while ( abs ( Z**ZPower - 1 ) >= epsilon and iter_count < maxiter ):
			if ( Z ):
				Z = ( Z - ( ( Z**ZPower - 1 ) / ( ZPower * Z**( ZPower - 1 ) ) ) ) + C

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
		'''
		mycolour = colour_list[ iter_count % lenlc  ]
		img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		'''
		y_pixel += 1
		
	x_pixel += 1

dt = timer() - start

MsgText = 'Newton Julia for Z^' + str( ZPower ) + ' + ' + str( C ) + ' and rnum: ' + str( rnum )
fname = 'Newton_Julia_Z^' + str( ZPower ) + '_X:' + str( X_MAX ) + str( X_MIN ) + '_Y:' + str( Y_MAX ) + str( Y_MIN ) + str( C ) + '.png'

draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/Library/Fonts/Arial.ttf", 12 )
draw.text( ( 0, 0 ),  MsgText, ( 139,0,0 ), font=font )

print MsgText
print 'Created in %f s' % dt
print 'Calc: ', calc_count
print 'Fname:', fname

img.show()
#img.save( fname )

