book = dict()

book['apple'] = 0.67
book['milk'] = 1.49
book["avocado"] = 1.49

print(book)
print(book['avocado'])

# check if someone has voted without scanning whole list

voted = {}

def check_voter(name):
    if voted.get(name):
        print("Kick the Republican out")
    else:
        voted[name] = True
        print("Let them vote")

check_voter("Charlie")
check_voter("Elijah")
check_voter("Charlie")

# websites uses hash tables as cache - i.e. pages that will appear the same to everyone are stored as a hashed value for instant retrieval

cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url] # returns cached data
    else:
        data = get_data_from_server(url) # saves this data to the cache first
        cache[url] = data
        return data