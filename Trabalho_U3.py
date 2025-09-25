import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

caminho_db = r'C:\Users\Guilh\projeto\ADS\banco\dados_vendas.db'
conn = sql.connect(caminho_db, timeout=10)
cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS vendas1 (
  id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
  data_venda DATE,
  produto TEXT,
  categoria TEXT,
  valor_venda REAL,
  UNIQUE(produto, categoria, valor_venda)
)
''')

vendas = [
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00)
]

for venda in vendas:
    cursor.execute('''
        INSERT OR IGNORE INTO vendas1 (data_venda, produto, categoria, valor_venda)
        VALUES (?, ?, ?, ?)
    ''', venda)

cursor.execute("SELECT * FROM vendas1;")
rows = cursor.fetchall()

# Pegando nomes das colunas
colunas = [desc[0] for desc in cursor.description]

# Criando o DataFrame
df = pd.DataFrame(rows, columns=colunas)

print(">-------------------------------------------------------------<")
print(df)

print(">-------------------------------------------------------------<")

acao = 0

while acao != "10":
  acao = 0
  acao = input("O que você quer saber?\n1 - Total de dinheiro por categoria.\n2 - Compra mais cara.\n3 - Valor médio total.\n4 - Relatório de vendas.\n> ")
  print(">----------------------------------<")

  if acao == "1":
    vendas_categoria = df.groupby("categoria")["valor_venda"].sum()
    #print(vendas_categoria)

    plt.figure(figsize=(8,5))
    plt.bar(vendas_categoria.index, vendas_categoria.values, color='green')
    plt.title("Venda total por categoria - Matplotlib")
    plt.xlabel("Categoria")
    plt.ylabel("Vendas Totais")
    plt.show()
    plt.close('all')

    print(">----------------------------------<")

  elif acao == "2":
    mais_vendido = df.groupby("produto")["valor_venda"].sum().sort_values(ascending=False)
    #print(mais_vendido)

    plt.figure(figsize=(8,5))
    plt.bar(mais_vendido.index, mais_vendido.values, color='skyblue')
    plt.title("Vendas por Produto - Matplotlib")
    plt.xlabel("Produto")
    plt.ylabel("Total de Vendas")
    plt.xticks(rotation=45)
    plt.show()
    plt.close('all')

    print(">----------------------------------<")

  elif acao == "3":
    df["data_venda"] = pd.to_datetime(df["data_venda"])  # garantir tipo datetime
    df["ano_mes"] = df["data_venda"].dt.to_period("M")   # formato AAAA-MM
    total_mes = df.groupby("ano_mes")["valor_venda"].sum().reset_index()
    #print(total_mes)

    ax = sns.barplot(data=total_mes, x="ano_mes", y="valor_venda")
    ax.set_title("Vendas por Mês - Seaborn")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Valor Vendido")
    ax.tick_params(axis='x',labelrotation=45.0)
    plt.show()
    plt.close('all')

    print(">----------------------------------<")

  elif acao == '4':
    vendas_categoria = df.groupby("categoria")["valor_venda"].sum()
    categoria_vendeu = vendas_categoria.idxmax()
    mais_vendido = df.groupby("produto")["valor_venda"].sum().sort_values(ascending=False)
    ticket_medio = df["valor_venda"].mean()


    print("\n=== Conclusão e Insights ===")
    print(f"- O produto mais vendido foi: {mais_vendido.index[0]} com R${mais_vendido.iloc[0]:.2f} em vendas.")
    print(f"- O ticket médio das vendas foi de R${ticket_medio:.2f}.")
    print(f"- A categoria que mais vendeu foi: {categoria_vendeu} com {vendas_categoria.max():.2f} Reais vendidos")
    print("- Sugestão: focar em campanhas para os produtos e categorias mais vendidos, "
      "além de estratégias para aumentar o ticket médio, como combos ou upselling.")
    print(">----------------------------------<")


  elif acao >= '5' and acao != '10':
    print("Digite uma opção valida!")


else:
  print("Fechando o sistema...")
  #cursor.execute("DELETE FROM vendas1")
  conn.commit()
  cursor.close()
  conn.close()