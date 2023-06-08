
class node:
    data=None
    next=None
    def __init__(self,dat=None):
        self.data=dat
        print("data = ",self.data)
        return
# temp=node(10)
class lnkedlist:
    header=node()
    print("Linked list created")
    def add(self , dat):
        print("-"*30)
        if(self.header.next==None):
            temp=node(dat)
            self.header.next=temp
            print("First Node added in linked list")
            
        else:
            temp2=node(dat)
            temp=self.header.next
            print("Nodes present in linkedlist are: ")
            while(temp.next!=None):
                # print("k")
                print(temp.data , end=" -> ")
                temp=temp.next
            print(temp.data ,"-> Null")                
            # print("Linkedlist end")
            temp.next=temp2
            # print(temp.next)
            print("Next node added in linked list. Updated linked list is :\n")
            self.print_linked_list();
            return
        # print(self.header.next)
        return
    def insert_at(self, data , ind):
        print("*"*30)
        print("Previous linked list ")
        self.print_linked_list()
        count=1
        temp2=node(data)
        temp=self.header.next
        while(temp.next!=None):
            # print("k")
            # print(temp.data , end=" -> ")
            count=count+1
            if(count==ind):
                break
            else:
                temp=temp.next
        temp2.next=temp.next
        temp.next=temp2
        # print("\n")
        print(f"\nElement {data} insert at {ind} in the linkedlist\n")
        self.print_linked_list()
        
            
        return
    def print_linked_list(self):
        temp=self.header.next
        while(temp.next!=None):
            # print("k")
            print(temp.data , end=" -> ")
            temp=temp.next
        print(temp.data ,"-> Null\n")    
        return 


l=lnkedlist()
l.add(4)
l.add(7)
l.add(9)
l.add(5)
l.add(1)
l.add(3)

l.print_linked_list()
l.insert_at(6,4)