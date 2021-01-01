def Point_addition(v1,v2):

	O = (0,0)

	if v1 == O:   
		return v2

	elif v2 == O: 
		return v1

	else:         
		x1,y1 = v1
		x2,y2 = v2

		if (x1 == x2) and (y1 == -y2): 
			return O

		else: 

			if v1 != v2: 
				l = (y2 - y1) * pow(x2-x1, -1 ,p)

			else: 
				l = ( ( 3*pow(x1,2) + a ) * pow(2 * y1,-1 , p) ) 


	x3 = (l**2 - x1 - x2 ) % p     
	y3 = (l*(x1 - x3) - y1) % p 


	return (x3,y3)


a = 497
b = 1768
p = 9739

P = (493, 5564)
Q = (1539, 4742)
R = (4403,5202)

k1 = Point_addition(P,P) 
k2 = Point_addition(k1,Q) 
k3 = Point_addition(k2,R) 
S =  k3 
print("crypto{",S,"}")
