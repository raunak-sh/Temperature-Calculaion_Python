temperature = []
categoryCheck=[]
companyName = input("Enter the name of company: ")
address = input("Enter the address: ")
dateIn = input("Enter the date: ")



def initialDisplay(companyName, address, dateIn):
    header = f"""           
                        {companyName}
                          {address}
                                     Date: {dateIn}
          """
    print(header)
    return header


initialDisplay(companyName,address,dateIn)


def inputInfo():
    days = int(input("How many days to record?: "))
    print(f"Please enter {days} days temperature readings: ")
    for i in range(days):
        temp = int(input(f"Temperature day[{i + 1}]"))
        temperature.append(temp)

    return days


def calculationTemperature(temperature, days):
    sum = 0
    for i in temperature:
        sum = sum + i
    avg = sum / days
    return avg


def check(temperature):
    hot = 0
    cold = 0
    pleasant = 0


    for i in temperature:
        if i < 60:
            categoryCheck.append("Very cold")
            cold=cold + 1
        elif 60 < i < 80:
            categoryCheck.append("Pleasant")
            pleasant =pleasant + 1
        else:
            categoryCheck.append("Very hot")
            hot=hot + 1

    return cold,hot,pleasant
            
   

def final_display(days,avg,cold,hot,pleasant):
    for k in range(days):
            print(f'''Temperature day {k+1}={temperature[k]} Celsius {categoryCheck[k]}''')

    print(f"The average Temperature for {days}= {avg}Celsius")
    print(f"Number of hot days= {hot}")
    print(f"Number of Pleasant days= {pleasant}")
    print(f"Number of cold days= {cold}")
            
    
    

days=inputInfo()
avg=calculationTemperature(temperature,days)
hot,cold,pleasant=check(temperature)
final_display(days,avg,hot,cold,pleasant)


