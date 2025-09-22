import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar o dataset
df = pd.read_csv("Coffe_sales.csv")

print("RELATÓRIO")

def freq_table(col):
    abs_freq = df[col].value_counts()
    rel_freq = df[col].value_counts(normalize=True) * 100
    table = pd.DataFrame({
        "Frequência Absoluta": abs_freq,
        "Frequência Relativa (%)": rel_freq.round(2)
    })
    return table

def plot_freq(col, title=None):
    freq = df[col].value_counts()
    plt.figure(figsize=(10,6))
    sns.barplot(x=freq.index, y=freq.values, palette="viridis")
    plt.title(title if title else f"Frequência de {col}")
    plt.xlabel(col)
    plt.ylabel("Frequência Absoluta")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()



def descriptive_stats(df, col):
    media = df[col].mean()
    mediana = df[col].median()
    moda = df[col].mode()[0] if not df[col].mode().empty else None
    variancia = df[col].var()
    desvio_padrao = df[col].std()
    cv = desvio_padrao / media if media != 0 else None
    minimo = df[col].min()
    maximo = df[col].max()
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)

    print(f"--- Estatísticas para '{col}' ---")
    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {moda}")
    print(f"Variância: {variancia:.2f}")
    print(f"Desvio padrão: {desvio_padrao:.2f}")
    print(f"Coeficiente de variação: {cv:.2%}" if cv is not None else "CV: indefinido")
    print(f"Mínimo: {minimo}")
    print(f"Máximo: {maximo}")
    print(f"Q1 (25%): {q1}")
    print(f"Q3 (75%): {q3}")
    print()


print(freq_table("coffee_name"))
print(freq_table("Time_of_Day"))
print(freq_table("Weekday"))
print(freq_table("Month_name"))

# plot_freq("coffee_name", "Frequência de Tipos de Café")
# plot_freq("Time_of_Day", "Frequência por Período do Dia")
# plot_freq("Weekday", "Frequência por Dia da Semana")
# plot_freq("Month_name", "Frequência por Mês")

descriptive_stats(df, "money")
descriptive_stats(df, "hour_of_day")



print("Análise Bivariada")
tabela_cruzada41 = pd.crosstab(df['Weekday'], df['Time_of_Day'])
print(tabela_cruzada41)
print()

print("Tabela Cruzada Percentual (Row-wise %)")
tabela_cruzada_pct41 = pd.crosstab(df['Weekday'], df['Time_of_Day'], normalize='index') * 100
print(tabela_cruzada_pct41.round(2))



media_por_dia = df.groupby('Weekday')['money'].mean().round(2)
print("Média de Money por Dia da Semana:")
print(media_por_dia)



plt.figure(figsize=(8,5))
sns.barplot(x=media_por_dia.index, y=media_por_dia.values, palette="viridis")
plt.title("Média de Money por Dia da Semana")
plt.ylabel("Média de Money")
plt.xlabel("Dia da Semana")
plt.show()



