import pandas as pd
from django.conf import settings
import os
import jdatetime
from unidecode import unidecode
from law.models import *
from projects.models import JobField, Tag
import MySQLdb


class Convert:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "mdavoodi2020"
        name = "tags"
        db = MySQLdb.connect(host, user, password, name, charset='utf8', use_unicode=True)
        self.cursor = db.cursor()

    def convert(self):
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

    def convertMaintSubGroup(self):
        self.cursor.execute("SELECT * FROM `shekk`")
        for item in self.cursor.fetchall():
            jobfield = JobField(id=item[0])
            jobfield.title = item[1]
            if item[5]:
                jobfield.parent_id = item[5]
            jobfield.save()

    def convertSalahiat(self):
        self.cursor.execute("SELECT * FROM `sheeek` WHERE `sId` = 3")
        for item in self.cursor.fetchall():
            jobfield = JobField()
            jobfield.title = item[3]
            jobfield.parent = JobField.objects.get(id=item[5])
            jobfield.save()

    def convertTags(self):
        self.cursor.execute("SELECT * FROM `sheeek` WHERE `sId` = 3")
        for item in self.cursor.fetchall():
            tag = item[4].split("#")
            b = 0
            for i in tag:
                print(i)
                if len(i.strip()) == 0:
                    continue
                tags, _ = Tag.objects.get_or_create(title=i.strip())
                for j in JobField.objects.filter(title=item[3].strip()):
                    if j.parent is None:
                        continue
                    elif j.parent.parent is None:
                        continue
                    elif j.parent.parent:
                        print(i, j)
                        try:
                            tags.jobfield.add(j.id)
                        except:
                            pass

    def convertRouls(self):
        self.cursor.execute("SELECT DISTINCT (`group`) FROM `sheet1` ")
        for item in self.cursor.fetchall():
            group = Group()
            group.title = item[0]
            group.save()

    def convertRule(self):
        self.cursor.execute("SELECT * FROM `sheet1` ")
        for item in self.cursor.fetchall():
            rule = Rule()
            rule.group = Group.objects.get(title=item[1])
            rule.date = unidecode(item[2])
            print(rule.date)
            rule.date = item[2]
            rule.title = item[3]
            rule.article = item[4]
            rule.description = item[5]
            rule.footnote = item[6]
            rule.save()
