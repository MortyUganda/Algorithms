from collections import deque

base_man_names = "abbey, abram acker adair adam adams adamson addison adkins aiken akerman akers albert albertson albinson alexander alfredson alger alvin anderson andrews ansel"

graph = {}
graph['you'] = ["Bill", 'Sofia', 'Ben', "albertson", "ansel"]
graph['Bill'] = ['Maria']
graph['Sofia'] = []
graph['Ben'] = []

def person_is_seller(name):
    if name in base_man_names.split():
        return True
    return False

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is founded!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search('you')