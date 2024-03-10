import numpy as np
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
from scipy.stats import mode

dados = [19.00, 11.00, 26.24, 53.00, 19.00, 2.25, 38.88, 10.25, 54.38, 10.00,
             35.00, 17.50, 12.38, 26.02, 8.63, 15.00, 44.25, 19.50, 17.63, 9.75,
             9.00, 12.50, 29.50, 79.38, 36.25, 22.63, 20.38, 39.88, 34.63, 10.38,
             31.38, 10.25, 33.25, 39.00, 49.38, 32.13, 30.63, 9.63, 30.63, 34.50]

def create_frequency_table(dados):
    # Ordenar os dados para ROL
    dados_ordenados = sorted(dados)

    # Calcular o número de classes usando o critério de Sturges
    n = len(dados)
    k = round(1 + 3.322 * np.log10(n))

    # Criar os intervalos de classe
    min_val = min(dados)
    max_val = max(dados)
    range_val = max_val - min_val
    bin_width = round(range_val / k)  # AMPLITUDE DE INTERVALO
    bins = np.arange(min_val, max_val + bin_width, bin_width)

    # Calcular as frequências
    hist, edges = np.histogram(dados, bins=bins)
    frequencia_absoluta = hist
    frequencia_relativa = hist / n
    frequencia_relativa_percentual = frequencia_relativa * 100
    frequencia_acumulada = np.cumsum(hist)
    frequencia_relativa_acumulada = np.cumsum(frequencia_relativa)
    frequencia_relativa_acumulada_percentual = frequencia_relativa_acumulada * 100

    # Calcular a média, moda e mediana dos dados
    media = np.mean(dados)
    mediana = np.median(dados)
    moda_result = mode(dados)
    modas = moda_result.mode
    frequencias = moda_result.count

    # Montar a tabela de distribuição de frequência
    tabela_freq = pd.DataFrame({
        'Intervalo': [f"{edges[i]:.2f} - {edges[i+1]:.2f}" for i in range(len(edges)-1)],
        'Freq. Absoluta': frequencia_absoluta,
        'Freq. Relativa': np.round(frequencia_relativa, 4),
        'Freq. Relativa (%)': np.round(frequencia_relativa_percentual, 2),
        'Freq. Acumulada': frequencia_acumulada,
        'Freq. Rel. Acumulada': np.round(frequencia_relativa_acumulada, 4),
        'Freq. Rel. Acum. (%)': np.round(frequencia_relativa_acumulada_percentual, 2)
    })

    return bins, frequencia_absoluta, tabela_freq, dados_ordenados, k, media, mediana, modas, frequencias

def save_table(tabela, filename='tabela.png'):
    fig, ax = plt.subplots(figsize=(12, 2))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=tabela.values, colLabels=tabela.columns, loc='center', cellLoc='center')

    plt.savefig(filename, dpi=300)
    plt.close()

if __name__ == "__main__":

    bins, frequencia_absoluta, tabela_freq, dados_ordenados, k, media, mediana, modas, frequencias = create_frequency_table(dados)
    
    # Tabela ROL
    tabela_rol = pd.DataFrame(dados_ordenados, columns=['Dados em ROL'])
    print("Tabela ROL:")
    print(tabulate(tabela_rol, headers='keys', tablefmt='pretty', showindex=False))
    print(f"Número de classes: {k}")
    
    # Tabela de Distribuição de Frequência
    print("\nTabela de Distribuição de Frequência:")
    print(tabulate(tabela_freq, headers='keys', tablefmt='pretty', showindex=False))
    print(f"\nMédia dos dados: {media:.2f}")
    print(f"Mediana dos dados: {mediana:.2f}")
    print(f"Moda dos dados: {modas} (Frequência: {frequencias})")
    save_table(tabela_freq, 'tabela_freq.png')