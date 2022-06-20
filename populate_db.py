from db.models import Person

for i in range(100):
    Person(name=f"name_from_script_{i}").save()
