from os import listdir
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


pd.set_option('display.max_columns', None)

print(*listdir("opinions"), sep="\n")

product_id = input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_id}.json")

average_score = opinions.stars.mean()

stars_count = opinions.stars.value_counts().reindex(np.arange(0,5.5,0.5), fill_value = 0)

stars_count.plot.bar()
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.show()

# opinions.pros = opinions.pros.replace(list(), None)
# pros_count = opinions.pros.notnull().count()
# rows_count = opinions.shape[0]

# print(rows_count,"=>",pros_count)
# print(opinions)