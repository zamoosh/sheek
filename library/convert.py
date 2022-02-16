import pandas as pd
from django.conf import settings
import os
from projects.models import JobField, Tag


def convert():
    df = pd.read_excel(os.path.join(settings.BASE_DIR, "library", '1.xlsx'))
    list = []
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
        try:
            job, _ = JobField.objects.get_or_create(title=i[0].strip())
            job, _ = JobField.objects.get_or_create(title=i[1].strip(), parent=job)
            job, _ = JobField.objects.get_or_create(title=i[2].strip(), parent=job)
            for j in i[3]:
                if j.strip() == "":
                    continue
                tag, _ = Tag.objects.get_or_create(title=j.strip())
                tag.jobfield.add(job)
        except:
            pass
