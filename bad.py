from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"  # Noncompliant
app.config['SESSION_COOKIE_SECURE'] = True  # Noncompliant
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Noncompliant
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Noncompliant
app.config['SESSION_COOKIE_DOMAIN'] = 'example.com'  # Noncompliant

app.run()