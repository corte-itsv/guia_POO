class Employee:
    def __init__(self , name , pay):
        self.name = name
        self.pay = pay

    def monthly_pay(self):
        return self.name + "monthly pay :" + str(self.pay)


class FullTimeEmployee(Employee):
    pass


class PartTimeEmployee(Employee):
    def __init__(self , name , hours , value):
        super().__init__(name = name , pay = hours * value)

if __name__ == "__main__":
    partTime =  PartTimeEmployee(" Bob ", 500, 20)
    fullTime =  FullTimeEmployee(" Alice ", 60000)
    print(partTime.monthly_pay())
    print(fullTime.monthly_pay())
