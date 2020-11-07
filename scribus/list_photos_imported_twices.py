# Scribus Python Console
#
# This is a standard Python console with some
# known limitations. Please consult the Scribus
# Scripter documentation for further information.

import scribus

db = {}

for page in range(1, scribus.pageCount() + 1):
    scribus.gotoPage(page)
    for item in scribus.getPageItems():
        if item[1] == 2:
            k = scribus.getImageFile(item[0])
            if k in db:
                db[k] += 1
                print(k, db[k])
            else:
                db[k] = 1
