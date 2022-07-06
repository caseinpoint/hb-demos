"""Example of an undirected graph."""

from collections import deque
from datetime import date


class PersonNode:
    """Node in a graph representing a person."""

    def __init__(self, name, species, birthdate, adjacent=None):
        """Create a person node with friends adjacent"""

        if adjacent is None:
            adjacent = set()

        assert isinstance(adjacent, set), "adjacent must be a set!"
        assert isinstance(birthdate, date), "birthdate must be a date!"

        self.name = name
        self.species = species
        self.birthdate = birthdate
        self.adjacent = adjacent

    def __repr__(self):
        """Debugging-friendly representation"""

        return f"<PersonNode: {self.name}>"


class FriendGraph:
    """Graph holding people and their friendships."""

    def __init__(self):
        """Create an empty graph"""

        self.nodes = set()

    def __repr__(self):
        return f"<FriendGraph: { {n.name for n in self.nodes} }>"

    def add_person(self, person):
        """Add a person to our graph"""

        self.nodes.add(person)

    def set_friends(self, person1, person2):
        """Set two people as friends"""

        person1.adjacent.add(person2)
        person2.adjacent.add(person1)

    def add_people(self, people_list):
        """Add a list of people to our graph"""

        for person in people_list:
            self.add_person(person)

    def remove_person(self, person):
        """Remove a person from the graph."""

        # remove all edges that point to person
        for friend in person.adjacent:
            friend.adjacent.remove(person)

        # remove person from the graph
        self.nodes.remove(person)

    def are_connected(self, person1, person2):
        """Are two people connected? Breadth-first search."""

        possible_nodes = deque()
        seen = set()
        possible_nodes.append(person1)
        seen.add(person1)

        while len(possible_nodes) > 0:
            person = possible_nodes.popleft()
            print("checking", person)
            if person is person2:
                return True
            else:
                # for friend in person.adjacent - seen:

                for friend in person.adjacent:
                    if friend not in seen:
                        possible_nodes.append(friend)
                        seen.add(friend)
                        print("added to queue:", friend)
        return False

    def are_connected_recursive(self, person1, person2, seen=None):
        """Are two people friends? Recursive depth-first search."""

        if seen is None:
            seen = set()

        if person1 is person2:
            return True

        seen.add(person1)  # Keep track that we've visited here
        print("adding", person1)
        # check that seen is the same as other recursive calls
        print("id of seen:", id(seen))
        print("seen:", seen, '\n')

        for person in person1.adjacent:

            if person not in seen:

                if self.are_connected_recursive(person, person2, seen):
                    return True

        return False

    def verbose_are_connected_recursive(self, person1, person2, seen=None):
        """Are two people friends? Recursive depth-first search."""

        if not seen:
            seen = set()

        if person1 is person2:
            print(f"\nreturning True - {person1.name} is {person2.name}")
            return True

        seen.add(person1)  # Keep track that we've visited here
        print("adding", person1)

        for person in person1.adjacent:

            if person not in seen:

                print(
                    f"calling method on {person1.name}'s friend {person.name} with {person2.name}"
                )
                if self.verbose_are_connected_recursive(person, person2, seen):
                    print(f"\nreturning True from checking {person.name}")
                    return True

        print(f"returning False from checking {person1.name}")
        return False


# Add sample friends (apparently from Animal Crossing)
ankha = PersonNode("Ankha", "Cat", date(2002, 9, 22))
canberra = PersonNode("Canberra", "Koala", date(2002, 5, 14))
beau = PersonNode("Beau", "Deer", date(2002, 4, 5))
drake = PersonNode("Drake", "Duck", date(2002, 6, 25))
genji = PersonNode("Genji", "Rabbit", date(2002, 1, 21))
erik = PersonNode("Erik", "Deer", date(2002, 7, 27))
hamphrey = PersonNode("Hamphrey", "Hamster", date(2002, 2, 25))
ike = PersonNode("Ike", "Bear", date(2002, 4, 16))
jay = PersonNode("Jay", "Bird", date(2002, 7, 17))

friends = FriendGraph()
friends.add_people([ankha, canberra, beau, drake, erik, hamphrey, ike, jay])

friends.set_friends(ankha, canberra)
friends.set_friends(ankha, beau)
friends.set_friends(ankha, drake)
friends.set_friends(canberra, beau)
friends.set_friends(drake, canberra)
friends.set_friends(drake, genji)
friends.set_friends(beau, erik)
friends.set_friends(hamphrey, ike)
friends.set_friends(hamphrey, jay)
