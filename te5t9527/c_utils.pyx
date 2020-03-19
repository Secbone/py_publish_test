# cython: language_level = 3, infer_types = True, boundscheck = False

import numpy as np
cimport numpy as np
cimport cython



cdef int c_min(int[:] arr):
    cdef int res = np.inf

    for i in range(arr.shape[0]):
        if res > arr[i]:
            res = arr[i]
    return res
