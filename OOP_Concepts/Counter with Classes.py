import time
class Counter():
    def __init__(self,count = 0):
        self.count = count
    def starting_value(self,new_starting = 0):
        self.count = new_starting
        print("Starting values is updated:",self.count)
    def increment_counter(self,increment):
        self.count += increment
        print("Value:",self.count)
    def decrement_counter(self,decrement):
        self.count -= decrement
        print("Value:",self.count)
    def reset_counter(self):
        self.count = 0
        print("Counter has been reset. Value: {}".format(self.count))

counter = Counter()
print("""
Info:
1--> See the starting value:
2--> Increment the counter as you wish:
3--> Decrement the counter as your wish:
4--> Reset the counter:
q--> Exit the program
""")
while True:
    py = input("Select an option:")
    if py == "q":
        print("Ending the program.")
        for i in range(3):
            print(".",end=" ")
            time.sleep(1)
        print("\n")
        for i in range(4):
            print(".",end =" ")
            time.sleep(1)
        break
    elif py == "1":
        counter.starting_value()
    elif py == "2":
        increment_value = int(input("Increment value:"))
        counter.increment_counter(increment_value)
    elif py == "3":
        decrement_value = int(input("Decrement value:"))
        counter.decrement_counter(decrement_value)
    elif py =="4":
        counter.reset_counter()
    else:
        print("Please enter numbers 1-4")

