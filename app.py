import random
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from conversation_data import conversation_dict



# Initialize Flask app, database, and other components
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' #please add secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.db'  # SQLite Database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    chats = db.relationship('Chat', backref='author', lazy=True)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_message = db.Column(db.String(500), nullable=False)
    ai_message = db.Column(db.String(500), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('chat'))
        else:
            flash('Login unsuccessful. Check email and password', 'danger')
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


def get_ai_response(user_message):
    user_message_lower = user_message.lower()

    # Search in each category of the conversation dictionary
    for category, messages in conversation_dict.items():
        for user_phrase in messages["user"]:
            if user_message_lower == user_phrase.lower():
                # If a match is found, return a random AI response from the category
                return random.choice(messages["ai"])
    
    # If no match found, return a default response
    return "I'm sorry, I don't have an answer for that right now."

@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    if request.method == 'POST':
        user_message = request.form['message']
        
        # Get the AI response from the conversation dictionary
        ai_message = get_ai_response(user_message)

        # Save chat to the database (Chat and db are assumed to be pre-defined)
        chat = Chat(user_id=current_user.id, user_message=user_message, ai_message=ai_message)
        db.session.add(chat)
        db.session.commit()

        # Return the response as JSON
        return jsonify({'user_message': user_message, 'ai_message': ai_message})

    # Load chat history for the current user
    chat_history = Chat.query.filter_by(user_id=current_user.id).all()
    return render_template('chat.html', chat_history=chat_history)


with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True)
