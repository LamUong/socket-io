from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask import render_template

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def hello_world():
   return render_template('main.html')


@socketio.on('connect')
def test_connect():
   # send to current user only
   emit('new connection', 'you are connected')
   # send to all users not including current user
   emit('new connection', 'new user connected', broadcast=True, include_self=False)

@socketio.on('chat message')
def handle_message(msg): # message could be json or other stuffs
   # just emitting the message to everyone except the sender
   emit('chat message', msg, broadcast=True, include_self=False)
   print('new message')

if __name__ == '__main__':
   socketio.run(app)
