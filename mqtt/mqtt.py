# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
ENDPOINT = "ar5dtxqp6xalx-ats.iot.ap-northeast-2.amazonaws.com"
CLIENT_ID = "babo"
PATH_TO_CERT = "certificates/3536b3cc1d-certificate.pem.crt"
PATH_TO_KEY = "certificates/3536b3cc1d-private.pem.key"
PATH_TO_ROOT = "certificates/root.pem"
MESSAGE = ord("a")
TOPIC = "test/testing"
RANGE = 20 

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

myAWSIoTMQTTClient.connect()
print('Begin Publish')
for i in range (RANGE):
    data = "{} [{}]".format(chr(MESSAGE), i+1)
    message = {"message" : data}
    myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 0) 
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
    t.sleep(0.1)
    MESSAGE += 1
print('Publish End')
myAWSIoTMQTTClient.disconnect()