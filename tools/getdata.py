from config.configuration import db, collection

def dialogue_character(name):
    query = {"Character" : f"{name}"}
    star_wars = list(collection.find(query, {"_id":0}))
    return star_wars

 

 def order_character_dialogue(lines):
    query = {"Line Order" : f"{lines}"}
    star_wars = list(collection.find(query, {"_id":0}))
    return star_wars