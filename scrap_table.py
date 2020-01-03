import requests
import pandas as pd
from bs4 import BeautifulSoup

url_to_web = 'https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)'
# view the data from requests
data = requests.get(url_to_web)
print(f'Data from provided url\n {data.content}')
# if succesful, parse results to beautifulsoup for further processing
soup_obj = ''
if data.status_code == 200:
    soup_obj = BeautifulSoup(data.content, "html.parser")

# find table by html class name
table = soup_obj.find('table',{'class':'wikitable sortable'}) # search element of type table and class wikitable sortable

new_table = []
for row in table.find_all('tr')[1:]:
    column_marker = 0
    columns = row.find_all('td')# individual cell per row
    new_table.append([column.get_text() for column in columns])

print(f'View scrapped table\n {new_table}')
# convert the list of lists to pd dataframe

df = pd.DataFrame(new_table, columns=['ContinentCode','Alpha2','Alpha3','PhoneCode','Name'])
df['Name'] = df['Name'].str.replace('\n','') # cleaning
print(df)
pandas_result =  pd.read_html(url_to_web)
print(f'Dataframe using pandas.read_html\n{pandas_result[2]}')