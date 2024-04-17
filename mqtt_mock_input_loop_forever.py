import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def publish_incrementing_value(client):
    value = 0
    while True:
        value += 1
        client.publish("test/topic", str(value))
        print("Published: " + str(value))
        time.sleep(1)

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("broker.example.com", 1883, 60)

    publish_incrementing_value(client)

if __name__ == "__main__":
    main()
