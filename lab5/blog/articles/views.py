from .models import Expense
from django.shortcuts import render, redirect


def archive(request):
    return render(
        request,
        'archive.html',
        {"posts": Expense.objects.all()}
    )

def get_expense(request, expense_id):
    try:
        post = Expense.objects.get(id=expense_id)
        return render(request, 'expense.html', {'post': post})
    except Expense.DoesNotExist:
        raise Http404


def create_expense(request):

    if not request.user.is_authenticated:
        raise Http404

    if request.method == "POST":

        form = {
            'expense_type': request.POST.get('expense_type', '').strip(),
            'purchase_date': request.POST.get('purchase_date', ''),
            'department': request.POST.get('department', '').strip(),
            'amount': request.POST.get('amount', ''),
            'receipt_number': request.POST.get('receipt_number', '').strip()
        }

        if not all(form.values()):
            form['errors'] = "Не все поля заполнены"
            return render(request, 'create_expense.html', {'form': form})

        if Expense.objects.filter(
            receipt_number=form['receipt_number']
        ).exists():
            form['errors'] = "Покупка с таким номером телефона уже существует"
            return render(request, 'create_expense.html', {'form': form})

        try:
            post = Expense.objects.create(
                expense_type=form['expense_type'],
                purchase_date=form['purchase_date'],
                department=form['department'],
                amount=form['amount'],
                receipt_number=form['receipt_number'],
                employee=request.user
            )

            return redirect('get_expense', expense_id=post.id)

        except (ValueError, TypeError, IntegrityError):
            form['errors'] = "Проверьте правильность введенных данных"
            return render(request, 'create_expense.html', {'form': form})

    return render(request, 'create_expense.html', {})