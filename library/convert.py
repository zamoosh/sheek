import pandas as pd
from django.conf import settings
import os


def convert():
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "library", '1.xlsx'))
    list = []
    counter = 0
    for i in range(df.index.start, df.index.stop, df.index.step):
        data = {}
        try:
            for j in range(len(df.columns)):
                st = df.iloc[i, j]
                if "#" in st:
                    data[j] = df.iloc[i, j].split("#")
                else:
                    data[j] = df.iloc[i, j]
            list.append(data)
        except:
            pass
    print(list)
