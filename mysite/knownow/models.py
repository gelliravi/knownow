from neo4django.db import models

class Person(models.NodeModel):
    name = models.StringProperty()

class Knowledge(models.NodeModel):
    content = models.StringProperty()
    date = models.IntegerProperty()
    referalKnowledge = models.Relationship('self',rel_type='refer_to')
    provider = models.Relationship('Person',rel_type='has_provided')
    def __unicode__(self):
        return self.content


