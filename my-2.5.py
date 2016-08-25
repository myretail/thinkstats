import Pmf

def PmfMean(pmf):
    return sum([value * pmf.Prob(value) for value in pmf.Values()])

def PmfVar(pmf):
    mean = PmfMean(pmf)
    return sum([pmf.Prob(value)*(value - mean)**2 for value in pmf.Values()])

if __name__ == '__main__':
    pmf  = Pmf.MakePmfFromList([1,3,45,78,18,46,4,9,12])
    print("mean:", PmfMean(pmf))
    print("Var:", PmfVar(pmf))
    print("使用内建函数计算，结果应该和自己编写的函数返回值相同")
    print ("Mean:" , pmf.Mean())
    print ("Var:", pmf.Var())