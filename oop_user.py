from datetime import date

# Klassendiagramm

# +-----------------------------+
# |           User              |
# +-----------------------------+
# | + first_name: str           |
# | + last_name: str            |
# | + email: str                |
# | + username: str             |
# | + birth_date: date          |
# | + location: str             |
# +-----------------------------+
# | + User( first_name: str,    |
# |         last_name: str,     |
# |         email: str,         |
# |         username: str,      |
# |         birth_date: date,   |
# |         location: str       |
# |        )                    |
# | + describe_user(): None     |
# | + greet_user(): None        |
# | + age(): int                |
# +-----------------------------+

# Objektdiagramm

# +--------------------------------+
# | user1: User                    |
# +--------------------------------+
# | first_name = "Günter"          |
# | last_name = "Müller"           |
# | email = "guenter@email.de"     |
# | username = "guenterm"          |
# | birth_date = date(1996, 5, 12) |
# | location = "Berlin"            |
# +--------------------------------+


class User:
    def __init__(self, first_name, last_name, email, username, birth_date, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.birth_date = birth_date
        self.location = location

    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
        return age

    def describe_user(self):
        print(f"Benutzerprofil von {self.username}:")
        print(f"Vorname: {self.first_name}")
        print(f"Nachname: {self.last_name}")
        print(f"E-Mail: {self.email}")
        print(f"Geburtsdatum: {self.birth_date}")
        print(f"Alter: {self.age()}")
        print(f"Ort: {self.location}")

    def greet_user(self):
        print(f"Hallo {self.first_name}, willkommen zurück!")

user1 = User("Günter", "Müller", "guenter@email.de", "guenterm", date(1996, 5, 12), "Berlin")
user1.greet_user()
print()
user1.describe_user()