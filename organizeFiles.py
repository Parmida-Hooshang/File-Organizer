import os
import re
import sys
import time

BLACK = '\033[30m'
BRIGHT_GREEN = '\033[92m'
RESET = '\033[0m'  # called to return to standard terminal text color

source = sys.argv[1]
dest = sys.argv[2]

# {"year": ([photos' paths],[vids' paths],[Docs' path],[audios' path],[others' path])}
found = {}
if not os.path.isdir(dest):
    os.mkdir(dest)
everything = os.walk(source)
for tup in everything:
    for file in tup[2]:
        route = os.path.join(tup[0], file)
        year = os.path.getmtime(route)
        year = time.ctime(year)
        year = year[-4:-1]+year[-1]
        if re.match(r".+\.(jpg|jpeg|png)$", file.lower()):
            try:
                found[year][0].append(route)
            except:
                found[year] = ([], [], [], [], [])
                found[year][0].append(route)

        elif re.match(r".+\.(mp4|avi|3gp|mpeg|mkv|wmv|mov|gif)$", file.lower()):
            try:
                found[year][1].append(route)
            except:
                found[year] = ([], [], [], [], [])
                found[year][1].append(route)

        elif re.match(r".+\.(doc|docx|pdf|txt|md|xls|xlsx|html|pptx)$", file.lower()):
            try:
                found[year][2].append(route)
            except:
                found[year] = ([], [], [], [], [])
                found[year][2].append(route)

        elif re.match(r".+\.(wav|mp3|aac|flac|m4a|wma|alac)$", file.lower()):
            try:
                found[year][3].append(route)
            except:
                found[year] = ([], [], [], [], [])
                found[year][3].append(route)

        else:
            try:
                found[year][4].append(route)
            except:
                found[year] = ([], [], [], [], [])
                found[year][4].append(route)


for year, data in found.items():
    if data == ([], [], [], [], []):
        continue
    photos = data[0]
    videos = data[1]
    docs = data[2]
    audios = data[3]
    others = data[4]

    os.mkdir(os.path.join(dest, year))
    if photos != []:
        os.mkdir(os.path.join(dest, year, "photos"))
        for p in photos:
            with open(p, "rb") as original:
                info = original.read()
                with open(os.path.join(dest, year, "photos", os.path.basename(p)), "wb") as new:
                    new.write(info)
    if videos != []:
        os.mkdir(os.path.join(dest, year, "videos"))
        for p in videos:
            with open(p, "rb") as original:
                info = original.read()
                with open(os.path.join(dest, year, "videos", os.path.basename(p)), "wb") as new:
                    new.write(info)
    if docs != []:
        os.mkdir(os.path.join(dest, year, "docs"))
        for p in docs:
            with open(p, "rb") as original:
                info = original.read()
                with open(os.path.join(dest, year, "docs", os.path.basename(p)), "wb") as new:
                    new.write(info)
    if audios != []:
        os.mkdir(os.path.join(dest, year, "audios"))
        for p in audios:
            with open(p, "rb") as original:
                info = original.read()
                with open(os.path.join(dest, year, "audios", os.path.basename(p)), "wb") as new:
                    new.write(info)
    if others != []:
        os.mkdir(os.path.join(dest, year, "others"))
        for p in others:
            with open(p, "rb") as original:
                info = original.read()
                with open(os.path.join(dest, year, "others", os.path.basename(p)), "wb") as new:
                    new.write(info)

print("------ All Done! ------")
