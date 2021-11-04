import numpy as np


def hart6(x,
          alpha=np.asarray([1.0, 1.2, 3.0, 3.2]),
          P=10 ** -4 * np.asarray([[1312, 1696, 5569, 124, 8283, 5886],
                                   [2329, 4135, 8307, 3736, 1004, 9991],
                                   [2348, 1451, 3522, 2883, 3047, 6650],
                                   [4047, 8828, 8732, 5743, 1091, 381]]),
          A=np.asarray([[10, 3, 17, 3.50, 1.7, 8],
                        [0.05, 10, 17, 0.1, 8, 14],
                        [3, 3.5, 1.7, 10, 17, 8],
                        [17, 8, 0.05, 10, 0.1, 14]])):
    """The six dimensional Hartmann function is defined on the unit hypercube.

    It has six local minima and one global minimum f(x*) = -3.32237 at
    x* = (0.20169, 0.15001, 0.476874, 0.275332, 0.311652, 0.6573).

    More details: <http://www.sfu.ca/~ssurjano/hart6.html>
    """
    assert x.shape[-1] == 6
    return -np.sum(alpha * np.exp(-np.sum(A * (np.array(x) - P) ** 2, axis=1)))


def ackley(x: np.ndarray, a=20, b=0.2, c=2 * np.pi):
    """
    :param x: c(x1, x2, ..., xd)
    :param a: constant (optional), with default value 20
    :param b: constant (optional), with default value 0.2
    :param c: constant (optional), with default value 2*pi
    :return: float or arr-like
    """
    d = x.shape[-1]
    sum1 = np.sum(np.power(x, 2.0), axis=-1)
    sum2 = np.sum(np.cos(c * x), axis=-1)

    term1 = -a * np.exp(-b * np.sqrt(sum1 / d))
    term2 = -np.exp(sum2 / d)

    return term1 + term2 + a + np.exp(1)


def bukin6(x: np.ndarray):
    """
    The function is usually evaluated on the rectangle x1 ∈ [-15, -5], x2 ∈ [-3, 3]
    :param x: 2-dim input
    :return: the y-value (float)
    """
    assert x.shape[-1] == 2
    x1 = x.T[0]
    x2 = x.T[1]

    term1 = 100 * np.sqrt(np.abs(x2 - 0.01 * x1 ** 2))
    term2 = 0.01 * np.abs(x1 + 10)
    return term1 + term2


def cross_in_tray(x: np.ndarray):
    """
    The function is usually evaluated on the square xi ∈ [-10, 10], for all i = 1, 2
    :param x: 2-dim numpy array
    :return: the y-value (float)
    """
    assert x.shape[-1] == 2
    x1 = x.T[0]
    x2 = x.T[1]

    fact1 = np.sin(x1) * np.sin(x2)
    fact2 = np.exp(np.abs(100 - np.sqrt(x1 ** 2 + x2 ** 2) / np.pi))

    return -0.0001 * (np.abs(fact1 * fact2) + 1) ** 0.1


def levy(x: np.ndarray):
    """
    The function is usually evaluated on the hypercube xi ∈ [-10, 10], for all i = 1, …, d.
    :param x: c(x1, x2, ..., xd)
    :return: the y-value (float)
    """
    w = 1 + (x - 1) / 4  # same shape as x

    term1 = (np.sin(np.pi * w.T[0])) ** 2
    term3 = (w.T[-1] - 1) ** 2 * (1 + 1 * (np.sin(2 * np.pi * w.T[-1])) ** 2)

    wi = w.T[:-1]
    sum = np.sum((wi - 1) ** 2 * (1 + 10 * (np.sin(np.pi * wi + 1)) ** 2))

    return term1 + sum + term3


def bohachevsky(x: np.ndarray):
    """
    The Bohachevsky functions all have the same similar bowl shape.
    The functions are usually evaluated on the square xi ∈ [-100, 100], for all i = 1, 2.
    :param x: 2-dimensional
    :return: float
    """
    assert x.shape[-1] == 2
    x1 = x.T[0]
    x2 = x.T[1]

    term1 = x1 ** 2
    term2 = 2 * x2 ** 2
    term3 = -0.3 * np.cos(3 * np.pi * x1)
    term4 = -0.4 * np.cos(4 * np.pi * x2)

    return term1 + term2 + term3 + term4 + 0.7


def matyas(x: np.ndarray):
    """
    The Matyas function has no local minima except the global one.
    The function is usually evaluated on the square xi ∈ [-10, 10], for all i = 1, 2.
    Global minimum at (0, 0)
    :param x: 2-dimensional
    :return: float
    """
    assert x.shape[-1] == 2
    x1 = x.T[0]
    x2 = x.T[1]

    term1 = 0.26 * (x1 ** 2 + x2 ** 2)
    term2 = -0.48 * x1 * x2

    return term1 + term2


def three_hump(x: np.ndarray):
    """
    The function is usually evaluated on the square xi ∈ [-5, 5], for all i = 1, 2.
    global minimum at (0, 0)
    :param x: 2-dimensional
    :return: float
    """
    assert x.shape[-1] == 2
    x1 = x.T[0]
    x2 = x.T[1]

    term1 = 2 * x1 ** 2
    term2 = -1.05 * x1 ** 4
    term3 = x1 ** 6 / 6
    term4 = x1 * x2
    term5 = x2 ** 2

    return term1 + term2 + term3 + term4 + term5
