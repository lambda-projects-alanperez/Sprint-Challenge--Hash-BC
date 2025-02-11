#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for x in tickets:
        hash_table_insert(hashtable, x.source, x.destination)

    for y in range(length):

        if y == 0:
            route[y] = hash_table_retrieve(hashtable, "NONE")
        else:
            route[y] = hash_table_retrieve(hashtable, route[y - 1])
    return route
