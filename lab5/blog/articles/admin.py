from django.contrib import admin
from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'department',
        'expense_type',
        'amount',
        'purchase_date',
        'receipt_number',
        'get_excerpt'
    )


admin.site.register(Expense, ExpenseAdmin)

