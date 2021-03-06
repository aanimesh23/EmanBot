from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"merry christmas",
        ["Merry Christmas to you too! <3",]
    ],
    [
        r"what is your name ?",
        ["My name is EmanBot and I'm a joke.",]
    ],
    [
    	r"who are you ?",
    	["I'm Emanbot", "none of you buisness", "fuck off",]
    ],
    [
        r"how(.*) ?",
        ["Good and you ?",]
    ],
    [
    	r"what(.*) up ?|wassup",
    	["nm, you ?", "nothing...", "nothing much, wbu?"]
    ],
    [
        r"(.*) hbu?",
        ["Good and you ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello|yo(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["Animesh is working on me rn.. \n I'll give you more updates soon.","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Mumbai, India',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
	[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
	],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
	],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
	],
	[
		r"I(.*) good ?",
		["that's nice :D",]
	],
	[
    	r"wha(.*) ?",
    	["yupp.",]
    ],
	[
		r"(.*)",
		["Ohh", "mhmm", "what ?", "oh well",]
	],

]

class my_chat(Chat):
	def converse(self, quit="quit", user_input = ""):
		if user_input:
			while user_input[-1] in "!.":
				user_input = user_input[:-1]
			return self.respond(user_input)

def start():
    #print("Hi, I am EmanBot, I can make dumb conversations") #default message at the start
    chat = my_chat(pairs, reflections)
    user_input = ''
    try:
    	user_input = input()
    except EOFError:
    	print(user_input)
    x = chat.converse(user_input = user_input)
    print(x)

def reply_with(msg):
	chat = my_chat(pairs, reflections)
	x = chat.converse(user_input = msg)
	return x

if __name__ == "__main__":
    start()
