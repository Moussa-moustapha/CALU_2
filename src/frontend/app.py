from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from uuid import uuid4
from models import storage
from models.user import User
from hashlib import md5
from flask_login import login_user, login_required, logout_user, current_user


app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/clubs')
def clubs():
    return render_template('clubs.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home1')
def home1():
    return render_template('home-1.html')

@app.route('/clubs1')
def clubs1():
    return render_template('clubs-1.html')




@app.route('/clubs1/<string:club_name>')
def club(club_name):
    return render_template('club.html', club_name=club_name)




 
@app.route('/about1')
def about1():
    return render_template('about-1.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')



@app.route('/signup')
def signup():
    return render_template('signup.html')



@app.route('/sign-in', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if request.method == "POST":
        data = request.form
        username = data.get('username')
        password = md5(data.get('password').encode()).hexdigest()
        users = storage.all(User).values()
        user = None
        for u in users:
            if u.username == username:
                user = u
                break
        if user:
            if password == user.password:
                flash("Logged in successfully", category='success')
                login_user(user, remember=True)
                return redirect(url_for('home1'))
            else:
                flash("Incorrect Password", category='error')
        else:
            flash("Incorrect username", category='error')
    return render_template("signup.html", cache_id=cache_id, user=current_user)


@app.route('/logout', strict_slashes=False)
@login_required
def logut():
    logout_user()
    return redirect(url_for('home'))


@app.route('/sign-up', methods=['GET', 'POST'], strict_slashes=False)
def register():
    if request.method == 'POST':
        users = storage.all(User).values()
        usernames = [user.username for user in users]
        emails = [user.email for user in users]
        phone_numbers = [user.phone for user in users]
        data = request.form
        email = data.get('email')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        password1 = data.get('password1')
        password2 = data.get('password2')
        phone_number = data.get('phoneNumber')
        username = data.get('username')

        if username in usernames:
            flash("Username already exists", category="error")
        elif email in emails:
            flash("Email address already exists", category='error')
        elif len(password1) < 6 or len(password1) > 15:
            flash("Password must be 6 - 15 characters length",
                  category='error')
        elif password1 != password2:
            flash("Passwords don't match", category='error')
        elif len(phone_number) != 10:
            flash("Please insert a valid phone number", category='error')
        elif phone_number in phone_numbers:
            flash("Phone number already exists", category='error')
        else:
            info = {"first_name": first_name, "last_name": last_name,
                    "email": email, "phone": phone_number, "password": password1,
                    "username": username}
            new_account = User(**info)
            new_account.save()
            login_user(new_account, remember=True)
            flash("Account created successfully", category='success')
            return redirect(url_for('home1'))

    return render_template("signup.html", cache_id=cache_id, user=current_user)



if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)