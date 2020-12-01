from config.configuration import db,collection

def insert_dialogue(line_order, character, dialogue):
    query = {"Line_order" : f"{line_order}",
    "Character" : f"{character}", 
    "Dialogue" : f"{dialogue}" 
    }
    collection.insert_one(query)