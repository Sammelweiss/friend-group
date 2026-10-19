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
                "Profession": "writer"},
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
