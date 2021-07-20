contacts = {"number": "4",
            "students": [{"name": "Jo Yu", "email": "joleneyu@abc.com"},
                         {"name": "Ed Kim", "email": "ekim@abc.com"},
                         {"name": "Nelson Lim", "email": "nellim@abc.com"},
                         {"name": "Rose Kim", "email": "rosekim@abc.com"}
                        ]
}
for contact in contacts:
    print(contacts["students"])

for student in contacts["students"]:
    print(student["email"])
