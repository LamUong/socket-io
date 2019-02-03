from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask import render_template

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def hello_world():
   return render_template('camera.html')


@socketio.on('connect')
def test_connect():
   # send to current user only
   emit('new connection', 'you are connected')
   # send to all users not including current user
   emit('new connection', 'new user connected', broadcast=False, include_self=True)

@socketio.on('image_data')
def handle_image(img): # message could be json or other stuffs
   # just emitting the message to everyone except the sender
   print("data")
   emit('image_data', img, broadcast=False, include_self=True)

if __name__ == '__main__':
   socketio.run(app)
