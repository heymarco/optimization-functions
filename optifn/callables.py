import numpy as np

from optifn.abstract import ManyLocalMinima, BowlShaped, PlateShaped, ValleyShaped
from optifn.functions import ackley, hart6, bukin6, cross_in_tray, levy, bohachevsky, matyas, three_hump


class Ackley(ManyLocalMinima):
    def description(self):
        return "The Ackley function is widely used for testing optimization algorithms. In its two-dimensional form, as shown in https://www.sfu.ca/~ssurjano/ackley.html, it is characterized by a nearly flat outer region, and a large hole at the centre. The function poses a risk for optimization algorithms, particularly hillclimbing algorithms, to be trapped in one of its many local minima."

    def __call__(self, *args, **kwargs):
        x = args[0]
        return ackley(x)

    def eval_limits(self, *args, **kwargs):
        dim = kwargs.get("dims", 2)
        limits = (-32.768, 32.768)
        return [limits for _ in range(dim)]

    def global_minimum(self):
        return 0.0


class Hartman6(ManyLocalMinima):
    def description(self):
        return "The 6-dimensional Hartmann function has 6 local minima."

    def __call__(self, *args, **kwargs):
        x = args[0]
        return hart6(x)

    def eval_limits(self, *args, **kwargs):
        dim = 6
        limits = (0.0, 1.0)
        return [limits for _ in range(dim)]

    def global_minimum(self):
        return -3.32237


class Bukin6(ManyLocalMinima):
    def description(self):
        return "The sixth Bukin function has many local minima, all of which lie in a ridge."

    def __call__(self, *args, **kwargs):
        x = args[0]
        return bukin6(x)

    def eval_limits(self, *args, **kwargs):
        return [(-15, 5), (-3, 3)]

    def global_minimum(self):
        return 0.0


class CrossInTray(ManyLocalMinima):
    def description(self):
        return "The Cross-in-Tray function has multiple global minima. It is shown here (https://www.sfu.ca/~ssurjano/crossit.html) with a smaller domain in the second plot, so that its characteristic cross will be visible."

    def __call__(self, *args, **kwargs):
        x = args[0]
        return cross_in_tray(x)

    def eval_limits(self, *args, **kwargs):
        dim = 2
        limits = (-10, 10)
        return [limits for _ in range(dim)]

    def global_minimum(self):
        return -2.06261


class Levy(ManyLocalMinima):
    def description(self):
        return "More information available under https://www.sfu.ca/~ssurjano/levy.html"

    def __call__(self, *args, **kwargs):
        x = args[0]
        return levy(x)

    def eval_limits(self, *args, **kwargs):
        dim = kwargs.get("dims", 2)
        limits = (-10, 10)
        return [limits for _ in range(dim)]

    def global_minimum(self):
        return 0.0


class Bohachevsky(BowlShaped):
    def description(self):
        return "The Bohachevsky functions all have the same similar bowl shape."

    def __call__(self, *args, **kwargs):
        x = args[0]
        return bohachevsky(x)

    def eval_limits(self, *args, **kwargs):
        dim = 2
        limits = (-100, 100)
        return [limits for _ in range(dim)]

    def global_minimum(self):
        return 0.0


class Matyas(PlateShaped):
    def description(self):
        return "The Matyas function has no local minima except the global one."

    def __call__(self, *args, **kwargs):
        x = args[0]
        return matyas(x)

    def eval_limits(self, *args, **kwargs):
        dim = 2
        limits = (-10, 10)
        return [limits for _ in range(dim)]

    def global_minimum(self):
        return 0.0


class ThreeHump(ValleyShaped):
    def description(self):
        return "The function has three local minima and a global minimum at (0, 0)."

    def __call__(self, *args, **kwargs):
        x = args[0]
        return three_hump(x)

    def eval_limits(self, *args, **kwargs):
        dim = 2
        limits = (-5, 5)
        return [limits for _ in range(dim)]

    def global_minimum(self):
        return 0.0


