import datetime

from django.shortcuts import render

DAYS = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
MONTHS = ["січня", "лютого", "березня", "квітня", "травня", "червня",
          "липня", "серпня", "вересня", "жовтня", "листопада", "грудня"]


def index(request):
    context = {"title": "Hello World"}
    return render(request, "helloweb/index.html", context)


def current_datetime(request):
    now = datetime.datetime.now()
    context = {
        "title": "Дата і час",
        "time": now.strftime("%H:%M:%S"),
        "day_name": DAYS[now.weekday()],
        "day": now.day,
        "month_name": MONTHS[now.month - 1],
        "year": now.year,
        "week": now.isocalendar()[1],
    }
    return render(request, "helloweb/datetime.html", context)


def about(request):
    context = {
        "title": "Про мене",
        "skills": [
            ("Мова", "Python"),
            ("Фреймворк", "Django"),
            ("Редактор", "PyCharm"),
        ],
    }
    return render(request, "helloweb/about.html", context)