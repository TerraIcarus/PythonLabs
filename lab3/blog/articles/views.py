from .models import Expense
from django.shortcuts import render


def archive(request):
    return render(
        request,
        'archive.html',
        {"posts": Expense.objects.all()}
    )

# Create your views here.
