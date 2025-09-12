#Armazena as notas em lista
notas = (input("Quais as notas do aluno? (separadas por virgula)"))

#Função para calcular a média
def somar_media(nota):

  #Separa as notas tornando-as float
  nota_float = [float(nota.strip()) for nota in notas.split(',')]

  soma = sum(nota_float)
  media = soma/len(nota_float)
  print(">-------------------------------<")
  print(f"As notas do aluno são: {nota}")
  print(f"A média do aluno é: {media}")
  return media

#"ativa" a função usando a lista "notas"
nota_aluno = somar_media(notas)

#detecta se passou ou reprovou
if nota_aluno >= 7:
  print("Parabéns, o aluno passou!")
  print(">-------------------------------<")
else:
  print("Infelizmente o aluno foi reprovado.")
  print(">-------------------------------<")
