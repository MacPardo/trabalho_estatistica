from math import sqrt

def media(lista):
	soma = 0
	for i in lista:
		soma += i
	return soma/len(lista)

def desvio_padrao(lista):
	mediav = media(lista)
	somatorio = 0
	for i in lista:
		somatorio += (i - mediav) ** 2
	somatorio /= len(lista)
	somatorio = sqrt(somatorio)
	return somatorio

def coeficiente_variacao(lista):
	return desvio_padrao(lista) / media(lista) * 100

def print_sem_intervalo(matriz):
	for i in range(8 * 2 + 3): print('-',end='')
	print()
	for i in matriz:
		print('|' + str(i[0]) + '\t|' + str(i[1]) + '\t|')
	for i in range(8 * 2 + 3): print('-',end='')
	print()

def media_sem_intervalo(matriz):
	total = 0
	n = 0
	for i in matriz:
		total += i[0] * i[1]
		n += i[1]
	return total / n

def desvio_padrao_sem_intervalo(matriz):
	_media = media_sem_intervalo(matriz)
	soma_q = 0
	soma_fi = 0
	for i in matriz:
		soma_q += (i[0] - _media) ** 2 * i[1]
		soma_fi += i[1]
	return sqrt(soma_q / soma_fi)

def coeficiente_variacao_sem_intervalo(matriz):
	return desvio_padrao_sem_intervalo(matriz) / media_sem_intervalo(matriz) * 100

def media_com_intervalo(matriz):
	somaxf = 0
	somaf = 0
	for i in matriz:
		somaf += i[2]
		somaxf += (i[0] + i[1]) / 2 * i[2]
	return somaxf / somaf

def desvio_padrao_com_intervalo(matriz):
	_media = media_sem_intervalo(matriz)
	soma_q = 0
	soma_fi = 0
	for i in matriz:
		soma_q += (  ((i[0] + i[1])/2) - _media) ** 2 * i[2]
		print((  ((i[0] + i[1])/2) - _media) ** 2 * i[2])
		soma_fi += i[2]
	print(soma_q,soma_fi)
	return sqrt(soma_q / soma_fi)

def main():
	return 0

if __name__ == '__main__':
	main()
