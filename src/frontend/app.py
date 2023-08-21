from flask import Flask, render_template, request, redirect, flash, url_for


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



if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)