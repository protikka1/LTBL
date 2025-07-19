try:
    from django.shortcuts import render, redirect
except ImportError:
    # Mock for testing outside Django
    def render(*args, **kwargs): pass
    def redirect(*args, **kwargs): pass

from .firebase_config import auth


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            auth.create_user_with_email_and_password(email, password)
            return redirect('login')
        except Exception as e:
            return render(request, 'signup.html', {'error': str(e)})
    return render(request, 'signup.html')
