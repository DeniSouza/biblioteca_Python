biblioteca = []

class Livro:

  def __init__(self, titulo, autor, genero, quantidade):
    self.titulo = titulo
    self.autor = autor
    self.genero = genero
    self.quantidade = quantidade

  def __str__(self):
    return f"Título: '{self.titulo}' | Autor: {self.autor} | Gênero: {self.genero} | Qtd: {self.quantidade}\n"

@staticmethod
def cadastrar_livro():
    titulo = input("Título do livro: ").strip()
    autor = input("Autor: ").strip()
    genero = input("Gênero: ").strip()

    while True:
      try:
        quantidade = int(input("Quantidade disponível: "))
        if quantidade < 0:
          print("A quantidade não pode ser negativa.")
          continue
        else:
          break
      except ValueError:
        print("Por favor, digite a quantidade corretamente.")

    novo_livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro)
    print(f"Livro '{titulo}' cadastrado com sucesso! \n")
    return novo_livro

@staticmethod
def listar_livros():
    if not biblioteca:
      print("\nNenhum livro cadastrado na biblioteca.\n")
      return
    print("\n--- Todos os Livros Cadastrados ---")
    for livro in biblioteca:
      print(livro)

@staticmethod
def listar_titulo(termo_busca):
    if not biblioteca:
      print("\nNenhum livro cadastrado na biblioteca.")
      return

    encontrados = [
        livro
        for livro in biblioteca
        if termo_busca.lower() in livro.titulo.lower()
        or termo_busca.lower() in livro.autor.lower()
        or termo_busca.lower() in livro.genero.lower()
    ]

    if encontrados:
      print(f"\n--- Resultado da busca por: '{termo_busca}' ---")
      for livro in encontrados:
        print(livro)
    else:
      print(
          f"\nMensagem: Nenhum livro foi encontrado com o termo '{termo_busca}'."
      )