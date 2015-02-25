##<Akshay Jha>
##<akshayjha@live.in>

##<https://github.com/axayjha?tab=repositories>
##<www.akshayjha.co.nr>

##--------------------------------------------------------------------------------------------------
##------------------------------------------HEADER--------------------------------------------------

print("+--------------------------------------------------+")
print("|                                                  |")
print("|                                                  |")
print("|         Recurring Deposit Calculator             |")
print("|         & automatic chart creater                |")
print("|                 Version 0.2                      |")
print("|                                                  |")
print("|                                                  |")
print("|                                          //Akshay|")
print("+--------------------------------------------------+")
print("")


##--------------------------------------------------------------------------------------------------
## Initialization of all the lists to store the data for different blocks
## One of the lists, named 'total' is initialized on around 100th line of the code for technical reasons

year=[] ## List containing the time intervals for all the blocks in MMYYYYmmyyyy format. eg. 012015092015 for 01/2015-09/2015
rate=[] ## List containing the interest rates for all the blocks
contribution=[] ## List containing the contribution amount for all the blocks

##---------------------------------------------------------------------------------------------
##Gets Name
name=''
while name=='':
        name=str(input("Enter name of the client: "))
        print("")
        if name=='':
                print("Invalid response. Try again.")
                print("")

##-------------------------------------------------------------------------------------------------
## Looping constructs used to get all the necessary inputs required to do the calculations

inp='2'
while inp!="1" or inp=="":
        mnyr1=str(input("Enter the starting month and year(in MMYYYY format): "))

        while len(mnyr1)!=6: 	
                print("Invalid format. Try again.")
                mnyr1=str(input("Enter the starting month and year(in MMYYYY format): "))
        
        while int(mnyr1[0:2])>12:
                print("Invalid month number. Try again.")              
                mnyr1=str(input("Enter the starting month and year(in MMYYYY format): "))     
       
        rt=float(input("Enter the interest rate: "))

        while rt<0:
                print("Invalid response. Interest rate must be positive. Try again.")
                rt=float(input("Enter the interest rate: "))

        if rt==0:
                print("Warning! You entered 0% interest rate. If it was intentional, ignore this \warning")
                print("If you mistyped, you'll have to start over again.")


        dd=float(input("Enter the contribution: "))	

        while dd<0:
                print("Invalid response. Contribution must be positive. Try again.")
                dd=float(input("Enter the contribution: "))

        mnyr2=str(input("Enter ending(last) month and year(MMYYYY): "))

        while len(mnyr2)!=6: 	
                print("Invalid format. Try again.")
                mnyr2=str(input("Enter the ending(last) month and year(in MMYYYY format): "))
                
                
        while int(mnyr2[0:2])>12:
                print("Invalid month number. Try again.")              
                mnyr2=str(input("Enter the ending(last) month and year(in MMYYYY format): "))

        print("")

        ##<-
        mnyr=mnyr1+mnyr2
        year.append(mnyr)	
        rate.append(rt)
        contribution.append(dd)
        ##->

        mnyr1=""
        mnyr2=""


        print("[1] Submit")
        print("[2] Continue") 
        print("")
        inp=str(input("Your response: "))
        print ("")

     

total=[contribution[0], ]   

##-------------------------------------------------------------------------------------------------
## months(MMYYYYmmyyyy): Function to find the number of months between MM/YYYY and mm/yyyy
## yearint = MMYYYYmmyyyyy

def months(yearint):

        if len(yearint)<12:
                raise  ValueError("Perhaps, you've entered the date(s) inappropriately. Date must be in MMYYYY format. (e.g.- 012015 for January, 2015.)")

        if int(yearint[2:6])>int(yearint[8:12]) or (int(yearint[2:6])==int(yearint[8:12]) and int(yearint[6:8])< int(yearint[0:2])):
                raise ValueError ("Perhaps, you have entered date in reverse order. Try again and enter older date first")

        if int(yearint[6:8])>= int(yearint[0:2]):
                yrint=int(yearint[8:12])-int(yearint[2:6])
                mnint=int(yearint[6:8])-int(yearint[0:2])
        else:
                yrint=(int(yearint[8:12])-int(yearint[2:6]))-1
                mnint=(int(yearint[6:8])-int(yearint[0:2]))+12                             

           

        month=(yrint*12)+mnint

        return month

##--------------------------------------------------------------------------------------------------
## roundto5p(x) : Takes any number x and rounds it off to the nearest multiple of 0.05
## Used here to round off an amount Rs. x to the nearest multiple of 5 paise
## for example, Rs4.33 will be rounded off to Rs4.35 and Rs4.32 to Rs4.30

def roundto5p(x):           ##Rounds off the amount(x) to the nearest multiple of 5 paise(0.05 Rupees)
	if type(x)==float:
		if round(round(x,2)%0.05, 2)<0.03:
			z=x-round(round(x,2)%0.05, 2)
		else:
			z=x+(0.05-round(round(x,2)%0.05, 2))
		return round(z,2)
	elif type(x)==int:
		return x
	else:
		raise TypeError ("Enter a valid number in parenthesis")


##--------------------------------------------------------------------------------------------------
## The most importain function, the main() function of this script, so to say.
##
## Let me explain the arguments it takes:
## pAmount : Principle amount - The contribution per month of the client for a particular block
## nAmount : Total amount at the end of the previous block including interests (equal to pAmount for the very first block)
## rate    : Interest rate per annum
## month   : Total number of months for one block
##
## This function returns the total balance including interests of a client

def returnValue(pAmount, nAmount, rate, month):  
        loop=0
                
        while loop<(month):
                amount=nAmount
                if loop>0:
                        amount=summ + pAmount   
                summ=amount + roundto5p(amount*rate/1200)                             
                loop=loop+1
        return roundto5p(summ)

##--------------------------------------------------------------------------------------------------

i=0

while i<len(year):
	total.append(returnValue(contribution[i], total[i], rate[i], months(year[i])))
	i=i+1

##--------------------------------------------------------------------------------------------------
## Created chart       

print("")
print("Data chart for " + name)
print("-----------------------------------------------------------------")
print("## |      Year       |Amount| Rate | Interest |  Total  |")


c=0
while c<len(year):
	print(" "+str(c+1) +" | "+str(year[c][0:2])+"/"+str(year[c][2:6])+"-"+str(year[c][6:8])+"/"+str(year[c][8:12]) + " | "+str(contribution[c]) +" | "+str(rate[c])+" | "+str(roundto5p(total[c+1]-(months(year[c])*contribution[c])))+" | "+str(total[c+1])+" | ")
	c=c+1



print("-----------------------------------------------------------------")

print("")
input("Press <ENTER> to exit")
