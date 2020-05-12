# Just that

def jaccard_index(A,B):
	intersection = set(A) & set(B)
	union = set(A) | set(B)
	
	return len(intersection)/len(union)
