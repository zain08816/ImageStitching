import numpy as np

# p1 and p2 are points in the first image. P1 and P2 are the corresponding points in the second image.
# Returns a 2x2 numpy matrix (m) such that p1*m=P1 and p2*m=P2.
def transformationMatrixFromPoints(p1, p2, P1, P2):
	a = np.array([[p1[0],p1[1]], [p2[0],p2[1]]])
	b = np.array([P1[0],P2[0]])
	c = np.array([P1[1],P2[1]])
	x = np.linalg.solve(a, b)
	y = np.linalg.solve(a, c)
	return np.transpose(np.vstack((x, y)))