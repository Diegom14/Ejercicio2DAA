def binary_search(A,	key):	
		pos	=	-1			
		lo	=	0
		hi	=	len(A)	-1
			
		while	lo	<=	hi:	
				mid	=	lo	+	(hi-lo)//2
				if	A[mid]	<	key:	
						lo	=	mid+1
				elif	A[mid]	>	key:	
						hi	=	mid-1
				else:	
						pos	=	mid	
						break
		return	pos

def tres_sum(A):
	n = len(A)
	count = 0
	key = 0
	A.sort()
	for i in range(n):
		for j in range(i+1,n):
			key = A[i] + A[j]
			key = (-key)
			if binary_search(A, key) != -1: 
				count =+ 1
	return count

