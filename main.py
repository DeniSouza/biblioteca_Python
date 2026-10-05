import Models.Livro as ModuloLivro
import Models.Relatorios as Relatorios

def menu_principal():
    print("=== BEM-VINDO AO CEMITÉRIO DOS LIVROS ESQUECIDOS ===")
    print("=== 1 - Cadastrar livro                          ===")
    print("=== 2 - Listar todos os livros                   ===")
    print("=== 3 - Buscar um livro por título               ===")
    print("=== 4 - Gerar um relatório de gênero             ===")
    print("=== 5 - Gerar um relatório por autor             ===\n")

def main():
  menu_principal()
  while True:
    opcao = input("O que deseja fazer? Selecione uma opção ").strip()

    match opcao:
      case "1":
        ModuloLivro.cadastrar_livro()

      case "2":
        ModuloLivro.listar_livros()

      case "3":
        termo = input("\nDigite o título ou termo para buscar: ").strip()
        ModuloLivro.listar_titulo(termo)

      case "4":
        Relatorios.gerar_grafico_por_genero()
      
      case "5":
        Relatorios.gerar_grafico_por_autor()

      case "0":
        print("\n=== O CEMITÉRIO DOS LIVROS ESQUECIDOS AGRADECE SUA VISITA ===")
        break

      case _:
        print("\nOpção inválida! Por favor, escolha um número válido.")

if __name__ == "__main__":
    main()

   