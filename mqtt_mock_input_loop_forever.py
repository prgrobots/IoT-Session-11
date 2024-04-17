import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected with result code "+str(reason_code))
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def publish_incrementing_value():
   """
    Publishes an int that increases by 1 every second
    
    Returns:
        int: The published value
    """

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)

mqttc.loop_forever()