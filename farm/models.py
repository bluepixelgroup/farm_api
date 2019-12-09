from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=70, blank=False, default='')
    middle_name = models.CharField(max_length=70, blank=True, null=True)
    last_name = models.CharField(max_length=70, blank=False, default='')
    age = models.CharField(max_length=70, blank=False, default='')
    gender = models.CharField(max_length=70, blank=False, default='')

    class Meta:
        db_table = "Person"
        indexes = [
            models.Index(fields=['first_name'], name='first_name_idx')
        ]
        unique_together = [['first_name', 'middle_name', 'last_name', 'age']]

    def __str__(self):
        return 'Person({} {} {})'.format(
            self.first_name,
            self.middle_name,
            self.last_name
        )


class Fieldman(models.Model):
    person = models.OneToOneField(Person, on_delete=models.PROTECT, null=False, related_name='fieldman')

    class Meta:
        db_table = "Fieldman"
        indexes = [
            models.Index(fields=['person'], name='Fieldman_idx')
        ]

    def __str__(self):
        return 'Fieldman({} {} {})'.format(
            self.person.first_name,
            self.person.middle_nane,
            self.person.last_name
        )


class Farmer(models.Model):
    person = models.OneToOneField(Person, on_delete=models.PROTECT, null=False, related_name='farmer')
    farmer_code = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        db_table = "Farmer"
        indexes = [
            models.Index(fields=['farmer_code'], name='ryot_code_idx'),
        ]

    def __str__(self):
        return 'Farmer({} {} {}) - {}'.format(
            self.person.first_name,
            self.person.middle_nane,
            self.person.last_name,
            self.farmer_code
        )


class PersonFamily(models.Model):
    relationship_types = [
        ('FR', 'Father of'),
        ('MR', 'Mother of'),
        ('SR', 'Son of'),
        ('DR', 'Daughter of'),
        ('BR', 'Brother of'),
        ('TR', 'Sister of'),
        ('GR', 'grandson of'),
        ('HR', 'husband of'),
        ('WR', 'wife of'),
    ]

    person = models.ForeignKey(Person, on_delete=models.PROTECT, null=False)
    relative_of = models.ForeignKey(Person, on_delete=models.PROTECT, null=False, related_name='relatives')
    relation_type = models.CharField(max_length=32, choices=relationship_types)


    class Meta:
        db_table = "PersonFamily"
