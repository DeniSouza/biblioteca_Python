from collections import Counter
import matplotlib.pyplot as plt

# Importa a biblioteca declarada no módulo Livro
from Models.Livro import biblioteca


def gerar_grafico_por_genero():
  """Gera um gráfico de barras com a quantidade total de livros por gênero."""
  if not biblioteca:
    print("\nNão há livros cadastrados para gerar o gráfico.")
    return

  qtd_por_genero = Counter()
  for livro in biblioteca:
    qtd_por_genero[livro.genero] += livro.quantidade

  generos = list(qtd_por_genero.keys())
  quantidades = list(qtd_por_genero.values())

  plt.figure(figsize=(8, 5))
  plt.bar(generos, quantidades, color="skyblue", edgecolor="black")

  plt.title("Quantidade de Livros por Gênero na Biblioteca")
  plt.xlabel("Gênero")
  plt.ylabel("Quantidade Disponível")
  plt.grid(axis="y", linestyle="--", alpha=0.7)

  plt.tight_layout()
  plt.show()
  print("Relatório criado com sucesso\n")


def gerar_grafico_por_autor():
  """Gera um gráfico de barras com a quantidade total de livros por autor."""
  if not biblioteca:
    print("\nNão há livros cadastrados para gerar o gráfico.")
    return

  qtd_autor = Counter()
  for livro in biblioteca:
    qtd_autor[livro.autor] += livro.quantidade

  autores = list(qtd_autor.keys())
  quantidades = list(qtd_autor.values())

  plt.figure(figsize=(8, 5))
  plt.bar(autores, quantidades, color="salmon", edgecolor="black")

  plt.title("Quantidade de Livros por Autor na Biblioteca")
  plt.xlabel("Autor")
  plt.ylabel("Quantidade Disponível")
  plt.grid(axis="y", linestyle="--", alpha=0.7)

  plt.tight_layout()
  plt.show()
  print("Relatório criado com sucesso\n")