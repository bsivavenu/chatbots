import nltk
from nltk.corpus import wordnet
import re

list_words=['hello','describe','role','website','help', 'operate','refund','located']

dict_syn={}

for word in list_words:
    print(word)
    synonyms=[]
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            synonyms.append(lem.name())
    # print(set(synonyms))
    dict_syn[word]=set(synonyms)




keywords={}

keywords['greet']=[]

for synonym in list(dict_syn['hello']):
    keywords['greet'].append('.*\\b'+synonym+'\\b.*')
keywords['about_chatbot']=[]

keywords['about_chatbot'].append('.*who.*you.*')
for synonym in list(dict_syn['describe']):
    keywords['about_chatbot'].append('.*\\b'+synonym+'\\b.*'+'\\byourself\\b'+'.*')
    keywords['about_chatbot'].append('.*\\b'+synonym+'\\b.*'+'\\byourself\\b'+'.*')
    
    keywords['about_chatbot'].append('.*\\b'+synonym+'\\b.*'+'\\byou\\b'+'.*')
    keywords['about_chatbot'].append('.*\\b'+synonym+'\\b.*'+'\\byou\\b'+'.*')
# ..........CREATE FURTHER RULES................
# ...............................................


patterns={}

for intent, keys in keywords.items():
    patterns[intent]=re.compile('|'.join(keys))


responses={
    'greet':'Hello! How can I help you?',
    'about_chatbot':'Hi, My name is Sam. I am here to help you out',
    'role': 'I help people in understanding functionality of our product website. I also assist the end user in purchasing and refunding our product',
    'about_site':'We help people around the world to celebrate important occassions with a special gift.',
    'site_functionality':'Please use the menu on the top to navigate and explore different gift categories. We specialize in anniversary gifts, birthday gifts, and other types of gifts',
    'refund':'Well, we value our customers. You can refund the amount if you return it back within a day. For more information explore our refund section on this link: ____',
    'located_in':'We are based in ______ near _____',
    'default':'Please rephrase...'
}

def match_intent(message):
    print(message)
    matched_intent = None
    
    for intent,pattern in patterns.items():
        if re.search(pattern,message):
            matched_intent=intent
    return matched_intent

def respond(message):
    intent=match_intent(message)
    
    key='default'
    
    if intent in responses:
        key=intent
    
    return responses[key]

def send_message(message):
    return respond(message)


# send_message("hello, hope you are good")
# send_message("hello hi ")
send_message("your role please")
send_message("what is your purpose here???")








