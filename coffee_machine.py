# Write your code here
class CoffeeMachine:
    # states = ["Choosing an action", "Choosing a type of coffee", "Filling a coffee machine", "Filling water",
    #               "Filling milk", "Filling beans", "Filling coffee cups"]
    # phrases = ["Write action (buy, fill, take, remaining, exit):",
    #            "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:",
    #            "I have enough resources, making you a coffee!", "Sorry, not enough water!", "Sorry, not enough milk!",
    #            "Sorry, not enough beans!", "Sorry, not enough cups!"]
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.coffee_cups = 9
        self.money = 550
        self.current_state = "Choosing an action"

    def check_water(self, amount_of_water):
        if self.water - amount_of_water > 0:
            return True
        else:
            print("Sorry, not enough water!")
            self.current_state = "Choosing an action"
            return False

    def check_milk(self, amount_of_milk):
        if self.milk - amount_of_milk > 0:
            return True
        else:
            print("Sorry, not enough milk!")
            self.current_state = "Choosing an action"
            return False

    def check_beans(self, amount_of_beans):
        if self.beans - amount_of_beans > 0:
            return True
        else:
            print("Sorry, not enough beans!")
            self.current_state = "Choosing an action"
            return False

    def check_coffee_type(self, coffee_type):
        if coffee_type != "back":
            if self.coffee_cups > 0:
                if coffee_type == "1":
                    if self.check_water(250):
                        if self.check_beans(16):
                            self.make_coffee("1")
                if coffee_type == "2":
                    if self.check_water(350):
                        if self.check_milk(75):
                            if self.check_beans(20):
                                self.make_coffee("2")
                if coffee_type == "3":
                    if self.check_water(200):
                        if self.check_milk(100):
                            if self.check_beans(12):
                                self.make_coffee("3")
                return
            else:
                print("Sorry, not enough cups!")
                self.current_state = "Choosing an action"
                return
        return

    def make_coffee(self, coffee_type):
        if coffee_type == "1":
            self.water -= 250
            self.beans -= 16
            self.money += 4
        if coffee_type == "2":
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
        if coffee_type == "3":
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6
        self.coffee_cups -= 1
        print("I have enough resources, making you a coffee!")
        self.current_state = "Choosing an action"
        return

    def __str__(self):
        return f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.coffee_cups} of disposable cups
{self.money} of money"""

    def fill_water(self, water):
        self.water += water
        return

    def fill_milk(self, milk):
        self.milk += milk
        return

    def fill_beans(self, beans):
        self.beans += beans
        return

    def coffee_cup(self, cofcup):
        self.coffee_cups += cofcup
        return

    def take_money(self):
        print("I gave you $%d" % self.money)
        self.money -= self.money
        return

    def read_input(self, string):
        if string == "buy":
            coffee_machine.current_state = "Choosing a type of coffee"
            return
        elif type(string) == int:
            if coffee_machine.current_state == "Filling a coffee machine step 2":
                self.fill_milk(string)
                self.current_state = "Filling a coffee machine step 3"
            elif coffee_machine.current_state == "Filling a coffee machine step 3":
                self.fill_beans(string)
                self.current_state = "Filling a coffee machine step 4"
            elif coffee_machine.current_state == "Filling a coffee machine step 4":
                self.coffee_cup(string)
                self.current_state = "Choosing an action"
            else:
                self.fill_water(string)
                self.current_state = "Filling a coffee machine step 2"
        elif string == "fill":
            self.current_state = "Filling a coffee machine"
        elif string == "take":
            self.take_money()
        elif string == "remaining":
            print(self)
        elif string == "exit":
            global _exit
            _exit = False
        elif string == "1" or "2" or "3":
            self.check_coffee_type(string)


_exit = True
coffee_machine = CoffeeMachine()
while _exit:
    if coffee_machine.current_state == "Choosing an action" and _exit:
        print("Write action (buy, fill, take, remaining, exit):")
        coffee_machine.read_input(input())
    elif coffee_machine.current_state == "Choosing a type of coffee" and _exit:
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_machine.read_input(input())
    elif coffee_machine.current_state == "Filling a coffee machine" or "Filling a coffee machine step 2" or "Filling a coffee machine step 3" or "Filling a coffee machine step 4" and _exit:
        print("Write how many ml of water do you want to add:")
        coffee_machine.read_input(int(input()))
        print("Write how many ml of milk do you want to add:")
        coffee_machine.read_input(int(input()))
        print("Write how many grams of coffee beans do you want to add:")
        coffee_machine.read_input(int(input()))
        print("Write how many disposable cups of coffee do you want to add:")
        coffee_machine.read_input(int(input()))
    print("")
# coffee_made = 0
# while water >= 200 and milk >= 50 and beans >= 15:
#    water -= 200
#    milk -= 50
#    beans -= 15
#    coffee_made += 1
# if coffee_made == coffee_amount:
#   print("Yes, I can make that amount of coffee")
# elif coffee_made > coffee_amount:
#    print("Yes, I can make that amount of coffee (and even %d more than that)" % (coffee_made - coffee_amount))
# elif coffee_made < coffee_amount:
#    print("No, I can make only %d cups of coffee" % coffee_made)
