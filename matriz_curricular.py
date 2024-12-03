# Programa que recebe um arquivo de texto contendo uma matriz curricular
# sem quebra de linhas e sem delimitadores e gera um novo arquivo .csv
# utilizando ponto-e-vírgula como separador

# Os dados para o arquivo são provenientes da ementa da UNIVESP, e o programa foi necessário
# para que a matriz curricular pudesse ser manipulada em formato de planilhas do Google



import re

#PROCESSAMENTO DO ARQUIVO

#Solicita que o usuário informe o caminho do arquivo contendo a string a ser
#formatada e salva o conteúdo em uma variável
def ler_arquivo():
  caminho = input("Informe o caminho do arquivo .txt: ")
  try:
    with open(caminho, 'r') as arquivo:
      dados = arquivo.read()
      return dados

  except FileNotFoundError:
    print("Arquivo não encontrado.")

  except Exception as e:
    print(f"Ocorreu um erro: {e}")


#Grava o arquivo formatado
def salvar_arquivo(conteudo):
  nome_arquivo = input("Espeficique um nome para o novo arquivo: ")+".csv"
  try:
    with open(nome_arquivo, 'w') as arquivo_saida:
      arquivo_saida.write(conteudo)
  except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo: {e}")



#PROCESSAMENTO DOS DADOS

#Recebe a String com os dados e quebra em uma linha por disciplina
def string_para_linhas (string_de_dados):
  padrao_cod = r"[A-Z]{3,}[0-9]{3,}" #REGEX código da disciplina
  disciplinas = re.split(f"(?={padrao_cod})",string_de_dados) #Quebra a string em linhas
  linhas = "\n".join(disciplinas) #Junta as linhas
  return linhas


#Formata cada linha em colunas delimitadas por ponto-e-virgula e adiciona
#um cabeçalho
def delimita_com_ponto_e_virgula (lista_de_disciplinas):
  saida = "CÓD;DISCIPLINA;CH;SEM;BIM"

  padrao_linha = r"([A-Z]{3,}\d{3})\s+(.*?)\s+(\d{2})\s+(\d)\s+(\d)"

  for linha in lista_de_disciplinas.split('\n'):
    match = re.match(padrao_linha, linha)

    if match:
      codigo = match.group(1)
      nome = match.group(2)
      carga_horaria = match.group(3)
      semestre = match.group(4)
      bimestre = match.group(5)

      linha_formatada = f"{codigo};{nome};{carga_horaria};{semestre};{bimestre}"
      saida += '\n' + linha_formatada

  return saida


def formata_arquivo():
  dados = ler_arquivo()
  linhas = string_para_linhas(dados)
  string_formatada = delimita_com_ponto_e_virgula(linhas)
  salvar_arquivo(string_formatada)

formata_arquivo()
