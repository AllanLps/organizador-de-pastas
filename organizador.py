import os
import shutil

from categorias import CATEGORIAS

# Função para encontrar a categoria com base na extensão do arquivo, se encontrar retorna a categoria, caso contrário retorna "Outros"
def encontrar_categoria(extensao):
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria
    return "Outros"

# Função para listar os arquivos em uma pasta, retorna uma lista de arquivos encontrados na pasta, ignorando subpastas e diretórios. A função utiliza a função os.listdir para obter os itens na pasta e verifica se cada item é um arquivo usando os.path.isfile. Se for um arquivo, ele é adicionado à lista de arquivos que será retornada no final.
def listar_arquivos(pasta):
    arquivos = []
    for item in os.listdir(pasta):
        caminho = os.path.join(pasta, item)
        if os.path.isfile(caminho):
            arquivos.append(item)
    return arquivos

def simular_organizar(pasta):
    arquivos = listar_arquivos(pasta)
    contagem = {}
    linhas = []
    for nome in arquivos:
        extensao = os.path.splitext(nome)[1].lower()
        categoria = encontrar_categoria(extensao)
        contagem[categoria] = contagem.get(categoria, 0) + 1
        linhas.append(f"{nome} -> {categoria}/")         
    
    linhas.append(f"\n── Resumo ──────────────")
    linhas.append(f"Total: {len(arquivos)} arquivos")
    for categoria, total in contagem.items():
        linhas.append(f"  {categoria}: {total}")
        
    return "\n".join(linhas), contagem

# Função para organizar os arquivos em uma pasta, a função recebe o caminho da pasta como argumento e realiza as seguintes etapas:
# 1. Lista os arquivos na pasta usando a função listar_arquivos.
# 2. Para cada arquivo, obtém a extensão e encontra a categoria correspondente usando a função econtrar_categorias.
# 3. Cria a pasta de destino para a categoria, se ela não existir.
def organizar(pasta):
    arquivos = listar_arquivos(pasta)

    for nome in arquivos:
        extensao = os.path.splitext(nome)[1].lower()
        categoria = encontrar_categoria(extensao)

        pasta_destino = os.path.join(pasta, categoria)
        os.makedirs(pasta_destino, exist_ok=True)

        origem = os.path.join(pasta, nome)
        destino = os.path.join(pasta_destino, nome)

        if os.path.exists(destino):
            base, ext = os.path.splitext(nome)
            destino = os.path.join(pasta_destino, f"{base}_copia{ext}")
            contador = 1
            while os.path.exists(destino):
                destino = os.path.join(pasta_destino, f"{base}_copia{contador}{ext}")
                contador += 1

        shutil.move(origem, destino)
        print(f"{nome} -> {categoria}/")
        
