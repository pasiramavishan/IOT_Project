from paho.mqtt import client as mqtt_client
import paho.mqtt.client as mqtt
import time

# Callback when the client connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe(topic)  # Subscribe to the receive topic
    else:
        print("Connection failed with code {rc}")


# Callback when a message is received from the subscribed topic
def on_message(client, userdata, msg):
    # print ("Message received " + "on "+ topic + ": "  + str(msg.payload.decode("utf-8")))
    print (str(msg.payload.decode("utf-8")))
# Create an MQTT client instance
client = mqtt.Client()




# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message



# Connect to the MQTT broker
broker_address = "broker.mqtt.cool"  # broker's address
broker_port = 1883
keepalive = 60
qos = 0

topic = input("where you want to put message: ")
name = input("you name: ")
# topic = input ('Enter the topic to subscribe to: ')
client.connect(broker_address, broker_port, keepalive)



client.loop_start()


try:
    while True:
        # Publish a message to the send topic
        
        value = input()
        value = name + '->' + value
        client.publish(topic,value)
        # print(f"Published message '{value}' to topic '{topic}'\n")
        
        # Wait for a moment to simulate some client activity
        time.sleep(6)
except KeyboardInterrupt:
    # Disconnect from the MQTT broker
    pass
client.loop_stop()
client.disconnect()

print("Disconnected from the MQTT broker")

