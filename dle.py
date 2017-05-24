import numpy as np

pre = -0.36641
cursor = 0.18808
post1 = -0.35177
post2 = -0.4707
zero = -0.49841

x1 = pre - zero
x0 = cursor - zero
xn1 = post1 - zero
xn2 = post2 - zero

y = np.matrix('0; 0; 1; 0')
A = np.matrix([[x0, xn1, xn2, 0], [x1, x0, xn1, xn2], [0, x1, x0, xn1], [0, 0, x1, x0]])
c = np.linalg.solve(A, y)
c_norm = c / np.sum(np.absolute(c))

print "post2: %f" % -c_norm[0]
print "post1: %f" % -c_norm[1]
print "pre: %f" % -c_norm[3]
