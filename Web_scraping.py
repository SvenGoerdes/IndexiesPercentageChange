from bs4 import BeautifulSoup as soup ### parse the html 
from urllib.request import urlopen as uReq  ### is gonna grap the URL
import pandas as pd

my_url = 'https://de.finance.yahoo.com/world-indices'

## grabs the page 
uclient = uReq(my_url)

## makes it to a variable 
page_html = uclient.read()

uclient.close()

## Html parsing 
page_soup = soup(page_html, "html.parser") ### we have to declare it as a html file 

## finds everything 
percantage= page_soup.findAll("td",{"class":"data-col4 Ta(end) Pstart(20px)"})

names = page_soup.findAll("td",{"class":"data-col1 Ta(start) Pend(10px)"})

table = page_soup.findAll("table",{"class":"yfinlist-table W(100%) BdB Bdc($tableBorderGray)"})









namesstring = []

for name in names:
    namesstring.append(str(name))


Index = []
for getword in namesstring:
    fillerget = getword.split('<td class="data-col1 Ta(start) Pend(10px)" data-reactid="')
    fillerget2 = fillerget[1].split(">")
    fillerget3 = fillerget2[1].split("<")
    Index.append(fillerget3[0])
    

percstring = []




for perc in percantage:
    percstring .append(str(perc))


Finalpercentage = [] ### list to extract the percantage change. Either positive or negative 

for getpercantage in percstring:
    fillerget = getpercantage.split('<td class="data-col4 Ta(end) Pstart(20px)" data-reactid=')
   	
    fillerget2 = fillerget[1].split('>')
    fillerget3 = fillerget2[2].split("<")
    Finalpercentage.append(fillerget3[0])
    





### Create a dictionary 

Growth = {"Names": Index,
          "Percentage": Finalpercentage 
            
             }

             
df = pd.DataFrame(Growth, columns = ['Names', 'Percentage'])

### Creates html file 

html = df.to_html()
text_file = open("percantage.html", "w")
text_file.write(html)
text_file.close()
