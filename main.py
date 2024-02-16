# Import
from flask import Flask, render_template,request, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<User {self.id}>'
    
# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    
    email = request.form.get('email')
    text = request.form.get('text')
    
    
    if email is not None:
        with open('kullanici_verisi.txt', 'a') as f:
            f.write(f'{email}\n')
            f.write(f'{text}\n')
            f.write('--------------\n')
            
        Abuser = User(email=email, comment=text)
        db.session.add(Abuser)
        db.session.commit()
        

    return render_template('index.html',
                           button_python=button_python,
                           button_discord=button_discord,
                           button_html=button_html,
                           button_db=button_db)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
