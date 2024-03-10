import matplotlib.pyplot as plt
from main import create_frequency_table, dados

bins, frequencia_absoluta, _, _, _ = create_frequency_table(dados)

# Gerar o histograma
plt.figure(figsize=(10, 6))
plt.hist(dados, bins=bins, edgecolor='black', alpha=0.7, rwidth=0.8)
plt.title('Histograma dos Dados')
plt.xlabel('Intervalo')
plt.ylabel('Frequência Absoluta')
plt.xticks(bins)
plt.savefig('histograma.png', dpi=300)
plt.close()