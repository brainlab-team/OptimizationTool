import numpy
from numpy import *
from decimal import *

random.seed(19680801)

# Number Randomization


def randomint(low, high):
    ""
    if low <= high:
        return random.randint(low, high)
    else:
        return -1.0


def randomfloat(low = 0.0, high = 1.0):
    ""
    if low <= high:
        return random.uniform(low, high)
    else:
        return -1.0


def randombit():
    ""
    return random.choice([0, 1])


def perm(lenght):
    ""
    return random.permutation(lenght)


# Matrix management

def col(mat, index):#ottengo vettore colonna all'indice 
    ""
    mat = castmat(mat)
    c = mat[:, index]
    c = transpose(c)
    c = castarr(c)
    return c


def row(mat, index):
    ""
    mat = castmat(mat)
    r = mat[index, :]
    r = castarr(r)
    return r


def elem(mat, r, c):
    ""
    rel = row(mat, r)
    cel = col(rel, c)
    return cel[0]


def submatrix(mat, perm, startind, stopind):
    ""
    return [(row(mat, perm[i]).tolist())[0] for i in range(startind, stopind)]


def newmat(rows, cols):
    ""
    return zerosmat(rows, cols)


def onesmat(rows, cols):
    ""
    return numpy.asmatrix(numpy.ones((rows, cols), dtype = numpy.dtype(Decimal)))



def zerosmat(rows, cols):
    ""
    return numpy.asmatrix(numpy.zeros((rows, cols), dtype = numpy.dtype(Decimal)))


def castmat(doublearray):
    ""
    return numpy.asmatrix(doublearray, dtype = numpy.dtype(Decimal))


def transpmat(matrix):
    ""
    return castmat(numpy.transpose(matrix))


def covmat(matrix):
    ""
    matrix = castmat(matrix)
    matrix = matrix.T
    [nrows, ncols] = matrix.shape
    means = rowsmean(matrix)
    adj = numpy.repeat(means, nrows, axis=0)
    cov = onesmat(ncols, ncols)
    for i in range(0, ncols):
        x1 = matrix[:,i]
        mx1 = adj[:, i]
        for j in range(i, ncols):
            x2 = matrix[:, j]
            mx2 = adj[:, j]
            prod = prodmat(transpmat(x1 - mx1), x2 - mx2)
            val = prod[0, 0]/(nrows)
            cov[i, j] = val
            cov[j, i] = val
    return cov


def covnormat(matrix):
    ""
    matrix = castmat(matrix)
    [nrows, ncols] = matrix.shape
    cov = onesmat(ncols, ncols)
    for i in range(0, ncols):
        x1 = matrix[:,i]
        for j in range(i, ncols):
            x2 = matrix[:, j]
            prod = prodmat(transpmat(x1), x2)
            val = prod[0, 0]/(nrows-1)
            cov[i, j] = val
            cov[j, i] = val
    return cov


def diagmat(matrix):
    ""
    try:
        matrix = numpy.array(matrix, dtype=numpy.float)
        [w, v] = numpy.linalg.eig(matrix)
        return [castarr(w), castmat(v)]
    except linalg.LinAlgError:
        print("Computation does not converge!")
    return [None, None]


def rowsmean(matrix):
    ""
    return numpy.mean(castmat(matrix), 0, dtype=numpy.dtype(Decimal))


def rowsmin(matrix):
    ""
    return numpy.amin(matrix, 0)


def rowsmax(matrix):
    ""
    return numpy.amax(matrix, 0)


def rowsstd(matrix):
    ""
    return numpy.std(matrix, 0, dtype=numpy.dtype(Decimal))


def prodmat(matrix1, matrix2):
    ""
    [arows, acols] = matrix1.shape
    [brows, bcols] = matrix2.shape
    if acols != brows:
        return None
    prod = newmat(arows, bcols)
    for i in range(0, arows):
        for j in range(0, bcols):
            sum = Decimal(0)
            for k in range(acols):
                sum = sum + (Decimal(matrix1[i, k]) * Decimal(matrix2[k, j]))
            prod[i, j] = Decimal(sum)
    return prod


