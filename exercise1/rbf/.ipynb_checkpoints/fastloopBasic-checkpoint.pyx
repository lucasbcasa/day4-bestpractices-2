import numpy as np

cdef extern from "math.h":
    double exp(double x)

def rbf_network_cython(double[:,:] X, double[:] beta, int theta):

    cdef int N = len(X)
    cdef int D = len(X[0])
    Y_np = np.zeros(N)
    cdef double[:] Y=Y_np
    theta = theta * theta
    cdef int i = 0
    cdef int j = 0
    cdef int d = 0
    cdef float r = 0
    while i < N:
        j=0
        while j < N:
            r = 0
            d = 0
            while d < D:
                r+= (X[j, d] - X[i, d]) ** 2
                d += 1
            Y[i] += beta[j] * exp(-r*theta)
            j+=1
        i+=1
    return Y


#  r = -sum([(X[j, d] - X[i, d]) ** 2 for d in range(D)]) * theta
#  Y[i] += beta[j] * exp(r)