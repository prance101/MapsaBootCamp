from abc import ABCMeta, abstractmethod


class Internet(metaclass=ABCMeta):

    @abstractmethod
    def connetcting(self, Card_code):
        pass


class Bank_port(Internet):
    def connetcting(self, Card_code):
        print("{} Your card is unvalid!".format(Card_code))


class Proxy(Internet):
    def __init__(self):
        self.__port = Bank_port()
        self.__cart_list = []
        self.min_inventory = 1000000

    def valid_card_code(self, valid):
        self.__cart_list.append(valid)

    def inventory(self,count):
        self.__cart_list.append(count)

    def connetcting(self, Card_code):
        if Card_code in self.__cart_list:
            print("Your card is valid")

        else:
            self.__port.connetcting(Card_code)


class Bank_card:
    def __init__(self):
        self.port = Proxy()
        self.port.valid_card_code("123456789")
        self.port.inventory("1000000")

    def connect(self, Card_code):
        self.port.connetcting(Card_code)


if __name__ == "__main__":
    port = Bank_card()
    port.connect(input('cart_code: '))
    port.connect(input('have much money: '))