valor = float(input())
a = (valor//100)
b = ((valor-(a*100))//50)
c = ((valor-(a*100)-(b*50))//20)
d = ((valor-(a*100)-(b*50)-(c*20))//10)
e = ((valor-(a*100)-(b*50)-(c*20)-(d*10))//5)
f = ((valor-(a*100)-(b*50)-(c*20)-(d*10)-(e*5))//2)
g = ((valor-(a*100)-(b*50)-(c*20)-(d*10)-(e*5)-(f*2))//1)
h = ((valor-(a*100)-(b*50)-(c*20)-(d*10)-(e*5)-(f*2)-(g*1))//0.5)
i = ((valor-(a*100)-(b*50)-(c*20)-(d*10)-(e*5)-(f*2)-(g*1)-(h*0.5))//0.25)
j = ((valor-(a*100)-(b*50)-(c*20)-(d*10)-(e*5)-(f*2)-(g*1)-(h*0.5)-(i*0.25))//0.10)
k = ((valor-(a*100)-(b*50)-(c*20)-(d*10)-(e*5)-(f*2)-(g*1)-(h*0.5)-(i*0.25)-(j*0.10))//0.05)
l = ((valor-(a*100)-(b*50)-(c*20)-(d*10)-(e*5)-(f*2)-(g*1)-(h*0.5)-(i*0.25)-(j*0.10)-(k*0.05))/0.01)
print("NOTAS:")
print("{:.0f}".format(a),"nota(s) de R$ 100.00")
print("{:.0f}".format(b),"nota(s) de R$ 50.00")
print("{:.0f}".format(c),"nota(s) de R$ 20.00")
print("{:.0f}".format(d),"nota(s) de R$ 10.00")
print("{:.0f}".format(e),"nota(s) de R$ 5.00")
print("{:.0f}".format(f),"nota(s) de R$ 2.00")
print("MOEDAS:")
print("{:.0f}".format(g),"moeda(s) de R$ 1.00")
print("{:.0f}".format(h),"moeda(s) de R$ 0.50")
print("{:.0f}".format(i),"moeda(s) de R$ 0.25")
print("{:.0f}".format(j),"moeda(s) de R$ 0.10")
print("{:.0f}".format(k),"moeda(s) de R$ 0.05")
print("{:.0f}".format(l),"moeda(s) de R$ 0.01")