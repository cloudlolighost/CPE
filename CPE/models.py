from django.db import models


class Cpe(models.Model):
    id = models.IntegerField()
    tittle_num = models.IntegerField(primary_key=True)
    tittle = models.CharField(max_length=50)
    submissions_solving_count = models.IntegerField(db_column='Submissions_Solving_count')  # Field name made lowercase.
    submissions_solving = models.CharField(db_column='Submissions_Solving', max_length=15)  # Field name made lowercase.
    users_solving_count = models.IntegerField(db_column='Users_Solving_count')  # Field name made lowercase.
    users_solving = models.CharField(db_column='Users_Solving', max_length=15)  # Field name made lowercase.
    pdf_link = models.TextField()
    text = models.TextField()
    description = models.TextField()
    input = models.TextField(db_column='Input')  # Field name made lowercase.
    output = models.TextField(db_column='Output')  # Field name made lowercase.
    sample_input = models.TextField(db_column='Sample_Input')  # Field name made lowercase.
    sample_output = models.TextField(db_column='Sample_output')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cpe'


