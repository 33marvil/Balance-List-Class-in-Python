"""code goes here"""
class BalanceList:

    # constructor method
    def __init__(self, name, balances):
        self.__name = name
        self.__balances = balances
        self.__nums = 0

    # getter method
    @property
    def name(self):
        return self.__name

    # return largo de la lista balances
    def number_of_balances(self):
        return len(self.__balances)

    # return suma de balances
    def total_balance(self):
        # balance = 0 # variable Local Acumulador
        return sum([saldo[1] for saldo in self.__balances]) # list Comprehensions
        # for saldo in self.__balances:# iteracion list
        #     balance += saldo[1] # acumulador de resultado de iteracion por posición
        #return balance

    def add_balance(self, balance):
        return self.__balances.append(balance)

    def current_balance_per_month(self): # posición en list
        return "Mes: " + "" + self.__balances[self.__nums][0] + ", Saldo: " + str(self.__balances[self.__nums][1])

    def next_balance(self):
        if self.__nums < len(self.__balances) - 1:
            self.__nums += 1
        else:
            self.__nums = 0
        return self.__balances[self.__nums][1]


# balance_1 = BalanceList("Manuel", [["Julio", 234], ["Enero", 456], ["Agosto", 123]])
# print(balance_1.name == "Manuel")
# print(balance_1.number_of_balances() == 3)
# print(balance_1.total_balance())#== 813)
# balance_1.add_balance(["Marzo", 678])
# print(balance_1.number_of_balances() == 4)
# print(balance_1.current_balance_per_month() == "Mes: Julio, Saldo: 234")
# print(balance_1.next_balance())#== 456)
# print(balance_1.next_balance())#== 123)
# print(balance_1.current_balance_per_month() == "Mes: Agosto, Saldo: 123")
# print(balance_1.next_balance())#== 678)
# print(balance_1.next_balance())
# print(balance_1.next_balance())
