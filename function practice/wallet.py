
import enum
class BanknoteType(enum.Enum):
    USD5  = 5
    USD10 = 10
    USD15 = 15
    USD20 = 20
    USD100= 100
#print(BanknoteType.USD10)
#print(BanknoteType.USD10.value)

class Wallet:
    def __init__(self):
        self.cash = {}
        #for item in BanknoteType:
           # self.cash[item.name]= 0
        #print(self.cash)


    def putBanknotesInWallet(self,banknoteType,number):
        if banknoteType not in self.cash:
            self.cash[banknoteType] = number
        else:
            currentNumber=self.cash.get(banknoteType)
            self.cash[banknoteType] = currentNumber + number

    def takeBanknotesFromWallet(self,banknoteType,number):
        if banknoteType not in self.cash:
            print("Not Found")
        else:
            currentNumber = self.cash.get(banknoteType)
            if currentNumber < number:
                print("Error : There is not enough stock")
            else:
                self.cash[banknoteType] = currentNumber -  number





farzinWallet = Wallet()
print(farzinWallet.cash)
farzinWallet.putBanknotesInWallet(BanknoteType.USD10,6)
print(farzinWallet.cash)
farzinWallet.putBanknotesInWallet(BanknoteType.USD5,3)
print(farzinWallet.cash)
farzinWallet.putBanknotesInWallet(BanknoteType.USD10,2)
print(farzinWallet.cash)

farzinWallet.takeBanknotesFromWallet(BanknoteType.USD10,5)
print(farzinWallet.cash)

