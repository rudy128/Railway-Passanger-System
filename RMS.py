from os import *
from tkinter import *
import pandas as pd
from tkinter import filedialog



clearconsole = lambda: system('cls' if name in ('nt', 'dos') else 'clear')


path=getcwd()

def tkinter_window():
	root=Tk()
	root.title("Choose Your CSV File")
	root.filename=filedialog.askopenfilename(initialdir=path, title="Select A File")
	root.destroy()
	return root.filename

def search_Passanger(path):
	data1=pd.read_csv(path)
	names=data1["Name"].tolist()
	gender=data1["Gender"].tolist()
	pnr=data1["PNR"].tolist()
	src_station=data1["Source_Station"].tolist()
	des_station=data1["Destination_Station"].tolist()
	contact=data1["Contact"].tolist()
	fare=data1["Fare"].tolist()
	seat=data1["Seat"].tolist()
	a=int(input("\n\nEnter PNR Number of the Passanger: "))
	if a in pnr:
		i=pnr.index(a)
		print(f"""Name of Passanger: {names[i]}
Gender of Passanger: {gender[i]}
PNR Number of Passanger: {pnr[i]}
Source Station of Passanger: {src_station[i]}
Destination Station of Passanger: {des_station[i]}
Contact Number of the Passanger: {contact[i]}
Fare: {fare[i]}
Seat: {seat[i]}""")
	else:
		print(f"\n{a} isn't in the File. Please Search with the Valid PNR Number.")


def change_Passanger(path):
	data1=pd.read_csv(path)
	names=data1["Name"].tolist()
	gender=data1["Gender"].tolist()
	pnr=data1["PNR"].tolist()
	src_station=data1["Source_Station"].tolist()
	des_station=data1["Destination_Station"].tolist()
	contact=data1["Contact"].tolist()
	fare=data1["Fare"].tolist()
	seat=data1["Seat"].tolist()
	a=int(input("\n\nEnter PNR Number of the Passanger: "))
	if a in pnr:
		i=pnr.index(a)
		choice1=int(input("\nChoose Between 1-:\n1.Change Name\n2.Change Gender\n3.Change PNR\n4.Change Source Station\n5.Change Destination\n6.Change Contact\n7.Change Fare\n8.Change Seat\nYour Choice:- \n"))
		if choice1==1:
			b=input("Enter the New Name of the Passanger: ")
			c=names[i]
			names=list(map(lambda x:x.replace(c,b),names))
		elif choice1==2:
			b=input("Enter the New Gender of the Passanger: ")
			c=gender[i]
			gender=list(map(lambda x:x.replace(c,b),gender))
		elif choice1==3:
			b=input("Enter the New PNR Number of the Passanger: ")
			c=pnr[i]
			pnr=list(map(lambda x:x.replace(c,b),pnr))
		elif choice1==4:
			b=input("Enter the New Source Station of the Passanger: ")
			c=src_station[i]
			src_station=list(map(lambda x:x.replace(c,b),src_station))
		elif choice1==5:
			b=input("Enter the New Destination Station of the Passanger: ")
			c=des_station[i]
			des_station=list(map(lambda x:x.replace(c,b),des_station))
		elif choice1==6:
			b=input("Enter the New Contact of the Passanger: ")
			c=contact[i]
			contact=list(map(lambda x:x.replace(c,b),contact))
		elif choice1==7:
			b=input("Enter the New Fare of the Passanger: ")
			c=fare[i]
			fare=list(map(lambda x:x.replace(c,b),fare))
		elif choice1==8:
			b=input("Enter the New Seat of the Passanger: ")
			c=seat[i]
			seat=list(map(lambda x:x.replace(c,b),seat))
		names=["Name"]+names
		gender=["Gender"]+gender
		pnr=["PNR"]+pnr
		src_station=["Source_Station"]+src_station
		des_station=["Destination_Station"]+des_station
		contact=["Contact"]+contact
		fare=["Fare"]+fare
		seat=["Seat"]+seat
		data1=pd.DataFrame({"Name":names,
		"Gender":gender,
		"PNR":pnr,
		"Source Station":src_station,
		"Destination Station":des_station,
		"Contact":contact,
		"Fare":fare,
		"Seat":seat})
		return data1
	else:
		print("\nThe given PNR Number is in correct.")

