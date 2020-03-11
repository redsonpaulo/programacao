#Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
#Entrada O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
#Saída Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
valor = int(input())
a = (valor//100)
b = ((valor-(a*100))//50)
c = ((valor-(a*100)-(b*50))//20)
d = ((valor-(a*100)-(b*50)-(c*20))//10)
e = ((valor-(a*100)-(b*50)-(c*20)-(d*10))//5)
f = ((valor-(a*100)-(b*50)-(c*20)-(d*10)-(e*5))//2)
g = ((valor-(a*100)-(b*50)-(c*20)-(d*10)-(e*5)-(f*2))//1)
print(valor)
print(a,"nota(s) de R$ 100,00")
print(b,"nota(s) de R$ 50,00")
print(c,"nota(s) de R$ 20,00")
print(d,"nota(s) de R$ 10,00")
print(e,"nota(s) de R$ 5,00")
print(f,"nota(s) de R$ 2,00")
print(g,"nota(s) de R$ 1,00")