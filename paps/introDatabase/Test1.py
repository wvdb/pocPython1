import dbm
from paps.introDatabase.Book import Book

# Create DB

db = dbm.open('myBooks', 'c')

# db["1"] = Book(1, '1984', 25.21, None).__str__()

db["1"] = Book(1, '1984', 25.21, "").__str__()
db["2"] = Book(2, 'animal farm', 14.12, "").__str__()

for key in db:
    print('gevonden in de db : ', key, db[key])

db.close()