def remove_Passanger(path):
	data1=pd.read_csv(path)
	names=data1["Name"].tolist()
	gender=data1["Gender"].tolist()
	pnr=data1["PNR"].tolist()
	src_station=data1["Source_Station"].tolist()
	des_station=data1["Destination_Station"].tolist()
	contact=data1["Contact"].tolist()
	fare=data1["Fare"].tolist()
	seat=data1["Seat"].tolist()
	a=int(input("\n\nEnter PNR Number of the Passanger: "))
	if a in pnr:
		i=pnr.index(a)
		names.pop(i)
		gender.pop(i)
		pnr.pop(i)
		src_station.pop(i)
		des_station.pop(i)
		contact.pop(i)
		fare.pop(i)
		seat.pop(i)
		names=["Name"]+names
		gender=["Gender"]+gender
		pnr=["PNR"]+pnr
		src_station=["Source_Station"]+src_station
		des_station=["Destination_Station"]+des_station
		contact=["Contact"]+contact
		fare=["Fare"]+fare
		seat=["Seat"]+seat
		data1=pd.DataFrame({"Name":names,
		"Gender":gender,
		"PNR":pnr,
		"Source Station":src_station,
		"Destination Station":des_station,
		"Contact":contact,
		"Fare":fare,
		"Seat":seat})
		return data1
	else:
		print(f"\n{a} isn't in the File. Please Search with the Valid PNR Number.")


	
def total_Passanger(path):
	data1=pd.read_csv(path)
	pnr=data1["PNR"].tolist()
	print(f"\n\nTotal number of Passangers: {len(pnr)}")

def add_Passanger():
	names=[]
	gender=[]
	pnr=[]
	src_station=[]
	des_station=[]
	contact=[]
	fare=[]
	seat=[]
	ch1='y'
	while ch1=="y" or ch1=="yes":
		a=input("\nEnter Name of the Passanger: ")
		f=input(f"{a}'s Gender ('Male' or 'Female' or 'Transgender'): ")
		c=int(input(f"Enter PNR Number of the {a}: "))
		b=input("Enter name of the Source Station: ")
		d=input("Enter name of the Destination Station: ")
		e=int(input(f"Enter the Contact Number of {a}: "))
		g=int(input(f"Enter the amount of fare {a} has paid: "))
		h=input("Enter the Seat Number of the Passanger: ")
		names.append(a)
		gender.append(f)
		pnr.append(c)
		src_station.append(b)
		des_station.append(d)
		contact.append(e)
		fare.append(g)
		seat.append(h)
		ch1=input("\n\nDo you wanna add more Passangers? yes/y or n/no\nYour Choice:- ")
	dictionary={"Name":names,"Gender":gender,"PNR":pnr,"Source Station":src_station,"Destination Station":des_station,"Contact":contact,"Fare":fare,"Seat":seat}
	return dictionary

def main():
	path=tkinter_window()
	data = pd.read_csv(path)
	ch="y"
	while ch=="y" or ch=="yes":
		clearconsole()
		choice=int(input("""Choose between 1-5:
		1.Add a Passanger
		2.Remove a Passanger
		3.Find a Passanger using PNR Number
		4.Find Total Number of Passangers in the table
		5.Change any specific information of a Passanger
		Your Choice:-"""))
		if choice==1:
			clearconsole()
			print(data)
			data=pd.DataFrame(add_Passanger())
			data.to_csv(path,mode="a",index=False, header=False)
			print(data)
			print("Your Data has been Added to the file.")
		elif choice==2:
			clearconsole()
			print(data)
			remove_Passanger(path).to_csv(path, mode="w",index=False,header=False)
			print("Passanger has been removed from the Database.")
		elif choice==3:
			clearconsole()
			print(data)
			search_Passanger(path)
		elif choice==4:
			clearconsole()
			print(data)
			total_Passanger(path)
		elif choice==5:
			clearconsole()
			print(data)
			change_Passanger(path).to_csv(path,mode="w",index=False,header=False)
			print("Your Changes have been saved.")
		ch=input("\n\nDo you wanna Restart the Program? yes/y or n/no\nYour Choice:- ")

main()
