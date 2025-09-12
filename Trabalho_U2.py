import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import time as tm

class livro:     #criando a classe livro
  def __init__(self,titulo,autor,genero,disponiveis):
    self.titulo = titulo
    self.autor = autor
    self.genero = genero
    self.disponiveis = disponiveis

  def __str__(self):  #função para mostrar os dados dos livros
    return f"-- {self.titulo} de {self.autor}, genero: {self.genero}, disponiveis: {self.disponiveis}"

  def adicionar_livro():  #função para adicionar livro
    titulo = input("Qual o nome do livro?\n> ")
    autor = input("Quem é o autor do livro?\n> ")
    genero = input("Qual genero do livro?\n> ")
    disponiveis = input("Tem quantas unidades?\n> ")
    novo_livro = livro(titulo, autor, genero, disponiveis)
    return novo_livro

#lista pré definida e alteravel
biblioteca = [livro("Dom Casmurro", "Machado de Assis", "Romance/Realismo", "6"), livro("O Senhor dos Anéis: A Sociedade do Anel", "J. R. R. Tolkien", "Fantasia", "1"), livro("1984", "George Orwell", "Distopia/Ficção", "12"), livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Fábula/Ficção", "4"), livro("Orgulho e Preconceito", "Jane Austen", "Romance", "9")]

acao = "0"  #chamado inicial da variavel acao

while acao != "5":   #inicio do loop while

    #seleção de ação
  acao = input(">---------------------------<\nO que deseja fazer?\n1 - Adicionar livro.\n2 - Mostrar lista de livros.\n3 - Procurar livro.\n4 - Gráfico por Gênero.\n5 - Fechar.\n> ")
  print(">---------------------------<")

  if acao == "1":    #adicionar livro à biblioteca
    novo = livro.adicionar_livro()
    biblioteca.append(novo)

  elif acao == "2":  #mostrar livros da biblioteca
    for l in biblioteca:
      print(l)

  elif acao == "3":  #procurar um livro específico
    busca = input("Qual o título do livro?\n> ")
    for livro in biblioteca:
      if busca.lower() in livro.titulo.lower():
        print(f"-- {livro.titulo}, {livro.autor}, {livro.genero}  - {livro.disponiveis} disponiveis")

  elif acao == "4":  #mostrar o grafico de generos
    gen = []

    #separar generos
    for livro in biblioteca:
        gen.extend(livro.genero.split("/"))

    #Conta os generos
    numero_generos = Counter(gen)

    #listas planas
    x = list(numero_generos.keys())      #gêneros (nomes)
    y = list(numero_generos.values())    #quantidades (números)

    #posições numéricas para o eixo X
    numeros_x = np.arange(len(x))

    #gráfico
    fig, ax = plt.subplots()
    ax.bar(numeros_x, y)
    ax.set_xticks(numeros_x)
    ax.set_xticklabels(x, rotation=45, ha="right")

    #mostra o gráfico
    plt.show()

    #fechando grafico
    print(f"\rFechando em 3", end="")
    tm.sleep(1)
    print(f"\rFechando em 2", end="")
    tm.sleep(1)
    print(f"\rFechando em 1", end="")
    tm.sleep(1)
    plt.close()

  elif acao != "5":   #caso a opção selecionada seja invalida
    print("Digite uma opção válida.")

else:    #encerrando o programa
  print("Programa encerrado com sucesso!")
