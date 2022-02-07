import pandas as pd
from django.conf import settings
import os
from projects.models import JobField, Tag


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
    for i in list:
        job, _ = JobField.objects.get_or_create(title=i[0])
        job, _ = JobField.objects.get_or_create(title=i[1], parent=job)
        job, _ = JobField.objects.get_or_create(title=i[2], parent=job)
        for j in i[3]:
            tag, _ = Tag.objects.get_or_create(title=j)
            tag.jobfield.add(job)
