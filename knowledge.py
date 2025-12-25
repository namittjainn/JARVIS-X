import wikipedia

def search_web(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except:
        return "Sorry, I could not find information."
