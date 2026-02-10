import json

def success(data, status=200):
    return {
        "statusCode": status,
        "body": json.dumps(data)
    }

def error(message, status=400):
    return {
        "statusCode": status,
        "body": json.dumps({"error": message})
    }
