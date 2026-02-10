# 📸 Image Upload & Storage Service (Instagram-like Backend)

## 📌 Overview

This project implements the backend service layer of an **Instagram-like image management system**.  
It provides APIs to upload, list, view, and delete images using **AWS serverless services**.

The goal of this project is to demonstrate:
- Clean backend architecture
- Proper use of AWS services
- Strong unit testing using mocked cloud services (Moto)
- Interview-ready, production-style code

---

## 🏗️ Architecture

The application is designed using a **serverless architecture**:

| Component | Responsibility |
|---------|----------------|
| **API Gateway** | Exposes REST APIs |
| **AWS Lambda** | Handles business logic |
| **Amazon S3** | Stores image files |
| **Amazon DynamoDB** | Stores image metadata |
| **IAM** | Manages secure access |

### Flow

1. Client uploads an image via API
2. Lambda uploads image to S3
3. Metadata is saved in DynamoDB
4. Client can list, view, or delete images

This architecture ensures:
- High scalability
- Low operational cost
- Stateless and fault-tolerant design

---

## 📂 Project Structure
```
monty-coding-test/
│
├── app/
│ ├── __init__.py
│ ├── handlers/
│ │ ├── __init__.py
│ │ ├── upload.py
│ │ ├── list_images.py
│ │ ├── view.py
│ │ └── delete.py
│ │
│ ├── services/
│ │ ├── __init__.py
│ │ ├── s3_service.py
│ │ └── dynamo_service.py
│ │
| ├── utils/
│ │ ├── __init__.py
│ │ ├── response.py
│ │ └── validators.py
│ ├── aws_clients.py
│ ├── main.py
│ ├── models.py
│ └── config.py
│
├── tests/
│ ├── conftest.py
│ ├── test_upload.py
│ ├── test_list.py
│ ├── test_view.py
│ └── test_delete.py
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Configuration

The application uses environment variables for configuration.

### `.env.example`

```env
AWS_REGION=ap-south-1
S3_BUCKET_NAME=instagram-images-demo
DYNAMODB_TABLE_NAME=ImageMetadata
```

### `config.py`
```
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
S3_BUCKET = os.getenv("S3_BUCKET_NAME", "instagram-images-demo")
DYNAMO_TABLE = os.getenv("DYNAMODB_TABLE_NAME", "ImageMetadata")
```

## 🌍 Environment Compatibility

The application is designed to use environment variables for all AWS configurations.  
This allows the **same codebase** to run seamlessly in:

- Local development environment
- CI/CD pipelines
- AWS Lambda production environment

No code changes are required when switching environments—only environment variables need to be updated.

---

## 🔌 API Endpoints

### 📤 Upload Image
**POST** `/upload`

- Uploads an image file to Amazon S3
- Stores image metadata in Amazon DynamoDB

---

### 📄 List Images
**GET** `/images`

- Returns a list of uploaded images
- Supports filtering (e.g., by user, upload date, etc.)

---

### 👁️ View Image
**GET** `/images/{image_id}`

- Returns a pre-signed Amazon S3 URL
- Allows secure, temporary access to view or download the image

---

### 🗑️ Delete Image
**DELETE** `/images/{image_id}`

- Deletes the image file from Amazon S3
- Removes associated metadata from Amazon DynamoDB


## 🧪 Testing Approach

This project uses the **Moto** library to mock AWS services (S3 and DynamoDB) during testing.  
Moto allows testing AWS-dependent logic **locally without real AWS credentials**, costs, or infrastructure, while still enforcing real AWS behavior and constraints.

---

## ▶️ Running Tests

### Install Dependencies

```bash
pip install -r requirements.txt
```

Run Test
```bash
pytest -v
```

All AWS interactions in the tests are handled using mocked services via Moto, ensuring fast, reliable, and production-accurate test execution.
