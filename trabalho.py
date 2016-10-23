from math import sqrt
from copy import deepcopy

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

def com_intervalo_to_sem_intervalo(matriz):
	matriz = deepcopy(matriz)
	for i in matriz:
		i[1] = (i[0] + i[1]) / 2
		i.pop(0)
	return matriz

def media_com_intervalo(matriz):
	matriz = com_intervalo_to_sem_intervalo(matriz)
	return media_sem_intervalo(matriz)

def desvio_padrao_com_intervalo(matriz):
	matriz = com_intervalo_to_sem_intervalo(matriz)
	return desvio_padrao_sem_intervalo(matriz)

def coeficiente_variacao_com_intervalo(matriz):
	return desvio_padrao_com_intervalo(matriz)/media_com_intervalo(matriz) * 100

def print_sem_intervalo(matriz):
	for i in range(8 * 2 + 3): print('-',end='')
	print()
	for i in matriz:
		print('|' + str(i[0]) + '\t|' + str(i[1]) + '\t|')
	for i in range(8 * 2 + 3): print('-',end='')
	print()

def print_com_intervalo(matriz):
	for i in matriz:
		print(str(i[0]) + '--|' + str(i[1]) + '\t' + str(i[2]))

lols = [[0,2,30],[2,4,40],[4,6,10],[6,8,15],[8,10,5]]
