from covid import Covid
import json
import time


covid=Covid()
print("""Welcome To Covid19 Tracker 
Develop By Hussain Muhammad Auwal""")
print("Note:For better Result make sure you have good internet connection,also check for country id in the countries list to avoid error!\n \n")

confirmed=covid.get_total_confirmed_cases()
active=covid.get_total_active_cases()
recovered=covid.get_total_recovered()
death=covid.get_total_deaths()
data=f"Total Confirmed Cases: {confirmed}",f"Total Active Cases: {active}",f"Total Recovered: {recovered}",f"Total Deaths: {death}"
obj=json.dumps(data,indent=2)
print("World Update")
print(obj)
while True:
	choose=input("Did you want more status for other countries? yes/no: ")
	if choose == "yes":
		print("Check country id number Here")
		data=covid.list_countries()
		obj=json.dumps(data,indent=2)
		print(obj)
		print("\n")
		id=int(input("Enter country Id number here: "))
		data=covid.get_status_by_country_id(id)
		obj=json.dumps(data,indent=2)
		print(obj)
	
	else:
		break
		
print("Stay Safe")