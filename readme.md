# MQTT Mock Input with Paho and Adafruit IO

This repository contains Python scripts demonstrating how to create mock input for MQTT (Message Queuing Telemetry Transport) using the Paho MQTT client library and publish to Adafruit IO. Two versions of mock input are provided:

1. **Loop Forever**: Sends an incrementing variable to an MQTT topic every second.
2. **Wait for User Input**: Waits for the user to input an integer and publishes it to an MQTT topic.

## Requirements

- Python 3.x
- Paho MQTT library (`paho-mqtt`)

## Installation

You can install the required dependencies using pip:

```bash
pip install paho-mqtt
```

# 1. Instructions

1. **Loop Forever**:
    - Run the script `mqtt_mock_input_loop_forever.py`.
    - This script will continuously send an incrementing variable to the MQTT topic specified in `FEED_NAME` every second.

2. **Wait for User Input**:
    - Open the script `mqtt_mock_input_wait_for_input.py` in a text editor.
    - Locate the section marked `# TO DO` in the script.
    - Modify the script to include error handling using try-except blocks for user input.
    - Save the changes to the script.
    - Run the modified script.
    - This script will wait for the user to input an integer. Once an integer is entered, it will be published to the MQTT topic specified in `FEED_NAME`.

Ensure that you have a properly configured MQTT broker to receive messages from the scripts.  You can use https://testclient-cloud.mqtt.cool/ to view your messages



# 2. Connecting to Adafruit IO

### To connect the MQTT client to Adafruit IO, follow these steps:

Create an Adafruit IO Account:

- Visit the Adafruit IO website.
- Sign up for a free account.
### Get Your Adafruit IO API Key:

Once logged in, navigate to your Adafruit IO account settings.
Find your Adafruit IO API key. This will be used to authenticate your client with Adafruit IO's MQTT broker.
### Create a Feed:

In Adafruit IO, create a new feed.
Note the name of the feed. This will be the MQTT topic to which your client will publish messages.
### Modify the Script:

In the Python script **(mqtt_mock_input_wait_for_input.py or mqtt_mock_input_loop_forever.py)**, set the following variables:**
**ADAFRUIT_IO_USERNAME:** Your Adafruit IO username.
**ADAFRUIT_IO_KEY:** Your Adafruit IO API key.
***FEED_NAME:** The name of the feed you created on Adafruit IO.
This will authenticate your client with Adafruit IO's MQTT broker and allow it to publish messages to the specified feed.

### Error Handling
Both versions of the script include error handling using try-except blocks. This ensures graceful handling of exceptions such as KeyboardInterrupt, allowing the script to exit cleanly when needed.

### Instructions
Loop Forever:

Run the script **mqtt_mock_input_loop_forever.py.**
This script will continuously send an incrementing variable to the MQTT topic specified in FEED_NAME every second.
Wait for User Input:

Run the script **mqtt_mock_input_wait_for_input.py.**
This script will wait for the user to input an integer. Once an integer is entered, it will be published to the MQTT topic specified in FEED_NAME.
Ensure that you have a properly configured MQTT broker to receive messages from the scripts