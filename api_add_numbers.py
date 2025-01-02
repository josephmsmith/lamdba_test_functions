import json

def lambda_handler(event, context):
    # Extract query string parameters
    value1 = event.get('queryStringParameters', {}).get('value1')
    value2 = event.get('queryStringParameters', {}).get('value2')
    
    message = "value1 and value2 are needed"

    # Check if both parameters are present
    if value1 and value2:
        try:
            # Parse the values as integers and calculate the sum
            sum_result = int(value1) + int(value2)
            message = f"The sum of {value1} and {value2} is {sum_result}"
        except ValueError:
            # Handle cases where values cannot be converted to integers
            message = "value1 and value2 must be valid integers"

    # Create the response object
    response = {
        'statusCode': 200,
        'body': json.dumps(message)
    }
    return response