def zeromean(matrix):
    ""
    matrix = castmat(matrix)
    [nsamples, ndimensions] = matrix.shape
    zmean = newmat(nsamples, ndimensions)
    mean = rowsmean(matrix)
    meanmat = prodmat(onesarr(nsamples), mean)
    for j in range(0, ndimensions):
        zmean[:, j] = matrix[:, j] - meanmat[:, j]
    return zmean


def scale(matrix):
    ""
    matrix = castmat(matrix)
    [nsamples, ndimensions] = matrix.shape
    zmean = newmat(nsamples, ndimensions)
    mean = rowsmean(matrix)
    std = rowsstd(matrix)
    meanmat = prodmat(onesarr(nsamples), mean)
    for j in range(0, ndimensions):
        zmean[:, j] = (matrix[:, j] - meanmat[:, j])
        val = col(std, 0)
        zmean[:, j] = zmean[:, j]/val
    return zmean


def printmat(matrix, limit = -1):
    ""
    if matrix is None:
        return
    [nrows, ncols] = matrix.shape
    limited = False
    if limit != -1 and limit < nrows:
        nrows = limit
        limited = True
    for i in range(0, nrows):
        s = "Riga {}:".format(i)
        for j in range(0, ncols):
            s = s + str(matrix[i, j]) + "  "
        print( s + "\n")
    if limited: print("   ....  limited to {} items!\n".format(limit))


# ndArray management

def newarr(lenght):
    ""
    return castarr(zerosarr(lenght))


def onesarr(lenght):
    ""
    return numpy.ones([lenght,1], dtype=numpy.dtype(Decimal))


def zerosarr(lenght):
    ""
    return numpy.zeros([lenght,1], dtype=numpy.dtype(Decimal))


def castarr(array):
    ""
    return numpy.asarray(array, dtype = numpy.dtype(Decimal))


def subarray(array, perm, startind, stopind):
    ""
    return [array[perm[i]] for i in range(startind, stopind)]


def transparr(array):
    ""
    return numpy.asarray(numpy.transpose(array), dtype=numpy.dtype(Decimal))


def printarr(array, limit = -1):
    ""
    arr = array.tolist()
    nrows = len(arr)
    limited = False
    if limit != -1 and limit < nrows:
        nrows = limit
        limited = True
    for i in range(0, nrows):
        print( "{} ".format(arr[i]))
    if limited: print( "\n   ....  limited to {} items!\n".format(limit))


def sortarr(array, asc = 0):
    ""
    _mergesort(array, asc, 0, len(array)-1)


def _mergesort(array, asc, left, right):
    ""
    if left < right:
        center = (left + right)/2
        _mergesort(array, asc, left, center)
        _mergesort(array, asc, center+1, right)
        if asc == 0:
            _merge(array, left, center, right)
        else:
            _mergeasc(array, left, center, right)


def _merge(array, left, center, right):
    ""
    i = left
    j = center + 1
    k = 0
    b = [0 for val in range(0, right - left + 1)]
    while i <= center and j <= right:
        if array[i] <= array[j]:
            b[k] = array[i]
            i = i + 1
        else:
            b[k] = array[j]
            j = j + 1
        k = k + 1
    while i <= center:
        b[k] = array[i]
        i = i + 1
        k = k + 1
    while j <= right:
        b[k] = array[j]
        j = j + 1
        k = k + 1
    for k in range(left, right+1):
        array[k] = b[k - left]


def _mergeasc(array, left, center, right):
    ""
    i = left
    j = center + 1
    k = 0
    b = [0 for val in range(0, right - left + 1)]
    while i <= center and j <= right:
        if array[i] >= array[j]:
            b[k] = array[i]
            i = i + 1
        else:
            b[k] = array[j]
            j = j + 1
        k = k + 1
    while i <= center:
        b[k] = array[i]
        i = i + 1
        k = k + 1
    while j <= right:
        b[k] = array[j]
        j = j + 1
        k = k + 1
    for k in range(left, right+1):
        array[k] = b[k - left]





















