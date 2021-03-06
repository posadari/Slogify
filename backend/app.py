import flask 
import openai as ai
import json


app = flask.Flask("__main__")


# Import API-key
the_api_key = "sk-s0ju0lLCmSYVymwqIkRilbBd49gwzrxXoAKxl4ZZ"

ai.api_key = the_api_key

# Get User Input 
companyName = "Name: " + input("\nWhat is the name of your business: ")
print (companyName)


# Import text prompt
with open("prompt.txt") as pro:
	prompten = pro.read()

#concatanate to prompten data
prompten = prompten + companyName

# The Model
returns = ai.Completion.create(
    engine="davinci", # OpenAI has made four text completion engines available, named davinci, ada, babbage and curie. We are using davinci, which is the most capable of the four.
	prompt=prompten, # The text we will use as input
    max_tokens=500, # maximum completion length.
	temperature=0.7, # a number between 0 and 1 that determines how many creative risks the engine takes when generating text.,
	top_p=1, # an alternative way to control the originality and creativity of the generated text.
	n=1, #
	frequency_penalty=0.2, # a number between 0 and 1. The higher this value the model will make a bigger effort in not repeating itself.
	presence_penalty=0.9 # a number between 0 and 1. The higher this value the model will make a bigger effort in talking about new topics.
	#stream=False,
)

text = returns['choices'][0]['text']

print(text)

# function to return input
@app.route("/")
def my_index():
    return flask.render_template("index.html", token=text)

app.run(debug=True)