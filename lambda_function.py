import json
import requests

def lambda_handler(event, context):
    numbers_in_words = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    if event.get('queryStringParameters'):
        number = int(event['queryStringParameters']['number'])
    elif event.get('body'):
        body = json.loads(event['body'])
        number = int(body.get('number'))
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': 'Input must be provided as either query parameters or a JSON object in the request body'
            })
        }

    if number >= 1 and number <= 9:
        return {
            'statusCode': 200,
            'body': json.dumps({
                'number': numbers_in_words[number]
            })
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': 'Input must be a number between 1 and 9'
            })
        }
