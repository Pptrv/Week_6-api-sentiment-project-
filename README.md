# Week_6 Api-Sentiment-Project

![cover](Data/vader.png)

# Star Wars API

The API will have a method to introduce new data with POST and extract data with GET. 

## How does it work?
url = "http://localhost:5000/

### @POST

#### Insert a new character, line order and dialogue in the scrip. 

Endpoint
- /new_dialogue/

Params = Dialogue : "Not so far away, in a nearby galaxy"
        Character : "The Boss"
        Line_order : "1"

example:
new_post = requests.post(url_query_newpost = "http://localhost:5000/new_dialogue", data = Params)


### @GET

#### Reading a characters dialogue

Endpoint
- /dialogue/<character>

example:
vader_dialogue = 



#### Reading a characters line_orderEndpoint

Endpoint
- /line_order/<character>

example:

