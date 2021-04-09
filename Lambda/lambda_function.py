import json
import boto3

#Client to access Comprehend Medical
medComprehendClient = boto3.client(service_name='comprehendmedical', region_name='us-east-1')

def lambda_handler(event, context):
    print(event['Input'])
    inputText = event['Input']
    print(inputText)
    
    #API Call for Medical Entities Detection/NER
    entitiesDetected = medComprehendClient.detect_entities(Text = inputText)
    print(entitiesDetected)
    
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': entitiesDetected
    }
