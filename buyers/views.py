from django.contrib.auth.models import User
from django.http import HttpResponse


def show_users(request):
    users = User.objects.all()
    result = ''

    for user in users:
        result += f'<h1>{user.username}</h1>'

    result += "<style>body{padding: 10px; margin: 0; font-family: sans-serif; background-color: #262626;}" \
              "h1{font-size: 5vh; color: #eee;}</style>"
    return HttpResponse(result)
