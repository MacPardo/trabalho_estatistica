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

def sem_intervalo_to_lista(matriz):
	'''
	funçao que transforma uma matriz com intervalo de classe
	em uma lista de dados dispersos
	'''
	lista = []
	for i in matriz:
		for j in range(i[0]):
			lista.append(i[1])
	return lista

def print_sem_intervalo(matriz):
	for i in range(8 * 2 + 3): print('-',end='')
	print()
	for i in matriz:
		print('|' + str(i[0]) + '\t|' + str(i[1]) + '\t|')
	for i in range(8 * 2 + 3): print('-',end='')
	print()

def media_sem_intervalo(matriz):
	lista = sem_intervalo_to_lista(matriz)
	return media(lista)

def desvio_padrao_sem_intervalo(matriz):
	lista = sem_intervalo_to_lista(matriz)
	return desvio_padrao(lista)

def coeficiente_variacao_sem_intervalo(matriz):
	lista = sem_intervalo_to_lista(matriz)
	return coeficiente_variacao(lista)


def main():
	return 0

if __name__ == '__main__':
	main()
