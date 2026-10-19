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
                    {
                        "Name": "Zalika",
                        "Type": "friend"
                    }
                    },
            "Zalika": {
                "Age": 28,
                "Profession": "artist"},
            "John": {
                "Age": 27, 
                "Profession": "writer"},
                "Relationship": 
                    {
                        "Name": "Jill",
                        "Type": "partner"
                    }
                    {
                        "Name": "Nash",
                        "Type": "cousin" #inferred
                    }
                    },
            "Nash": {
                "Age": 34,
                "Profession": "chef"}}
