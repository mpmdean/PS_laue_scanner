import numpy as np
from glob import glob
from PIL import Image

tol = 1e-4

def get_SC(n, X, Y):
    S = 2*np.ones_like(X)
    S[n] = 10
    C = ['k']*len(X)
    C[n] = 'r'
    return S, C

def get_filename(n):
    image_string = f'images/laue_{n:d}_*.tif'
    filename = glob(image_string.format(n))[0]
    return filename


def left(n, N, X, Y, tol=tol):
    NXY = np.vstack([N, X, Y]).T
    try:
        NXY = NXY[np.isclose(X, max(X[X<(X[n] - tol)]), tol)]
        NXY = NXY[np.argmin((NXY[:, 2] -Y[n])**2)]
        n = NXY[0]
    except ValueError:
        pass
    return int(n)


def right(n, N, X, Y, tol=tol):
    NXY = np.vstack([N, X, Y]).T
    try:
        NXY = NXY[np.isclose(X, min(X[X>(X[n] + tol)]), tol)]
        NXY = NXY[np.argmin((NXY[:, 2] -Y[n])**2)]
        n = NXY[0]
    except ValueError:
        pass
    return int(n)

def up(n, N, X, Y, tol=tol):
    NXY = np.vstack([N, X, Y]).T
    try:
        NXY = NXY[np.isclose(Y, min(Y[Y>(Y[n] + tol)]), tol)]
        NXY = NXY[np.argmin((NXY[:, 1] - X[n])**2)]
        n = NXY[0]
    except ValueError:
        pass
    return int(n)


def down(n, N, X, Y, tol=tol):
    NXY = np.vstack([N, X, Y]).T
    try:
        NXY = NXY[np.isclose(Y, max(Y[Y<(Y[n] - tol)]), tol)]
        NXY = NXY[np.argmin((NXY[:, 1] - X[n])**2)]
        n = NXY[0]
    except ValueError:
        pass
    return int(n)