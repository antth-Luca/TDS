# Valor da máquina = R$ 70.000,00
# Após 10 anos, vende-se por R$ 5.000,00
# Trabalha 8h/dia
# Depreciação 10% linear (igual todo ano)

# 1. Colunas: Ano | Deprec. | Fund. Deprec. | Valor atual;
# 2. Linhas: De zero até total de anos.

# 1. Primeiro e último do [ Valor atual ];
# 2. Primiro - último = diferença;
# 3. Depreciação de cada ano recebe a diferença;
# 4. Preencher os demais campos de [ Valor atual ], reduzindo a diferença;
# 5. Fundo deprec. recebe ano * diferença.

from math import ceil
import os
import webbrowser

def limpar_valor_monet(valor_monet):
    if ' ' in valor_monet:
        valor_monet = valor_monet.replace(' ', '')
    if 'R$' in valor_monet.upper():
        valor_monet = valor_monet.replace('R$', '')
    if ',' in valor_monet:
        valor_monet = valor_monet.replace(',', '.')
    return float(valor_monet)


def limpar_valor_tempo(valor_tempo):
    valor_tempo = valor_tempo.upper()
    if ' ' in valor_tempo:
        valor_tempo = valor_tempo.replace(' ', '')
    if 'ANOS' in valor_tempo:
        valor_tempo = valor_tempo.replace('ANOS', '')
    if 'A' in valor_tempo:
        valor_tempo = valor_tempo.replace('A', '')
    if ',' in valor_tempo:
        valor_tempo = valor_tempo.replace(',', '.')
    return float(valor_tempo)


def criar_tabela_depreciacao(tempo_anos, valor_pago, valor_vendido):
    # Cálculo da depreciação anual
    deprec_anual = valor_pago - valor_vendido
    
    deprec = deprec_anual / tempo_anos
    
    # Cabeçalhos da tabela
    headers = ["Ano", "Deprec.", "Fund. Deprec.", "Valor Atual"]
    
    # Iniciando a tabela HTML
    html_table = '<table class="table table-sm table-dark table-striped table-hover">\n'
    html_table += "    <tr>\n"
    
    # Criando cabeçalhos
    for header in headers:
        html_table += f"    <th>{header}</th>\n"
    html_table += "    </tr>\n"
    html_table += "  </thead>\n"
    html_table += "  <tbody>\n"
    
    # Montando as linhas da tabela
    for ano in range(0, ceil(tempo_anos) + 1):
        if ano != 0:
            fundo_deprec = deprec * ano
            valor_atual = valor_pago - fundo_deprec
            
            html_table += "  <tr>\n"
            html_table += f"    <td>{ano}</td>\n"
            html_table += f"    <td>{deprec:.2f}</td>\n"
            html_table += f"    <td>{fundo_deprec:.2f}</td>\n"
            html_table += f"    <td>{valor_atual:.2f}</td>\n"
            html_table += "  </tr>\n"
        
        else:
            html_table += "  <tr>\n"
            html_table += f"    <td>{ano}</td>\n"
            html_table += f"    <td> --- </td>\n"
            html_table += f"    <td> --- </td>\n"
            html_table += f"    <td>{valor_pago:.2f}</td>\n"
            html_table += "  </tr>\n"
    
    # Fechando a tabela
    html_table += "</table>"
    
    return html_table


def salvar_html(nome_arquivo, conteudo_html):
    html_completo = f"""
    <html lang="pt-br" data-bs-theme="dark">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container-fluid mt-5">
            <div class="row">
                <div class="col-12 col-md-8 col-lg-6">
                    <h2 class="text-center">Tabela de Depreciação</h2>
                    {conteudo_html}
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    with open(nome_arquivo, "w") as file:
        file.write(html_completo)
    caminho_absoluto = os.path.abspath(nome_arquivo)
    print(f"Arquivo '{nome_arquivo}' salvo com sucesso em: {caminho_absoluto}")
    return caminho_absoluto


def main():
    pagou = str(input('Quanto foi pago na compra?\n> R$ '))
    pagou = limpar_valor_monet(pagou)

    vendeu = str(input('Por quanto foi vendido?\n> R$ '))
    vendeu = limpar_valor_monet(vendeu)

    ano = str(input('Quantos anos \n> '))
    ano = limpar_valor_tempo(ano)

    tabela_html = criar_tabela_depreciacao(ano, pagou, vendeu)

    # Salvar a tabela HTML em um arquivo
    nome_arquivo = "tabela_depreciacao.html"
    caminho_html = salvar_html(nome_arquivo, tabela_html)

    # Abrir o arquivo HTML no navegador
    webbrowser.open(f"file://{caminho_html}")

# MAIN
if __name__ == '__main__':
    main()