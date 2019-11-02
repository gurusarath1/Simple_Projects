def sortX(xy):
	return xy[0]

def sortY(xy):
	return xy[1]

def distance(p1,p2):
	return ( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2  )**0.5
	
def ClosestPairAcross(points, delta):

	print('Entry Across - ', points, delta)

	Strip = []
	minD = delta
	minXY = None
	mid = int( len(points) / 2 )

	mid_x = points[mid][0]

	for pt in points:
		if pt[0] <= (mid_x + delta) and pt[0] >= (mid_x - delta):
			Strip.append(pt)

	Strip.sort(key=sortY)

	print('Strip - ', Strip)

	for pt_i in range(len(Strip)):
		pt_j = pt_i + 1

		while pt_j < len(Strip) and ((Strip[pt_j][1] - Strip[pt_i][1]) < minD ):
			
			if distance(Strip[pt_j] , Strip[pt_i]) < minD:
				minD = distance(Strip[pt_j] , Strip[pt_i])
				minXY = [ Strip[pt_j] , Strip[pt_i] , minD ]

			pt_j += 1


	if not minXY:
		print('Exit Across - ', [None , None , float('inf')])
		return [None , None , float('inf')]

	return minXY

def ClosestPair(points):

	print( 'Entry - ' , points)

	if len(points) <= 1:
		print( 'Exit Inf - ' , points)
		return [None, None, float('inf')]

	if len(points) == 2:
		return [ points[0], points[1], distance(points[0], points[1]) ]

	if len(points) == 3:
		d1 = distance(points[0] , points[1])
		d2 = distance(points[1] , points[2])
		d3 = distance(points[2] , points[0])

		if d1 < d2 and d1 < d3:
			return [points[0] , points[1] , d1]

		if d2 < d1 and d2 < d3:
			return [points[1] , points[2] , d2]

		if d3 < d1 and d3 < d2:
			return [points[2] , points[0] , d3]


	mid = int( len(points) / 2 )

	LeftPoints = points[0:mid]
	RightPoints = points[mid:]

	pair_Left = ClosestPair(LeftPoints)
	pair_Right = ClosestPair(RightPoints)
	delta = float('inf')

	if pair_Left != None and pair_Right != None:

		if pair_Right[2] < pair_Left[2]:
			delta = pair_Right[2]
		else:
			delta = pair_Left[2]

	elif pair_Right == None:

		delta = pair_Left[2]

	elif pair_Left == None:

		delta = pair_Right[2]

	pair_across = ClosestPairAcross(points, delta)

	FinalMin = min(pair_Left[2] , pair_Right[2] , pair_across[2])
	FinalReturn = []

	print( 'Exit - ' , pair_Left , pair_Right , pair_across)

	if FinalMin == pair_Right[2]:
		FinalReturn.append(pair_Right[0])
		FinalReturn.append(pair_Right[1])
		FinalReturn.append(FinalMin)
		return FinalReturn

	if FinalMin == pair_Left[2]:
		FinalReturn.append(pair_Left[0])
		FinalReturn.append(pair_Left[1])
		FinalReturn.append(FinalMin)
		return FinalReturn

	if FinalMin == pair_across[2]:
		FinalReturn.append(pair_across[0])
		FinalReturn.append(pair_across[1])
		FinalReturn.append(FinalMin)
		return FinalReturn


Points = [(1,2),(5,6),(1,4),(8,6),(3,7)]
Points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
Points = [(1,1) , (2,2) , (5,5) , (5.1,5) , (100,100) , (1000,1000)]
Points.sort(key=sortX)
listX = Points[:]



M = ClosestPair(listX)
print(M)