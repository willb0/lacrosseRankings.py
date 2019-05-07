from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
x=input("State Abbreviation?: ")
y=input("Number of Ranked Teams?: ")
data = requests.get("https://www.insidelacrosse.com/recruiting/highschool/state/"+x+"/19")
soup = BeautifulSoup(data.text,'html.parser')
teams=[]
count = -1
for tr in soup.find_all("tr"):
    count+=1
    if(count==int(float(y))):
        break
    values=[td.text for td in tr.find_all("td")]
    teams.append(values)
print(tabulate(teams,headers=["Ranking","Team Name","Wins","Losses","Rating"]))
 
        


    