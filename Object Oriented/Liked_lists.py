class listnode:
    def __init__(self ,name):
        self.name = name
        self.next = None
        return
    
    def values(self ,value):
        "moghayes value ba node data"
        if self.name == value:
            return True
        else:
            return False
        
        
class linked_lists:
    def __init__(self):
        self.root  = None
        self.begin = None
        self.end   = None
        self.lenght= 0
        return
    
    def add_begin(self ,newItem):
        if self.root == None:
            self.root = newItem
        else:
            newItem.next = self.root
            self.root    = newItem
        self.lenght = self.lenght + 1
        
        
    def add_mdt(self ,perItem ,newItem):
        x = perItem.next
        perItem.next = newItem
        newItem.next = x
        self.lenght = self.lenght + 1
    
    
    def add_end(self ,newItem):
        if self.root == None:
            self.root = newItem
        else:
            if self.root.next == None:
                self.root.next = newItem
            if self.end != None:
                self.end.next  = newItem
            self.end = newItem
            

    def remove(self ,item):
        if self.root == item:
            self.root = self.root.next
        else:
            self.root.next = srn
            while True:
                if srn == item:
                    break
                srn = self.root
                
    
    def printLL(self):
        if self.root == None:
            print('Empty!')
        else:
            x = self.root
            print(self.root.name)
            while (self.root.next):
                x = x.next
                print(x.name)
                    
        
        
#node1 = listnode(10) ; node2 = listnode(20) ; node3 = listnode("hamed")
#print(node1.values(15))

main = linked_lists()
item_1 = listnode("hamed") ; item_2 = listnode("ali") ; item_3 = listnode("yaser")
item_4 = listnode("mm") ; item_5 = listnode("nima") ; item_6 = listnode("sima")

main.add_begin(item_1)
main.add_mdt(item_1,item_4)
main.add_end(item_3)

#remove()
main.printLL()
