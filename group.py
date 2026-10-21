"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

"""
friendgroup
- friend
   - age
   - profession
   - relationship(dict)
       - otherfriendname
           - relationship
           - connection

"""

my_group = {"Jill": {
                "Age": 26,
                "Profession": "biologist",
                "Relationship": 
                    [{
                        "Name": "Zalika",
                        "Type": "friend"
                    },
                    {
                        "Name": "John",
                        "Type": "partner"
                    }]
                    },
            "Zalika": {
                "Age": 28,
                "Profession": "artist",
                "Relationship": 
                    [{
                        "Name": "Jill",
                        "Type": "friend"
                    },
                    #inferred frmo Nash
                    {
                        "Name": "Nash",
                        "Type": "tenant"
                    }]
                     },
            "John": {
                "Age": 27, 
                "Profession": "writer",
                "Relationship": 
                    [{
                        "Name": "Jill",
                        "Type": "partner"
                    },
                    {
                        "Name": "Nash",
                        "Type": "cousin" #inferred
                    }]
                    },
            "Nash": {
                "Age": 34,
                "Profession": "chef",
                "Relationship": 
                    [{
                        "Name": "John",
                        "Type": "cousin"
                    },
                    {
                        "Name": "Zalika",
                        "Type": "landlord"
                    }]
                    }
}           


# this was a test, does not work properly
"""
def add_person() :
    my_group.update({"Jill": {
                "Age": 26,
                "Profession": "biologist",
                "Relationship": 
                    [{
                        "Name": "Zalika",
                        "Type": "friend"
                    },
                    {
                        "Name": "John",
                        "Type": "partner"
                    }]
                    }
                }
    )
"""

# define a function to add a person, with some default values
def add_person(name="New person", age=20, profession="default", relationship=[]) :
    my_group.update({name: {
                "Age": age,
                "Profession": profession,
                "Relationship": relationship
                        }
                }
    )

#testing adding a person
add_person()
#need to create a list of relations for the new person
relation_list =[{"Name": "John","Type": "teacher"}]
add_person("Diego", 35, "researcher", relation_list)

#trying to add with the relationship inside
add_person("Katie", 36, "postdoc", [{"Name": "Yana","Type": "friend"}])


#
# new section on comprehensions
"""
Task requirement
comprehension expressions to your group.py file so that it prints out the following when the script is run:
    the maximum age of people in the group
    the average (mean) number of relations among members of the group
    the maximum age of people in the group that have at least one relation
    [more advanced] the maximum age of people in the group that have at least one friend
"""

# testing extracting info
# Person
my_group["Jill"]
# age
my_group["Jill"]["Age"]
# code, extracting with for loop
age_list = [] # create list of ages
for person in my_group:
    print (person)
    print (my_group[person])
    print (my_group[person]["Age"])
    age_list.append (my_group[person]["Age"])
#    print (age)
        