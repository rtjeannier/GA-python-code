'''
Getting Data from APIs
What is an API?
- Application Programming Interface
- Structured way to expose specific functionality and data access to users
- Web APIs usually follow the "REST" standard
How to interact with a REST API:
- Make a "request" to a specific URL (an "endpoint"), and get the data back in a "response"
- Most relevant request method for us is GET (other methods: POST, PUT, DELETE)
- Response is often JSON format
- Web console is sometimes available (allows you to explore an API)

For this example we will be using SWAPI - the Star Wars API. 
This API is very user-friendly and an easy tool to learn with.
https://swapi.co/
Check out the documentation to get started
'''

# use requests library to interact with a URL
import requests

#based on the documentation, https://swapi.co/documentation, what is this requesting
full_request_url = 'http://swapi.co/api/starships'

r = requests.get(full_request_url)

# check the status: 200 means success, 4xx means error
r.status_code

# view the raw response text
r.text

# decode the JSON response body into a dictionary
r.json()

#Based on the output, how would I select just the reuslts?

results = 

# We can even turn this dictionary into a dataframe
import pandas as pd
df = pd.DataFrame(results)
 


# We can use functions or for loops to make multiple requests in a row
# for example, how would I write a four loop to select the first ten people ids
# check out the documentation!

people = []

for i in range():
    html= ''.format()
    x = requests.get(html)
    people.append(x.json())

# We can also turn this into a dataframe
df_people = pd.DataFrame(people)

# How would I save my new dataframe as a CSV so I can import it later?

