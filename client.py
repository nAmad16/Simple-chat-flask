import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("✅ Sunucuya bağlandı.")

@sio.event
def disconnect():
    print("❌ Sunucudan ayrıldı.")

@sio.on('message')
def on_message(data):
    print(f"📨 Gelen mesaj: {data}")

SERVER_URL = "https://urchat.onrender.com"

sio.connect(SERVER_URL)

while True:
    msg = input("Mesaj: ")
    sio.send(msg)
