from app.handlers import upload, list_images, view, delete

def lambda_handler(event, context):
    route = event["resource"]
    method = event["httpMethod"]

    if route == "/images" and method == "POST":
        return upload.handler(event, context)
    if route == "/images" and method == "GET":
        return list_images.handler(event, context)
    if route == "/images/{image_id}" and method == "GET":
        return view.handler(event, context)
    if route == "/images/{image_id}" and method == "DELETE":
        return delete.handler(event, context)

    return {"statusCode": 404, "body": "Not Found"}
