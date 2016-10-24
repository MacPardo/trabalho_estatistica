from math import sqrt
from copy import deepcopy
import os

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
	print('--------------')
	for i in matriz:
		print(str(i[0]) + '--|' + str(i[1]) + '\t| ' + str(i[2]))
	print('--------------')

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')
	

def main():
	while True:
		clear_screen()
		print("Você sempre tem que dar um enter depois de inserir qualquer dado.")
		print("1 - Inserir dados brutos")
		print("2 - Inserir dados sem intervalo de classe")
		print("3 - Inserir dados com intervalo de classe")
		print("4 - Sair")

		choice = int(input())
		values = []

		if choice == 1:
			data_quatity = int(input("quantidade de dados a serem inseridos: "))
			for i in range(data_quatity):
				print(values)
				number = float(input('insira: '))
				values.append(number)
			values.sort()
			while True:
				clear_screen()
				print(values)
				print()
				print('1 - Media')
				print('2 - Desvio Padrão')
				print('3 - Coeficiente de Variação')
				print('4 - Voltar para o menu')

				escolha = int(input())
				
				if escolha == 1:
					print('%.2f' % media(values))
					input('(Enter)')

				elif escolha == 2:
					print('%.2f' % desvio_padrao(values))
					input('(Enter)')

				elif escolha == 3:
					print('%.2f' % coeficiente_variacao(values))
					input('(Enter)')

				elif escolha == 4: break

		elif choice == 2:
			class_quantity = int(input("Quantidade de classes: "))

			for i in range(class_quantity):
				classe = []
				classe.append(float(input('classe: ')))
				classe.append(float(input('frequência da classe: ')))
				values.append(classe)

			while True:
				clear_screen()
				print_sem_intervalo(values)
				print()
				print('1 - Media')
				print('2 - Desvio Padrão')
				print('3 - Coeficiente de Variação')
				print('4 - Voltar para o menu')

				escolha = int(input())
				
				if escolha == 1:
					print('%.2f' % media_sem_intervalo(values))
					input('(Enter)')

				elif escolha == 2:
					print('%.2f' % desvio_padrao_sem_intervalo(values))
					input('(Enter)')

				elif escolha == 3:
					print('%.2f' % coeficiente_variacao_sem_intervalo(values))
					input('(Enter)')

				elif escolha == 4: break

		elif choice == 3:
			class_quantity = int(input('Quantidade de classes: '))
			class_interval = int(input('Intervalo de classe: '))
			class_bottom = int(input('Menor valor da primeira classe: '))

			for i in range(class_quantity):
				classe = []
				classe.append(class_bottom + class_interval * i)
				classe.append(class_bottom + (class_interval * (i + 1)))
				classe.append(float(input('frequência da classe %.2f|--%.2f: ' % (classe[0], classe[1]) )))
				values.append(classe)

			while True:
				clear_screen()
				print_com_intervalo(values)
				print()
				print('1 - Media')
				print('2 - Desvio Padrão')
				print('3 - Coeficiente de Variação')
				print('4 - Voltar para o menu')

				escolha = int(input())
				
				if escolha == 1:
					print('%.2f' % media_com_intervalo(values))
					input('(Enter)')

				elif escolha == 2:
					print('%.2f' % desvio_padrao_com_intervalo(values))
					input('(Enter)')

				elif escolha == 3:
					print('%.2f' % coeficiente_variacao_com_intervalo(values))
					input('(Enter)')

				elif escolha == 4: break
			
		elif choice == 4: break


if __name__ == '__main__': main()
