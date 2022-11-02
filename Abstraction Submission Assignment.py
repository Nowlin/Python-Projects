from abc import ABC, abstractmethod
class dayJob(ABC):
    def paySlip(self, amount):
        print("Your pay amount is: ", amount)
    @abstractmethod
    def payment(self, amount):
        pass

class monthlyBill(dayJob):
    def payment(self, amount):
        print('Your bill of {} exceeded your $400 pay '.format(amount))

obj = monthlyBill()
obj.paySlip("$400")
obj.payment("$800")
