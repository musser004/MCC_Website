# Professional Portfolio Website

from flask import Flask, render_template, flash, url_for, redirect
from flask_bootstrap import Bootstrap
from forms import ContactForm
from email_sender import EmailSender
import os
import gunicorn

# Initial Flask setup

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
Bootstrap(app)
email_sender = EmailSender()

# Index page setup


@app.route("/", methods=["GET", "POST"])
def index():
    form = ContactForm()

    # Contact form setup

    if form.validate_on_submit():
        flash("Message successfully sent!")
        email_sender.send_email(name=form.name.data,
                                phone=form.phone.data,
                                contact_email=form.email.data,
                                message=form.message.data
                                )
        form.name.data = ""
        form.email.data = ""
        form.phone.data = ""
        form.message.data = ""
    else:
        return render_template("index.html", form=form, section="contact")
    return render_template("index.html", form=form)

# Portfolio project - Blog page setup


@app.route("/full_blog.html")
def full_blog():
    return render_template("full_blog.html")

# Portfolio project - custom image watermarker page setup


@app.route("/watermarker.html")
def watermarker():
    return render_template("watermarker.html")

# Portfolio project - Alucard website page setup


@app.route("/alucard_website.html")
def alucard_website():
    return render_template("alucard_website.html")

# Portfolio project - JamesBot page setup


@app.route("/jamesbot.html")
def jamesbot():
    return render_template("jamesbot.html")

# Portfolio project - Flight deal finder page setup


@app.route("/flight_deal_finder.html")
def flight_deal_finder():
    return render_template("flight_deal_finder.html")

# Portfolio project - Selenium cookie clicker bot page setup


@app.route("/cookie_clicker_bot.html")
def cookie_clicker_bot():
    return render_template("cookie_clicker_bot.html")

# Portfolio project - Dr. Semmelweis data page setup


@app.route("/dr_semmelweis.html")
def dr_semmelweis():
    return render_template("dr_semmelweis.html")

# Portfolio project - Nobel prize data page setup


@app.route("/nobel_prize.html")
def nobel_prize():
    return render_template("nobel_prize.html")

# Portfolio project - Movie budget data page setup


@app.route("/movie_budget.html")
def movie_budget():
    return render_template("movie_budget.html")

# Portfolio project - Flash card app page setup


@app.route("/flash_card.html")
def flash_card():
    return render_template("flash_card.html")

# Portfolio project - Snake game page setup


@app.route("/snake_game.html")
def snake_game():
    return render_template("snake_game.html")

# Portfolio project - Sudoku checker page setup


@app.route("/sudoku_checker.html")
def sudoku_checker():
    return render_template("sudoku_checker.html")

# Portfolio project - Password generator page setup


@app.route("/password_generator.html")
def password_generator():
    return render_template("password_generator.html")


# Flask run


if __name__ == "__main__":
    app.run(debug=True)
