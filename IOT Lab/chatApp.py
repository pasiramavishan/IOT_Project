import paho.mqtt.client as mqtt
import tkinter as tk
import time

# Callback when the client connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        topic = entry2.get()
        if topic:
            client.subscribe(topic)
        client.subscribe(topic)  # Subscribe to the receive topic
        text_area.insert(tk.END, "Connected to MQTT broker and subscribed to topic: " + topic + "\n")
    else:
        text_area.insert(tk.END, "Failed to connect, return code %d\n" % rc)

# Callback when a message is received from the subscribed topic
def on_message(client, userdata, msg):
    message = str(msg.payload.decode("utf-8"))
    
    # Split the message into name and body
    if '->' in message:
        name, body = message.split('->', 1)
        text_area.insert(tk.END, f"{name.strip()} \t>>\t{body.strip()}\n")
    else:
        # Handle cases where the message format is incorrect
        text_area.insert(tk.END, f"Received malformed message: {message}\n")

# Create an MQTT client instance
client = mqtt.Client()

def on_send():
    topic = entry2.get()
    value = entry3.get()
    name = entry1.get()
    message = f"{name} -> {value}"
    client.publish(topic, message)
    # text_area.insert(tk.END, message)
    
def connect_mqtt():
    global broker_address, broker_port, keepalive
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(broker_address, broker_port, keepalive)
    client.loop_start()

app = tk.Tk()
app.title("Chat App")
app.geometry("600x400")

bar_frame = tk.Frame(app)
bar_frame.pack(pady=20)
bottom_frame = tk.Frame(app)
bottom_frame.pack(pady=10, fill=tk.X, side=tk.BOTTOM)

# Place labels, entries and button in the top frame
label1 = tk.Label(bar_frame, text="Name:")
label1.grid(row=0, column=0, padx=5)
entry1 = tk.Entry(bar_frame)
entry1.grid(row=0, column=1, padx=5)

label2 = tk.Label(bar_frame, text="Topic:")
label2.grid(row=0, column=2, padx=5)
entry2 = tk.Entry(bar_frame)
entry2.grid(row=0, column=3, padx=5)

button = tk.Button(bar_frame, text="Connect", command=connect_mqtt)
button.grid(row=0, column=4, padx=5)

# Place an entry and button in the bottom frame
entry3 = tk.Entry(bottom_frame)
entry3.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

button_send = tk.Button(bottom_frame, text="Send", command=on_send)
button_send.pack(side=tk.LEFT, padx=5, pady=5)

# Text area
text_area = tk.Text(app, height=10, font=("Arial", 10))
text_area.pack(pady=20, fill=tk.BOTH, expand=True)

# MQTT broker details
broker_address = "broker.mqtt.cool"
broker_port = 1883
keepalive = 60

def on_closing():
    global client
    if client:
        client.loop_stop()
        client.disconnect()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()
