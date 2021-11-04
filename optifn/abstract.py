from abc import ABC, abstractmethod
from typing import List

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


class OptimizationFunction(ABC):
    @abstractmethod
    def name(self): str

    @abstractmethod
    def type(self): str

    @abstractmethod
    def description(self): str

    @abstractmethod
    def __call__(self, *args, **kwargs): float

    @abstractmethod
    def eval_limits(self, *args, **kwargs): List

    @abstractmethod
    def global_minimum(self): float

    def plot_2d(self):
        limits = self.eval_limits(dims=2)
        low = limits[0][0]
        high = limits[0][1]
        x1 = x2 = np.arange(low, high, (high - low) / 100.0)
        X1, X2 = np.meshgrid(x1, x2)
        X = np.vstack([X1.flatten(), X2.flatten()]).T
        Y = self(X, c=0.2 * np.pi).reshape(X1.shape)
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X1, X2, Y, cmap=cm.coolwarm)
        plt.tight_layout()
        plt.show()


class ManyLocalMinima(OptimizationFunction, ABC):
    def type(self):
        return "Many Local Minima"


class BowlShaped(OptimizationFunction, ABC):
    def type(self):
        return "Bowl Shaped"


class PlateShaped(OptimizationFunction, ABC):
    def type(self):
        return "Plate Shaped"


class ValleyShaped(OptimizationFunction, ABC):
    def type(self):
        return "Valley Shaped"
