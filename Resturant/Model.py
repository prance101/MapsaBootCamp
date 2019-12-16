
class Members:
    def __init__(self, Members_name, unity, address):
        self.Members_name = Members_name
        self.unity = unity
        self.shopping_list = []
        self.address = address


    def shopping(self):
        self.food_number = []
        self.food_kind = []


class Food:
    fid = 1111
    def __init__(self, food_name: object, category: object, price: object) -> object:
        self.food_name = food_name
        self.category = category
        self.price = price

    #def generate_id(self):
        self.fid = Food.fid
        Food.fid += 1

    def __str__(self):
        print("ghazaie:",self.food_name,"ba category:",self.category," va gimate:",self.price ,"ba ID:",self.fid,"sabt gardid")


class Comment:
    def __init__(self, unity, fid, rate, **text):
        self.unity = unity
        self.fid  = fid
        self.rate = rate
        self.text = text

    def __str__(self):
        print("eshterake:",unity,"baraie ghaza ba id ",fid," emtizae ",rate ,"midaham")

ghime = Food("ghime","ghaza",12000)
morgh = Food("morgh","ghaza",15000)
salad = Food("salad","deser",10000)

#print(fd3)
