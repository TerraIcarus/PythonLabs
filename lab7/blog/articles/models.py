from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    department = models.CharField(max_length=200)
    expense_type = models.CharField(max_length=200)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    purchase_date = models.DateField(auto_now_add=True)
    receipt_number = models.CharField(max_length=11, unique=True)

    def __unicode__(self):
        return "%s: %s руб." % (
            self.employee.username,
            self.amount
        )
    
    def get_excerpt(self):
        return "%s — %s" % (
            self.expense_type,
            self.department
        )
