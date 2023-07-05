from flask import Flask, render_template, url_for, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email, ValidationError
from werkzeug.security import check_password_hash
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'anak-sholih'

class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password1 = PasswordField('password1', validators=[validators.DataRequired(), validators.Length(min=3), validators.EqualTo('password2', message='Passwords do not match')])
    password2 = PasswordField('password2', validators=[validators.DataRequired(), validators.EqualTo('password1', message='Passwords do not match')])
    submit = SubmitField('register')

    # def validate_email(self, field):
    #     if check_email_exists(field.data):
    #         raise ValidationError('This email has already been registered!')

@app.route("/")
def Home():
    title = 'Halaman Home'
    return render_template('sbadmin2/index.html', title=title)

        
@app.route("/login")
def Login():
    css_url = url_for('static', filename='css/sb-admin-2.min.css');
    return render_template('sbadmin2/login.html', css_url=css_url)

@app.route("/register", methods=['GET', 'POST'])
def Register():
    title = 'Halaman Registrasi'
    form = RegistrationForm()
    if form.validate_on_submit() == False:
        return render_template('sbadmin2/register.html', title=title, form=form)
    else:
        return "<p>Berhasil !</p>"

if __name__ == "__main__":
    app.run(debug=True)
