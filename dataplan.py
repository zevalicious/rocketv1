datainmonths=[]
monthlydata=int(input("enter mb/month for your data plan"))
month=int(input("enter number of months on the data plan"))
for i in range(month):
    data = int(input("enter data used in month"))
    datainmonths.append(data)
dataused = 0
for i in datainmonths:
    dataused += i

print("you have " + str((month*monthlydata)-(dataused))+" mb for this month")
    
