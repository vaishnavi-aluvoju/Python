class Bank:
    Bank_Name="TGB"
    def __init__(self,AccNo,Pin=123):
        self.AccNo=AccNo
        self.Pin=Pin
B1=Bank(1347)
B2=Bank(1247,143)
print(B1.AccNo,B1.Pin)
print(B2.AccNo,B2.Pin)
print(B1.Bank_Name)
B1.Bank_Name="SBI"
print(B1.Bank_Name)
print(Bank.Bank_Name)
print(B2.Bank_Name)