"""
Cafe Review Flask Application
------------------------------

This project is a Flask-based web application that allows users to manage a list of cafes.
Users can add new cafes by providing details such as the name, location, timings, and ratings for coffee, WiFi, and power outlets.
They can also view the existing list of cafes in a tabular format.

Features:
---------
1. Add a new cafe:
   - Cafe name
   - Location URL
   - Opening and closing time
   - Coffee rating (☕️)
   - WiFi rating (💪)
   - Power outlet rating (🔌)

2. View the list of cafes:
   - Data is stored in a CSV file (`cafe-data.csv`).
   - The table displays all stored cafes with their details.

Routes:
-------
1. `/`:
   - Renders the home page.

2. `/add`:
   - Renders a form to add a new cafe.
   - Saves valid form data to the `cafe-data.csv` file.
   - Redirects to the `/cafes` page upon successful submission.

3. `/cafes`:
   - Reads from the `cafe-data.csv` file and displays the cafes in a table.

Dependencies:
-------------
- Flask
- Flask-WTF
- Flask-Bootstrap
- WTForms
- CSV

Instructions:
-------------
1. Run the application with `python app.py`.
2. Visit `http://127.0.0.1:5000` to view the home page.
3. Use the "Add Cafe" form to add new cafes.
4. Navigate to `/cafes` to view the list of cafes.

"""

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap4(app)

coffee = [("1","☕️"),("2","☕️☕️"),("3","☕️☕️☕️"),("4","☕️☕️☕️☕️"),("5","☕️☕️☕️☕️☕️")]
wifi = [("1","✘"),("2","💪"),("3","💪💪"),("4","💪💪💪"),("5","💪💪💪💪"),("6","💪💪💪💪💪")]
power_outlet = [("1","✘"),("2","🔌"),("3","🔌🔌"),("4","🔌🔌🔌"),("5","🔌🔌🔌🔌"),("6","🔌🔌🔌🔌🔌")]


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])

    location_url = StringField(label='Website',validators=[DataRequired(),URL()])
    open_time =StringField(label="Opening_Time",validators=[DataRequired()])
    closing_time = StringField(label='closing_time',validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating',choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],validators=[DataRequired()])
    wifi_rating = SelectField(label="Wifi Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],validators=[DataRequired()])
    power_outlet_rating = SelectField(label="Power Socket Rating",choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    cafe_info = ""
    if form.validate_on_submit():
        print("True")
        cafe_info =f"\n{form.cafe.data},{form.location_url.data},{form.open_time.data},{form.closing_time.data},{form.coffee_rating.data},{form.wifi_rating.data},{form.power_outlet_rating.data}"

        with open('cafe-data.csv',"a", encoding='utf-8') as csv_file:
            csv_file.write(cafe_info)
        return redirect(url_for('cafes'))
        print("Cafe successfully added to the list")


    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
