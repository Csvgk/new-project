import datetime

from django.http import HttpResponse
from django.urls import reverse

STYLE = """
<style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        font-family: -apple-system, "Segoe UI", Roboto, sans-serif;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: #fff;
    }

    /* Навігація */
    nav {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 8px;
        padding: 16px;
        background: rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(12px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    }
    nav a {
        color: #fff;
        text-decoration: none;
        padding: 10px 20px;
        border-radius: 999px;
        font-weight: 500;
        transition: background 0.2s;
    }
    nav a:hover { background: rgba(255, 255, 255, 0.2); }
    nav a.active { background: #fff; color: #764ba2; font-weight: 700; }

    /* Контент */
    main {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
    }
    .card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px;
        padding: 40px 50px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25);
        max-width: 480px;
        width: 100%;
    }
    h1 { font-size: 2.4rem; margin-bottom: 12px; }
    p { opacity: 0.9; margin-bottom: 24px; }
    ul { list-style: none; margin-bottom: 8px; }
    li {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        padding: 14px 18px;
        margin: 10px 0;
        font-size: 1.1rem;
        display: flex;
        justify-content: space-between;
    }
    li span { opacity: 0.8; }
    .clock { font-size: 3rem; font-weight: 700; margin: 16px 0; letter-spacing: 2px; }
</style>
"""

CLOCK_SCRIPT = """
<script>
    setInterval(function () {
        var now = new Date();
        document.getElementById("clock").textContent = now.toLocaleTimeString("uk-UA");
    }, 1000);
</script>
"""

# Вкладки меню: (назва маршруту з urls.py, текст вкладки)
NAV_ITEMS = [
    ("index", "🏠 Головна"),
    ("datetime", "🕒 Дата і час"),
    ("about", "🙋 Про мене"),
]

DAYS = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
MONTHS = ["січня", "лютого", "березня", "квітня", "травня", "червня",
          "липня", "серпня", "вересня", "жовтня", "листопада", "грудня"]


def build_nav(active):
    links = ""
    for name, label in NAV_ITEMS:
        css_class = "active" if name == active else ""
        links += f'<a class="{css_class}" href="{reverse(name)}">{label}</a>'
    return f"<nav>{links}</nav>"


def render_page(title, content, active, script=""):
    return HttpResponse(f"""
    <!doctype html>
    <html lang="uk">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{title}</title>
        {STYLE}
    </head>
    <body>
        {build_nav(active)}
        <main>
            <div class="card">
                {content}
            </div>
        </main>
        {script}
    </body>
    </html>
    """)


def index(request):
    return render_page(
        "Hello World",
        """
        <h1>👋 Hello World</h1>
        <p>Мій перший сайт на Django працює!</p>
        """,
        active="index",
    )


def current_datetime(request):
    now = datetime.datetime.now()
    day_name = DAYS[now.weekday()]
    month_name = MONTHS[now.month - 1]

    return render_page(
        "Дата і час",
        f"""
        <h1>🕒 Поточний час</h1>
        <div class="clock" id="clock">{now.strftime("%H:%M:%S")}</div>
        <ul>
            <li><span>День тижня</span> {day_name}</li>
            <li><span>Дата</span> {now.day} {month_name} {now.year}</li>
            <li><span>Номер тижня</span> {now.isocalendar()[1]}</li>
        </ul>
        """,
        active="datetime",
        script=CLOCK_SCRIPT,
    )


def about(request):
    return render_page(
        "Про мене",
        """
        <h1>🙋 Про мене</h1>
        <p>Я вчуся створювати сайти на Django.</p>
        <ul>
            <li><span>Мова</span> Python</li>
            <li><span>Фреймворк</span> Django</li>
            <li><span>Редактор</span> PyCharm</li>
        </ul>
        """,
        active="about",
    )