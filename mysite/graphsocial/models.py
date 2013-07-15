from neo4django.db import models

class Person(models.NodeModel):
    name = models.StringProperty()
    age = models.IntegerProperty()

    friends = models.Relationship('self',rel_type='friends_with')
    def __unicode__(self):
        return self.name


class OnlinePerson(Person):
    email = models.EmailProperty()
    homepage = models.URLProperty()

class EmployedPerson(Person):
    job_title = models.StringProperty(indexed=True)

class Pet(Person):
    owner = models.Relationship(Person,
                                rel_type='owns',
                                single=True,
                                related_name='pets'
                               )
    def __unicode__(self):
        return self.name



