import unicodedata
import re
from num2words import num2words

def numberLetterCounts(limit):
    count = 0
    while limit:
        title = num2words(limit)
        titleStr = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore')
        titleMain = re.sub('[^A-Za-z0-9]+', '', titleStr)
        if limit == 101:
            print(titleMain)
        count += len(titleMain)
        limit -= 1
    return count

print(numberLetterCounts(101)) 