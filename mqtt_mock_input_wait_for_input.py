import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected with result code "+str(reason_code))
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def wait_for_user_input():
    """
    Waits for user input and returns the input value.

    Returns:
        int: The user input value.
    """
# TO DO - Create a function to prompt the user for an int with error handling 

       

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)



# Wait for user input
user_input = wait_for_user_input()

# If user input is valid, publish it to the MQTT topic
if user_input is not None:
    mqttc.publish("test/topic", user_input)
    print("Published: " + user_input)
  

mqttc.loop()
