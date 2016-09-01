import random
import Cdf, Pmf
import myplot

data = [random.expovariate(1/32.6) for i in range(44)]
pmf = Pmf.MakePmfFromList(data)
cdf = Cdf.MakeCdfFromPmf(pmf)


print(data)

myplot.Cdf(cdf,complement=True, xscale='linear', yscale='log')

myplot.Save(root='excercise 4.1',
            title='CDF of 4.1',
            xlabel='Num',
            ylabel='CCDF')