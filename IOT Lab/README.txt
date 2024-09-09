# MQTT Chat Application

This is a simple chat application built using Python and the `paho-mqtt` library for MQTT messaging, along with `tkinter` for the graphical user interface (GUI). The app allows users to connect to an MQTT broker, subscribe to a topic, and send/receive messages with other clients connected to the same topic.

## Features

- Connects to an MQTT broker.
- Subscribes to a user-specified topic.
- Sends and receives messages in real-time.
- Displays messages in a user-friendly format with the sender's name and the message body.
- Simple GUI built with `tkinter`.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- `paho-mqtt` library

You can install the `paho-mqtt` library using pip:

```bash
pip install paho-mqtt

## Code Overview

### MQTT Callbacks

- **on_connect:** This callback is triggered when the client successfully connects to the MQTT broker. It subscribes to the topic specified by the user.

- **on_message:** This callback is triggered when a message is received from the subscribed topic. It processes and displays the message in the text area.

### Main Application

- The application GUI is built using `tkinter`. It includes fields for entering your name, the topic, and the message, along with buttons to connect and send messages.

### MQTT Configuration

- **Broker Address:** The MQTT broker used in this app is `broker.mqtt.cool`.
- **Port:** The application connects to port `1883`.
- **Keepalive:** The keepalive interval is set to `60` seconds.

### Cleanup

- The app includes a cleanup function (`on_closing`) that stops the MQTT loop and disconnects the client when the window is closed.
