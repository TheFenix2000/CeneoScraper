import os 
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print(*[file_name.removesuffix(".json") for file_name in os.listdir('./opinions')], sep="\n")
product_code = input("Enter product code: ")

opinions = pd.read_json(f"opinions/{product_code}.json")
opinions.score = opinions.score.map(lambda x: x.split("/")[0].replace(",", ".")).astype(float)
stats = {
    'opinions_count': opinions.shape[0],
    'pros_count': opinions.pros.astype(bool).sum(),
    'cons_count': opinions.cons.astype(bool).sum(),
    'average_score': opinions.score.mean()
}
print(f"""Dla produktu o kodzie {product_code} pobranych zostało {stats['opinions_count']} opinii/opinie. Dla {stats['pros_count']} opinii podana została lista zalet produktu, a dla {stats['cons_count']} opinii podana została lista jego wad. Średia ocen produktu wynosi {stats['average_score']:.2f}.""")

stars = opinions.score.value_counts().reindex(list(np.arange(0, 5.5, 0.5)), fill_value=0)
stars.plot.bar()

try:
    os.mkdir("./figures")
except FileExistsError:
    pass

plt.title("Wykres ocen produktu")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")

plt.savefig(f"./figures/{product_code}_score.png")
plt.close()

recommendation = opinions["recommendation"].value_counts(dropna = False)
recommendation.plot.pie(
    autopct="%1.1f%%",
    labels = ["Polecam", "Nie polecam", "Nie mam zdania"],
    colors = ["green", "red", "gray"]
)

plt.savefig(f"./figures/{product_code}_recommendation.png")
plt.close()
