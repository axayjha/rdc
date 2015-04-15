##<Akshay Jha>
##<akshayjha@live.in>

##<www.github.com/axayjha>
##<www.akshayjha.co.nr>

##--------------------------------------------------------------------------------------------------

print("""
         +--------------------------------------------------+
         |                                                  |
         |                                                  |
         |         Recurring Deposit Calculator             |
         |         & automatic chart creater                |
         |                 Version 0.3                      |
         |                                                  |
         |                                                  |
         |                                          //Akshay|
         +--------------------------------------------------+ 

         """)


year=[]
rate=[]
contribution=[] 


name=''
while name=='':
        name=str(input("Enter name of the client: "))
        print("")
        if name=='':
                print("Invalid response. Try again.")
                print("")



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


def roundto5p(x):           
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



global monthlyTotal
monthlyTotal=[]

def returnValue(pAmount, nAmount, rate, month):  
        loop=0
        global  monthlyTotal       
        while loop<(month):
                if loop>0:
                        nAmount=nAmount + pAmount
                nAmount=roundto5p(nAmount + (nAmount*rate/1200))
                monthlyTotal.append(nAmount)             
                
                loop=loop+1
        return (nAmount)


i=0

while i<len(year):
	total.append(returnValue(contribution[i], total[i], rate[i], months(year[i])))
	i=i+1


yearsRaw=[]
for c in range(len(year)):
	yearsRaw.append(str(year[c][0:2])+"/"+str(year[c][2:6])+"-"+str(year[c][6:8])+"/"+str(year[c][8:12]) )


contRaw=[]
for c in range(len(contribution)):
	contRaw.append(str(contribution[c]))

rateRaw=[]
for c in range(len(rate)):
	rateRaw.append(str(rate[c]))

totRaw=[]
for c in range(len(total)):
	totRaw.append(str(total[c]))

intRaw=[]
for c in range(len(contribution)):
        intRaw.append(str(roundto5p(total[c+1]-(months(year[c])*contribution[c]))))

dataRaw=[]

dataRaw.append(yearsRaw)
dataRaw.append(contRaw)
dataRaw.append(rateRaw)
dataRaw.append(totRaw)
dataRaw.append(intRaw)



data=""""""
for i in range(len(dataRaw[0])):
	data=data+"""<tr><td>"""+str(dataRaw[0][i])+"""</td><td>"""+str(dataRaw[1][i])+"""</td>
	<td>"""+str(dataRaw[2][i])+"""</td><td>"""+str(dataRaw[4][i])+"""</td><td>"""+str(dataRaw[3][i+1])+"""</td></tr>""" 

monthly=""""""
for j in range(len(monthlyTotal)):
    monthly=monthly+"""<tr><td>"""+str(j+1)+"""</td><td>"""+str(monthlyTotal[j])+"""</td></tr>"""

try:
        cfile=open('C:/rdc/table.htm', 'w')
except FileNotFoundError: 
        cfile=open('C:/rdc-master/table.htm', 'w')

cfile.writelines("""
	<!doctype html>
	<html lang='en'>
	<head>
	      <meta charset="utf-8">
	      <title>Data Chart for """+name+"""</title>
          <!--[if lt IE 9]><script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
	      <img src="img/1.jpg">
	      <img src="img/2.jpg">
	      <h1 style="font-family:courier new; color:grey"><small>Data chart for """+name+""" </small></h1>
	      <hr>
	</head>

	<body style="background-color:lightblue">

	<table border="2" style="font-family:courier new; color:blue">
	<tr>
	<th>Year</th>
	<th>Amount</th>
	<th>Rate</th>
    <th>Interest</th>
	<th>Total</th>
	</tr>
	
	"""+data+"""

	</table>
    <hr>
    <p></p>
    <h3 style="font-family:cambria">Month wise chart</h3>
    <hr>
    <table border="2" style="font-family:courier new; color:black">
    <tr>
    <th>Month number</th>
    <th>Amount at the end of the month</th>
    </tr>
    """+monthly+"""
    </table>
	</body>
	<footer>
		<p></p>
		<hr>	
		<p style="font-family:consolas; color:darkblue"><small>//AXAY</small></p>	
	</footer>
	</html> """)

cfile.close()

print("")
print("Done! Chart Created. Open 'table.htm' file to see the result")
print("")
input("Press <ENTER> to exit")
raise SystemExit
