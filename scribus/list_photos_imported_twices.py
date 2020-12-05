import scribus

db = {}

whitelist = [
    "/home/iomonad/Medias/Projets/225kv/Metropolitain/K-70_3200_K70_1247.jpg",
    "/home/iomonad/Medias/Projets/225kv/EDF/K-70_100_K70_4479.jpg",
    "/home/iomonad/Medias/Projets/225kv/Metropolitain/X-T1_3200_DSCF5522.jpg",
    "/home/iomonad/Medias/Projets/225kv/Metropolitain/X-T1_6400_DSCF5559.jpg",
    "/home/iomonad/Medias/Projets/225kv/Gtek/K-70_200_K70_1838.jpg",
    "/home/iomonad/Medias/Projets/225kv/Ambiance/fomapan_029.jpg",
    "/home/iomonad/Medias/Projets/225kv/Metropolitain/K-70_3200_K70_3660.jpg",
    "/home/iomonad/Medias/Projets/225kv/Carrieres/ILCE-7_200_DSC03490.jpg",
    "/home/iomonad/Medias/Projets/225kv/Carrieres/K-70_200_K70_4298.jpg",
    "/home/iomonad/Medias/Projets/225kv/RER/X-T1_6400_DSCF2942.jpg",
    "/home/iomonad/Medias/Projets/225kv/Gtek/ILCE-7_640_DSC01903.jpg",
    "/home/iomonad/Medias/Projets/225kv/RER/fomapan_025.jpg",
    "/home/iomonad/Medias/Projets/225kv/Gtek/analog_025.jpg",
    "/home/iomonad/Medias/Projets/225kv/Ambiance/X-T1_3200_DSCF5885.jpg",
]

for page in range(1, scribus.pageCount() + 1):
    scribus.gotoPage(page)
    for item in scribus.getPageItems():
        if item[1] == 2:
            k = scribus.getImageFile(item[0])
            if k in whitelist or k == "":
                continue
            if k in db:
                db[k] += 1
                print(k, db[k])
            else:
                db[k] = 1
