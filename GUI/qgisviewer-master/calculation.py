import matrix
import math

#matrix initializatioin
xCord=matrix.zero(100,100)
yCord=matrix.zero(100,100)
elev=matrix.zero(100,100)
area=0.0
cvol=0.0
fvol=0.0
rvol=0.0
vol=0.0
tempvol=0.0

##we can assign the value into the matrix like this...
"""xCord[0][0]=2
xCord[0][1]=5
xCord[1][0]=3
xCord[1][1]=6

yCord[0][0]=4
yCord[0][1]=6
yCord[1][0]=8
yCord[1][1]=9

elev[0][0]=6
elev[0][1]=7
elev[1][0]=3
elev[1][1]=6"""




def calcArea(i, j, p, q):
	length=0.0
	readth=0.0
	dx=0.0
	dy=0.0
	dx=xCord[i][j]-xCord[i][q] #x coordinate difference
	dy=yCord[i][j]-yCord[i][q] #y coordinate difference
	
	# checking for the negative value	

	if dx<0:
		dx=dx*-1
	if dy<0:
		dy=dy*-1
	#calculating the length of one segment
	
	length=math.sqrt(math.pow(dx,2.0)+math.pow(dy,2.0))

	# difference in x and y coordinate for calculating the breadth
	dx=xCord[i][j]-xCord[p][j]
	dy=yCord[i][j]-yCord[p][j]
	if dx<0:
		dx=dx*-1
	if dy<0:
		dy=dy*-1
	breadth=math.sqrt(math.pow(dx,2.0)+math.pow(dy,2.0))

	return (length*breadth)# return area of the rectangle

def calcVol(i, j, p, q, area):
	avelv=0.0
	avelv=(elev[i][j]+elev[i][q]+elev[p][j]+elev[p][q])/4.0 #average elevation of 4 points
	return (area*avelv)

def calc(xCord, yCord, elev):

	print xCord
	print yCord
	print elev
	fvol = 0
	cvol = 0
	for i in range(10):
		for j in range(10):
			area=calcArea(i,j,i+1,j+1)
			vol=calcVol(i,j,i+1,j+1,area)
			if j==0:
				rvol=vol# storing the volume of road to compare with other volumes....
			else:
				tempvol=rvol-vol # finding the difference in volume
				if tempvol<0:
					cvol+=(tempvol*-1) # adding to cutt volume
				elif tempvol>0:
					fvol+=tempvol # adding to fill volume
		
	print "\nThe Fill volume is: "
	print fvol
	print "\nThe cut volume is: "
	print cvol
