def lambda_handler(event, context):
    print("Hi from Lambda!")
    return {
        'statusCode': 200,
        'body': "successful"
    }
