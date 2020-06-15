from django.db import models

class Cpe(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tittle = models.TextField(blank=True, null=True)
    submissions_solving_count = models.BigIntegerField(db_column='Submissions_Solving_count', blank=True, null=True)  # Field name made lowercase.
    submissions_solving = models.TextField(db_column='Submissions_Solving', blank=True, null=True)  # Field name made lowercase.
    users_solving_count = models.BigIntegerField(db_column='Users_Solving_count', blank=True, null=True)  # Field name made lowercase.
    users_solving = models.TextField(db_column='Users_Solving', blank=True, null=True)  # Field name made lowercase.
    pdf_link = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    input = models.TextField(db_column='Input', blank=True, null=True)  # Field name made lowercase.
    output = models.TextField(db_column='Output', blank=True, null=True)  # Field name made lowercase.
    sample_input = models.TextField(db_column='Sample Input', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sample_output = models.TextField(db_column='Sample output', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    difficulty = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cpe'




