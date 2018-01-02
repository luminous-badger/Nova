#!/usr/bin/python

# Attempt to do a Newton fractal in Python.
# JM Sun 21 Dec 2014 13:51:00 GMT
# Newton fractal for any power of Z.
# JM Wed 13 Sep 2017 13:32:10 BST
# Attempt to cure overflow error for power = 10

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list

start = timer()

X_MIN = -3.0
X_MAX =  3.0
Y_MIN = -3.0
Y_MAX =  3.0
offset     = 0.01
epsilon    = 0.01
maxiter    = 150
calc_count = 0
rnum       = nm.random.randint( 1,100,1 )
rnum       = 38
lenlc      = len( colour_list )  
ZPower     = 10

X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1
X_SIZE  = int( X_SIZE )
Y_SIZE  = int( Y_SIZE )
print 'X: ', X_SIZE ,' Y: ', Y_SIZE 

white      = (255,255,255)
randcolour = (176,196,222) 
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )
mycolour   = ( 100, 150, 200 ) 

x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		#Z = complex ( 0, 0 )
		Z = complex ( X, Y )
		iter_count = 0

		CALC_ERROR = False
		while ( iter_count < maxiter and not CALC_ERROR ):
			#if ( Z ):
			try:
				Z =  Z - ( ( Z**ZPower - 1 ) / ( ZPower * Z**( ZPower - 1 ) ) )
			except:		
				print 'CALC ERROR X,Y,Z,i:', X,Y,Z,iter_count
				CALC_ERROR = True
				pass

			try:
				if ( abs ( Z**ZPower - 1 ) < epsilon  ):
					#print 'BREAK X,Y,Z,ABS,iter:', X,Y,Z,abs ( Z**ZPower - 1 ), iter_count 
					break
			except:		
				print 'ABS ERROR X,Y,Z,i:', X,Y,Z,iter_count
				CALC_ERROR = True
				pass
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

MsgText = 'Newton for Z^' + str( ZPower ) + ' and rnum: ' + str( rnum )
fname = 'Newton_Z^' + str( ZPower ) + '_X:' + str( X_MAX ) + str( X_MIN ) + '_Y:' + str( Y_MAX ) + str( Y_MIN ) + '.png'

draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/Library/Fonts/Arial.ttf", 12 )
draw.text( ( 0, 0 ),  MsgText, ( 139,0,0 ), font=font )

print MsgText
print 'Created in %f s' % dt
print 'Calc: ', calc_count
print 'Fname:', fname

img.show()
#img.save( fname )

