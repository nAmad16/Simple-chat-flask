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

# SUNUCU URL'İNİ BURAYA YAZ (Render'dan alacaksın)
SERVER_URL = "https://senin-chat.onrender.com"

# Sunucuya bağlan
sio.connect(SERVER_URL)

# Mesaj gönderme döngüsü
while True:
    msg = input("Mesaj: ")
    sio.send(msg)
