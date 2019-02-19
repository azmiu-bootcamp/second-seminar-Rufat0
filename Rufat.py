sayi = int(input("Reqemleri daxil edin: "))
'''reqemler minniye qeder olanda program isdiir
10 minniyde sehf hesablayir :(
'''
a  = sayi //1000
b = (sayi - a*1000)//100
c = (sayi - a*1000 - b*100)//10
d = sayi - a*1000 - b*100 - c*10
print("Reqemlerin toplami: ", a+b+c+d)
