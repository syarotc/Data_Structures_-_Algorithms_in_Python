"""input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)"""

manatees = [
    {
        "name": "First",
        "age": 1
    },
    {
        "name": "Second",
        "age": 2
    },
    {
        "name": "Third",
        "age": 5
    },
    {
        "name": "Fourth",
        "age": 4
    },
    {
        "name": "Fifth",
        "age": 3
    }
]


def example1(manatees):
    if manatees is None:
        manatees = manatees
    for manatee in manatees:
        print(manatee["name"])


def example2(manatees):
    print(manatees[0]["name"])
    print(manatees[0]["age"])


def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print(manatee_property, ": ", manatee[manatee_property])


def example4(manatees):  # wrong behaviour
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print(oldest_manatee)


def example4_correct(manatees):  # correct behaviour
    try:
        oldest_manatee = manatees[0]
        for manatee2 in manatees:
            if oldest_manatee["age"] < manatee2["age"]:
                oldest_manatee = manatee2
        print(oldest_manatee["name"])
    except KeyError:
        print("No manatees here!")
    except TypeError:
        print("manatees must be a dict")


# example1(manatees)  # O(n)
# example2(manatees)  # O(1)
# example3(manatees)  # O(nm)
# example4(manatees)  # O(n^2)
example4_correct(manatees)
