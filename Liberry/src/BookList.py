from Model import *

mm  = Members('hamed' , 'sh', 28)
mm1 = Members('ali' , 'mn', 25)
mm2 = Members('milad' , 'ss', 23)
mm3 = Members('saeed' , 'df', 24)
mm4 = Members('sina' , 'gg', 29)

class Book:
    def __init__(self, bookname, author, category, bookid, language, translator, year):
        self.bookname   = bookname
        self.author = author
        self.category = category
        self.bookid = bookid
        self.language = language
        self.translator = translator
        self.year   = year
        self.status = True
        self.rent   = None

    # ezafe kardan ketabie renk be yek list json
    def addRentBook(self, author, bookid, bookname, year, name, family):
        data = {}
        data['books'] = []
        data['books'].append({
            "author": str(self.author),
            "bookid": str(self.bookid),
            "name": str(self.bookname),
            "year": self.year,
            "memberName": str(Members('hamed', 'sh', '28')),
        })
        with open('rentBookList.txt', 'w') as outfile:
            json.dump(data, outfile)

    def removeRentBook(self):
        pass

    #khandan rentBookList
    def readRentBook(self):
        with open('rentBookList.txt', 'r') as list:
            data = list.read()
        object = json.loads(data)
        for i in object['faBooks']:
            BookIrani.name = (i['name'])


class BookIrani(Book):
    pass
def abcd():
    pass
nameList = [] ; authorList = [] ; categoryList = [] ; bookidList = [] ; TranslatorList = []
with open('Fa_book.txt' , 'r') as list:
    data = list.read()
object = json.loads(data)
for i in object['faBooks']:
    nameList.append(i['name'])
    BookIrani.name = nameList

    authorList.append(i['author'])
    BookIrani.author = authorList

    categoryList.append(i['category'])
    BookIrani.category = categoryList

    bookidList.append(i['bookid'])
    BookIrani.bookid = bookidList

    TranslatorList.append(i['translator'])
    BookIrani.translator = TranslatorList



class BookInternational(Book):
    pass

enNameList = [] ; enAuthorList = [] ; enCategoryList = [] ; enBookidList = []
languageList = []

with open('En_book.txt' , 'r') as list:
    data = list.read()
object = json.loads(data)
for i in object['enBooks']:
    enNameList.append(i['name'])
    BookInternational.name = enNameList

    enAuthorList.append(i['author'])
    BookInternational.author = enAuthorList

    enCategoryList.append(i['category'])
    BookInternational.category = enCategoryList

    enBookidList.append(i['bookid'])
    BookInternational.bookid = enBookidList

    languageList.append(i['language'])
    BookInternational.language = languageList


book1 = Book(str(BookIrani.name[1]),str(BookIrani.author[1]),str(BookIrani.category[1]),
             str(BookIrani.bookid[1]),'',str(BookIrani.translator[1]),'')
book1.addRentBook("ss", "mh-8890", "buterfly", 1995, "hamed","sh")


print(BookIrani.name)
print(BookIrani.author)
print(BookInternational.name)
print(BookInternational.language)
bbb=BookIrani()
bbb.ab