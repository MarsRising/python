class Queue:
    def __init__(self):
        self.items=[]

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size()==0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

class IceCreamShop:
    def __init__(self,flavors):
        self.flavors=flavors
        self.orders=Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("\nSorry, we do not have this flavor.")
            return None
        if not (1 <= scoops <= 3):
            print("\nSorry, we can only provide up to 3 scoops.")
            return None
        else:
                print("\nOrder Created!")

        order={"customer": customer, "flavor":flavor, "scoops":scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        print("\nAll pending orders:")
        for orders in self.orders.items:
            print("Customer:", orders["customer"], "--Flavor:", orders["flavor"], "--Scoops:", str(orders["scoops"]))

    def next_order(self):
        print("\nNext Order Up:")
        for orders in self.orders.items:
            print("Customer:", orders["customer"], "--Flavor:", orders["flavor"], "--Scoops:", str(orders["scoops"]))
        self.orders.dequeue()

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()