#!/usr/bin/python
import json
import time

def write_omsconfig_host_telemetry(message):
    event_params = {}
    event_params['Name'] = 'Microsoft.EnterpriseCloud.Monitoring.OmsConfigHost'
    event_params['Version'] = '1.0'
    event_params['IsInternal'] = False
    event_params['Operation'] = 'omsconfig_host_wrapper'
    event_params['OperationSuccess'] = True
    event_params['Message'] = message
    event_params['Duration'] = 0
    event_params['ExtentionType'] = ''
    
    event = {}
    event['providerId'] = '69B669B9-4AF8-4C50-BDC4-6006FA76E975'
    event['parameters'] = event_params
    event['eventId'] = 1

    event_filename = "/var/lib/waagent/events/%d.tld" % (time.time()*1000000000)

    with open(event_filename, 'w+') as event_file:
        json.dump(event, event_file)

def write_omsconfig_host_event(pathToCurrentScript, dsc_host_switch_exists):
    msg_template = '<OMSCONFIGLOG>[{}] [{}] [{}] [{}] [{}:{}] {}</OMSCONFIGLOG>'
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y/%m/%d %H:%M:%S')
    if dsc_host_switch_exists:
        msg_buffer = 'Using dsc_host'
    else:
        msg_buffer = 'Falling back to OMI'
    message = msg_template.format(timestamp, os.getpid(), 'INFO', 0, pathToCurrentScript, 0, msg_buffer)
    write_omsconfig_host_telemetry(message)
