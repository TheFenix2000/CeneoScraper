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
print(f"""Dla produktu o kodzie {product_code} pobranych zostało {stats['opinions_count']} opinii/opinie. Dla {stats['pros_count']} opinii podana została lista zalet produktu, a dla {stats['cons_count']} opinii podana została lista jeego wad. Średia ocen produktu wynosi {stats['average_score']:.2f}.""")

stars = opinions.score.value_counts().reindex(list(np.arange(0, 5.5, 0.5)), fill_value=0)
stars.plot.bar()
plt.show()

#Na dodatkowe pkt:
# - Zrobić wykres kołowy: dla ilu polecam, dla ilu nie polecam (drop na do value_counts() - nie pomijaj NaN)
# - Utworzyć katalog plots i zapisywać wszystkie wykresy w katalogu i nie indeksować tego katalogu