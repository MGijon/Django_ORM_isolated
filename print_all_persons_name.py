from db.models import Person

for person in Person.objects.all():
    print(person.name)
