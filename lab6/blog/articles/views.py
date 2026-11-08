from .models import Expense
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login


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
            form['errors'] = "Проверьте правильность введенных данных или уникальность номера чека"
            return render(request, 'create_expense.html', {'form': form})

    return render(request, 'create_expense.html', {})

def register(request):

    if request.method == "POST":

        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        if not username or not email or not password:
            return render(request, 'register.html', {
                'error': 'Все поля должны быть заполнены',
                'username': username,
                'email': email
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Пользователь с таким логином уже существует',
                'username': username,
                'email': email
            })

        User.objects.create_user(username, email, password)

        return render(request, 'register.html', {
            'success': 'Регистрация прошла успешно'
        })

    return render(request, 'register.html')

def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username or not password:
            return render(request, 'login.html', {
                'error': 'Заполните все поля'
            })

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect('archive')

        else:
            return render(request, 'login.html', {
                'error': 'Такого аккаунта не существует или введен неправильный пароль'
            })

    return render(request, 'login.html')