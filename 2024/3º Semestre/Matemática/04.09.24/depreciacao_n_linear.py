import os
import webbrowser

def limpar_valor_monet(valor_monet):
    valor_monet = valor_monet.replace(' ', '').replace('R$', '').replace(',', '.')
    return float(valor_monet)

def limpar_valor_tempo(valor_tempo):
    valor_tempo = valor_tempo.upper().replace(' ', '').replace('ANOS', '').replace('A', '').replace(',', '.')
    return float(valor_tempo)

def criar_tabela_depreciacao(tempo_anos, valor_pago, valor_vendido):
    # Cálculo do total a ser depreciado
    deprec_total = valor_pago - valor_vendido
    fundo_deprec = 0  # Fundo de depreciação inicial
    valor_atual = valor_pago  # Valor inicial da máquina
    
    # Cabeçalhos da tabela
    headers = ["Ano", "Taxa (%)", "Depreciação", "Fundo Depreciação", "Valor Atual"]
    
    # Iniciando a tabela HTML com classes do Bootstrap
    html_table = '<table class="table table-sm table-dark table-striped table-hover">\n'
    html_table += "  <thead class='thead-dark'>\n"
    html_table += "    <tr>\n"
    
    # Criando cabeçalhos
    for header in headers:
        html_table += f"      <th>{header}</th>\n"
    html_table += "    </tr>\n"
    html_table += "  </thead>\n"
    html_table += "  <tbody>\n"
    
    # Montando as linhas da tabela
    for ano in range(0, int(tempo_anos) + 1):
        if ano != 0:
            # A taxa cresce em 2% a cada ano, começando com 1%
            taxa = 1 + (ano - 1) * 2
            
            # Cálculo da depreciação para o ano com base na taxa
            deprec = (taxa / 100) * deprec_total
            fundo_deprec += deprec
            valor_atual -= deprec
            
            html_table += "    <tr>\n"
            html_table += f"      <td>{ano}</td>\n"
            html_table += f"      <td>{taxa:.2f}</td>\n"
            html_table += f"      <td>{deprec:.2f}</td>\n"
            html_table += f"      <td>{fundo_deprec:.2f}</td>\n"
            html_table += f"      <td>{valor_atual:.2f}</td>\n"
            html_table += "    </tr>\n"

        else:
            html_table += "  <tr>\n"
            html_table += f"    <td>{ano}</td>\n"
            html_table += f"    <td> --- </td>\n"
            html_table += f"    <td> --- </td>\n"
            html_table += f"    <td> --- </td>\n"
            html_table += f"    <td>{valor_pago:.2f}</td>\n"
            html_table += "  </tr>\n"
    
    # Fechando a tabela
    html_table += "  </tbody>\n"
    html_table += "</table>"
    
    return html_table

def salvar_html(nome_arquivo, conteudo_html):
    html_completo = f"""
    <!DOCTYPE html>
    <html lang="pt-br" data-bs-theme="dark">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container-fluid mt-5">
            <div class="row">
                <div class="col-12 col-md-8 col-lg-6 mx-auto">
                    <h2 class="text-center">Tabela de Depreciação Não Linear</h2>
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

    ano = str(input('Quantos anos?\n> '))
    ano = limpar_valor_tempo(ano)

    tabela_html = criar_tabela_depreciacao(ano, pagou, vendeu)

    # Salvar a tabela HTML em um arquivo
    nome_arquivo = "tabela_depreciacao_nao_linear.html"
    caminho_html = salvar_html(nome_arquivo, tabela_html)

    # Abrir o arquivo HTML no navegador
    webbrowser.open(f"file://{caminho_html}")

# MAIN
if __name__ == '__main__':
    main()
