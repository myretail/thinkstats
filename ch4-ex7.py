import Cdf
import erf

def overNormal(value, m, s):
   return 1 - erf.NormalCdf(value, mu=m, sigma=s)

def underNormal(value, m, s):
   return erf.NormalCdf(value, mu=m, sigma=s)

print (overNormal(115, 100, 15))
print (overNormal(130, 100, 15))
print (overNormal(145, 100, 15))

print ("全球60亿人中，智商超过190的人的个数是：",overNormal(190, 100, 15) * 6000000000)
