from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)


ban_words = []
file = open("2.txt", encoding="utf-8")
for line in file:
    s = line.strip()
    ban_words.append(s)
file.close()

messages = []

file = open("23.txt", encoding="utf-8")
for line in file:
    if len(line) > 3:
        messages.append(line[:-1].lower())
file.close()
            
results = model.predict(messages, k=5)
for message, sentiment in zip(messages, results):
    positive = round(sentiment["positive"], 5)
    negative = round(sentiment["negative"], 5)
    neutral = round(sentiment["neutral"], 5)
    speech = round(sentiment["speech"], 5)
    skip = round(sentiment["skip"], 5)
    m = max(positive, negative, neutral, speech, skip)
    print(message, end="->")
    k = False
    for i in ban_words:
        if i in message:
            k = True
            break
    if m == negative or negative > 0.5 or k:
        print("Yes")
    else:
        print("No")
    
