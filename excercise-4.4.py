import random
import Cdf, Pmf
import myplot


def paretovariate(a, x):
    data = [random.paretovariate(a)*x for i in range(500000)]

    return data

# print(paretovariate(1.7, 100))

pmf = Pmf.MakePmfFromList(paretovariate(1.7, 100))
cdf = Cdf.MakeCdfFromPmf(pmf)


myplot.Cdf(cdf)

myplot.show()