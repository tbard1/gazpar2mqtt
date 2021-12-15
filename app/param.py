#!/usr/bin/env python3

import argparse
import os
import logging
from envparse import env

def _isItTrue(val):
  
  if val.lower() == 'true':
    return True
  else:
    return False

  
# Class Params
class Params:
  
  # Constructor
  def __init__(self):
    
    # Step 1 : set default params
    
    # Grdf params
    self.grdfUsername = 'tom@bard1.fr'
    self.grdfPassword = '4661Gbvc'
    
    # Mqtt params
    self.mqttHost = '192.168.0.1'
    self.mqttPort = 8883
    self.mqttClientId = 'gazpar2mqtt'
    self.mqttUsername = None
    self.mqttPassword = None
    self.mqttQos = 1
    self.mqttTopic = 'gazpar'
    self.mqttRetain = False
    self.mqttSsl = False
    
    # Run params
    self.scheduleTime = None
    
    # Publication params
    self.standalone = True
    self.hassDiscovery = False
    self.hassPrefix = 'homeassistant'
    self.hassDeviceName = 'gazpar'
    
    # Databse params
    self.dbInit = False
    
    # Debug param
    self.debug = False
    
    # Step 2 : Init arguments for command line
    self.args = self.initArg()
    
    # Step 3 : Get params from env variables
    self.getFromOs()
    
    # Step 4 : Get args from command line and overwrite env if needed
    self.getFromArgs()
    
    
  # Set arguments list
  def initArg(self):
    
    self.parser = argparse.ArgumentParser()
    
    self.parser.add_argument(
        "--grdf_username",    help="GRDF user name, ex : myemail@email.com")
    self.parser.add_argument(
        "--grdf_password",    help="GRDF password")
    self.parser.add_argument(
        "-s", "--schedule",   help="Schedule the launch of the script at hh:mm everyday")
    self.parser.add_argument(
        "--mqtt_host",        help="Hostname or ip adress of the Mqtt broker")
    self.parser.add_argument(
        "--mqtt_port",        help="Port of the Mqtt broker")
    self.parser.add_argument(
        "--mqtt_clientId",    help="Client Id to connect to the Mqtt broker")
    self.parser.add_argument(
        "--mqtt_username",    help="Username to connect to the Mqtt broker")
    self.parser.add_argument(
        "--mqtt_password",    help="Password to connect to the Mqtt broker")
    self.parser.add_argument(
        "--mqtt_qos",         help="QOS of the messages to be published to the Mqtt broker")
    self.parser.add_argument(
        "--mqtt_topic",       help="Topic prefix of the messages to be published to the Mqtt broker")
    self.parser.add_argument(
        "--mqtt_retain",      help="Retain flag of the messages to be published to the Mqtt broker, possible values : True or False")
    self.parser.add_argument(
        "--mqtt_ssl",         help="Enable MQTT SSL connexion, possible values : True or False")
    self.parser.add_argument(
        "--standalone_mode",  help="Enable standalone publication mode, possible values : True or False")
    self.parser.add_argument(
        "--hass_discovery",   help="Enable Home Assistant discovery, possible values : True or False")
    self.parser.add_argument(
        "--hass_prefix",      help="Home Assistant discovery Mqtt topic prefix")
    self.parser.add_argument(
        "--hass_device_name", help="Home Assistant device name")
    self.parser.add_argument(
        "--db_init", help="Force database reinitialization : True or False")
    self.parser.add_argument(
        "--debug",            help="Enable debug mode")
    
    return self.parser.parse_args()
  
  
      
  # Load params from Os environment variables 
  def getFromOs(self):
    
    if "GRDF_USERNAME" in os.environ: self.grdfUsername = os.environ["GRDF_USERNAME"]
    if "GRDF_PASSWORD" in os.environ: self.grdfPassword = os.environ["GRDF_PASSWORD"]
      
    if "MQTT_HOST" in os.environ: self.mqttHost = os.environ["MQTT_HOST"]
    if "MQTT_PORT" in os.environ: self.mqttPort = int(os.environ["MQTT_PORT"])
    if "MQTT_CLIENTID" in os.environ: self.mqttClientId = os.environ["MQTT_CLIENTID"]
    if "MQTT_USERNAME" in os.environ: self.mqttUsername = os.environ["MQTT_USERNAME"]
    if "MQTT_PASSWORD" in os.environ: self.mqttPassword = os.environ["MQTT_PASSWORD"]
    if "MQTT_QOS" in os.environ: self.mqttQos = int(os.environ["MQTT_QOS"])
    if "MQTT_TOPIC" in os.environ: self.mqttTopic = os.environ["MQTT_TOPIC"]
    if "MQTT_RETAIN" in os.environ: self.mqttRetain = _isItTrue(os.environ["MQTT_RETAIN"])
    if "MQTT_SSL" in os.environ: self.mqttSsl = _isItTrue(os.environ["MQTT_SSL"])
      
    if "SCHEDULE_TIME" in os.environ: self.scheduleTime = os.environ["SCHEDULE_TIME"]
      
    if "STANDALONE_MODE" in os.environ: self.standalone = _isItTrue(os.environ["STANDALONE_MODE"])
    if "HASS_DISCOVERY" in os.environ: self.hassDiscovery = _isItTrue(os.environ["HASS_DISCOVERY"])
    if "HASS_PREFIX" in os.environ: self.hassPrefix = os.environ["HASS_PREFIX"]
    if "HASS_DEVICE_NAME" in os.environ: self.hassDeviceName = os.environ["HASS_DEVICE_NAME"]
      
    if "DB_INIT" in os.environ: self.dbInit = _isItTrue(os.environ["DB_INIT"])
    
    if "DEBUG" in os.environ: self.debug = _isItTrue(os.environ["DEBUG"])
  
  
  # Get params from arguments in command line
  def getFromArgs(self):
    
    if self.args.grdf_username is not None: self.grdfUsername = self.args.grdf_username
    if self.args.grdf_password is not None: self.grdfPassword = self.args.grdf_password
      
    if self.args.mqtt_host is not None: self.mqttHost = self.args.mqtt_host
    if self.args.mqtt_port is not None: self.mqttPort = int(self.args.mqtt_port)
    if self.args.mqtt_clientId is not None: self.mqttClientId = self.args.mqtt_clientId
    if self.args.mqtt_username is not None: self.mqttUsername = self.args.mqtt_username
    if self.args.mqtt_password is not None: self.mqttPassword = self.args.mqtt_password
    if self.args.mqtt_qos is not None: self.mqttQos = int(self.args.mqtt_qos)
    if self.args.mqtt_topic is not None: self.mqttTopic = self.args.mqtt_topic
    if self.args.mqtt_retain is not None: self.mqttRetain = _isItTrue(self.args.mqtt_retain)
    if self.args.mqtt_ssl is not None: self.mqttSsl = _isItTrue(self.args.mqtt_ssl)
      
    if self.args.schedule is not None: self.scheduleTime = self.args.schedule
      
    if self.args.standalone_mode is not None: self.standalone = _isItTrue(self.args.standalone_mode)
    if self.args.hass_discovery is not None: self.hassDiscovery = _isItTrue(self.args.hass_discovery)
    if self.args.hass_prefix is not None: self.hassPrefix = self.args.hass_prefix
    if self.args.hass_device_name is not None: self.hassDeviceName = self.args.hass_device_name
      
    if self.args.db_init is not None: self.dbInit = _isItTrue(self.args.db_init)
      
    if self.args.debug is not None: self.debug = _isItTrue(self.args.debug)
    
    
  # Check parameters
  def checkParams(self):
    
    if self.grdfUsername is None:
      logging.error("Parameter GRDF username is mandatory.")
      return False
    elif self.grdfPassword is None:
      logging.error("Parameter GRDF password is mandatory.")
      return False
    elif self.mqttHost is None:
      logging.error("Parameter MQTT host is mandatory.")
      return False
    else:
      if self.standalone == False and self.hassDiscovery == False:
        logging.warning("Both Standalone mode and Home assistant discovery are disable. No value will be published to MQTT ! Please check your parameters.")
        return True
      else:
        return True
  
  # Display parameters in log
  def logParams(self):
    
    logging.info("GRDF config : username = %s, password = %s", "******@****.**", "******")
    logging.info("MQTT broker config : host = %s, port = %s, clientId = %s, qos = %s, topic = %s, retain = %s, ssl = %s", \
                 self.mqttHost, self.mqttPort, self.mqttClientId, \
                 self.mqttQos,self.mqttTopic,self.mqttRetain, \
                 self.mqttSsl),
    logging.info("Standlone mode : Enable = %s", self.standalone)
    logging.info("Home Assistant discovery : Enable = %s, Topic prefix = %s, Device name = %s", \
                 self.hassDiscovery, self.hassPrefix, self.hassDeviceName)
    logging.info("Database options : Force reinitialization = %s", self.dbInit)
    logging.info("Debug mode : Enable = %s", self.debug)
