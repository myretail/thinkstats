import random
import Cdf, Pmf
import myplot


def paretovariate(a, x):
    data = [random.paretovariate(a)*x for i in range(50)]

    return data

print(paretovariate(1.7, 100))

pmf = Pmf.MakePmfFromList(paretovariate(1.7, 100))
cdf = Cdf.MakeCdfFromPmf(pmf)


myplot.Cdf(cdf,complement=True, xscale='linear', yscale='log')

myplot.Save(root='excercise 4.3',
            title='CCDF of 4.3',
            xlabel='Num',
            ylabel='CCDF')