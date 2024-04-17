import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def wait_for_user_input():
    """
    Waits for user input and returns the input value.

    Returns:
        int: The user input value.
    """
    try:
        # TO DO

    
            

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("broker.example.com", 1883, 60)

    while True:
        client.loop()

        # Wait for user input
        user_input = wait_for_user_input()
        
        # If user input is valid, publish it to the MQTT topic
        if user_input is not None:
            client.publish("test/topic", user_input)
            print("Published: " + user_input)
            break  # Exit the loop after publishing the input value once

if __name__ == "__main__":
    main()
