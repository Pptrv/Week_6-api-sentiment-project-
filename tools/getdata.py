from config.configuration import db, collection

def dialogue_character(name):
    query = {"Character" : f"{name}"}
    star_wars = list(collection.find(query, {"_id":0}))
    return star_wars

 

def order_character_dialogue(lines):
    query = {"Line_order" : f"{lines}"}
    star_wars = list(collection.find(query, {"_id":0}))
    return star_wars


def sentimentAnalysisPolarity(sentence):
    query = {"Dialogue" : f"{sentence}"}
    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(sentence)
    polarity_charact = collection.apply(sentimentAnalysisPolarity)
    return polarity_charact 

def sentimentAnalysisCompound(sentence):
    query = {"Dialogue" : f"{sentence}"}
    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(sentence)
    pol = polarity['compound']
    compound_charact = collection.apply(sentimentAnalysisCompound)
    return compound_charact