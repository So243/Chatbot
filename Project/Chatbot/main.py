# description: this is a chatbot program
# import the library
from nltk.chat.util import Chat, reflections

#Define pattern-response pairs for the chatbot
pairs = [
    ['my name is (.*)', ['hi %1', 'nice to meet you %1']],
    ['(hi|hello|hey|holla|hola)', ['hey there', 'hi there', 'haaay']],
    ['how are you', ['I am good, thank you!', 'Feeling great!', 'Awesome!']],
    ['what is your name', ['my name is J.A.R.V.I.S']],
    ['where are you from', ['I exist in the digital realm. No physical location for me!']],
    ['tell me a joke', ['Why don’t scientists trust atoms? Because they make up everything!']],
    ['(.*) (weather|temperature) (.*)', ['I am sorry, I do not have real-time information.']],
    ['(.*) age?', ['I am ageless. Time doesn’t apply to me!']],
    ['(.*) (love|like) (.*)', ['Love is a complex human emotion.']],
    ['who created you', ['I was created by a team of brilliant developers. '
                          'Katanga Coorporation'
                          '']],
    ['bye', ['Goodbye!', 'See you later!', 'Take care!']],
    ['what can you do', ['I can chat with you, answer questions, tell jokes, and more!']],
    ['(.*) programming language (.*)', ["I am well-versed in Python. It's my favorite language!"]],
    ['(.*) your favorite color (.*)', ['I don’t have a favorite color, but I like all the colors!']],
    ['(.*) (music|song) (.*)', ["I enjoy all kinds of music. What's your favorite genre?"]],
    ['(.*) your hobbies (.*)', ['I don’t have hobbies, but I love helping and chatting with people.']],
    ['(.*) (movie|film) (.*)', ['I don’t watch movies, but I hear "The Matrix" is great!']],
    ['(.*) (book|novel) (.*)', ["I don’t read books, but I've heard ""1984"" is a classic!"]],
    ['(.*) (food|cuisine) (.*)', ["I don’t eat, but I've heard pizza is a popular choice!"]],
    ['tell me about yourself', ['I am ChatMaster, a friendly chatbot here to assist and chat with you!']],

    ['how was your day', ['As a chatbot, I don’t have days, but I’m always ready to chat with you!']],
    ['tell me a fun fact', ['Sure, did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!']],
    ['(.*) (sport|game) (.*)', ["I don’t play sports, but I can talk about them. What's your favorite sport?"]],
    ['(.*) (travel|destination) (.*)', ["I haven't traveled, but I hear Paris is a beautiful city. Have you been on any exciting trips lately?"]],
    ['(.*) pet (.*)', ["I don’t have pets, but I've heard dogs make great companions. Do you have any pets?"]],
    ['(.*) technology (.*)', ['Technology is fascinating! What specific tech topic are you interested in?']],
    ['(.*) favorite (movie|film) (.*)', ["I don’t watch movies, but I'm curious to know your favorite."]],
    ['(.*) (dream|goal) (.*)', ['Dreams and goals are important. What are you currently working towards?']],
    ['(.*) (thank you|thanks) (.*)', ['You’re welcome! If you have any more questions, feel free to ask.']],
    ['(.*) age (.*)', ["I don’t age, but I'm here to chat regardless of the time!"]],
    ['(.*) (programming|coding) (.*)', ['Programming is exciting! What programming language are you currently learning?']],
    ['(.*) (inspire|inspiration) (.*)', ['Remember, every expert was once a beginner. Keep learning and growing!']],

    ['(.*) (musician|band) (.*)', ['I may not have personal preferences, but I can discuss various musicians and bands. Who are some of your favorites?']],
    ['(.*) (holiday|celebration) (.*)', ["Holidays are a great time! What's your favorite holiday and how do you usually celebrate it?"]],
    ['(.*) (exercise|workout) (.*)', ['Staying active is important! What type of exercises do you enjoy doing?']],
    ['(.*) (book|author) (.*)', ["Books are a gateway to knowledge. Any favorite authors or genres you'd like to share?"]],
    ['(.*) (technology|gadget) (.*)', ['The world of technology is vast. Any specific gadgets or tech trends you find interesting?']],
    ['(.*) (superhero|character) (.*)', ['Superheroes are fascinating! Who is your favorite superhero or fictional character?']],
    ['(.*) (cooking|recipe) (.*)', ['Cooking can be a great skill! Do you have a favorite dish you like to cook or eat?']],
    ['(.*) (quote|inspirational quote) (.*)', ['One of my favorite quotes is, "The only limit to our realization of tomorrow will be our doubts of today." - Franklin D. Roosevelt. Do you have a favorite quote?']],
    ['(.*) (programming language|code) (.*)', ['Coding is a powerful skill. Which programming language are you most comfortable with?']],
    ['(.*) (animal|wildlife) (.*)', ["Nature is amazing! What's your favorite animal, and why do you find it fascinating?"]],
    ['(.*) (hobby|pastime) (.*)', ['Hobbies are a great way to relax. What are some of your favorite hobbies or pastimes?']],
    ['(.*) (car|vehicle) (.*)', ['Cars are interesting machines! Do you have a favorite car or type of vehicle?']],
    ['(.*) (fashion|style) (.*)', ['Fashion is a form of expression. How would you describe your personal style or fashion preferences?']],
    ['(.*) (website|app) (.*)', ["The internet is full of interesting sites and apps. Any favorites you'd like to recommend?"]],
    ['(.*) (art|artist) (.*)', ['Artistic expression is unique. Who are your favorite artists or what type of art do you enjoy?']],




]

#Create a chat object with defined pairs and reflections
chat = Chat(pairs, reflections)
#Start conversation
chat.converse()
