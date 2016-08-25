import thinkstats
import sys, math

def Pumpkin():
    pumpkins = [1,1,1,3,3,591]
    print ("均值：",thinkstats.Mean(pumpkins),"磅")
    print ("方差：",thinkstats.Var(pumpkins))
    print ("标准差：",math.sqrt(thinkstats.Var(pumpkins)),"磅")

if __name__ == '__main__':
    Pumpkin()
