import paho.mqtt.client as mqtt
import mqttutil
import time

# Broker settings
broker_client = "gazou"

# Initialize variables
mqtt_connected = False

# on_connect
def on_connect(client, userdata, flags, rc):
    global mqtt_connected
    print("on_connect: " + mqtt.connack_string(rc))
    mqtt_connected = True

# ----------------------------
# Main
# ----------------------------

# Create instance
print("Create mqtt instance")
client = mqtt.Client(broker_client)

# Activate callbacks
client.on_connect = on_connect
client.on_message = mqttutil.on_message
client.on_publish = mqttutil.on_publish
client.on_disconnect = mqttutil.on_disconnect

# Connect
print("Connexion to broker")
client.connect(mqttutil.mqtt_host["hostname"], mqttutil.mqtt_host["port"], 60)
time.sleep(2)
client.loop_start()

# Publish
if mqtt_connected :
    print("Publication to broker")
    client.publish(mqttutil.topic_name, "Hello world")
    time.sleep(3)

" Stop
time.sleep(2)
client.loop_stop()
