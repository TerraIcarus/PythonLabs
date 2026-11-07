from .models import Expense
from django.shortcuts import render


def archive(request):
    return render(
        request,
        'archive.html',
        {"posts": Expense.objects.all()}
    )

def get_expense(request, expense_id):
    try:
        post = Expense.objects.get(id=expense_id)

        return render(
            request,
            'expense.html',
            {"post": post}
        )

    except Expense.DoesNotExist:
        raise Http404
