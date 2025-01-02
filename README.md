# Lambda Test Functions

This repository contains several AWS Lambda function examples for different use cases, such as interacting with S3, DynamoDB, and handling API Gateway requests. These scripts are designed to demonstrate how to implement common operations with AWS services in Python.

## Prerequisites
- AWS account with necessary IAM permissions
- AWS services like S3 and DynamoDB configured for specific scripts
- Python 3.x
- `boto3` library installed (`pip install boto3`)

## Files and Descriptions

### 1. [`api_add_numbers.py`](https://github.com/josephmsmith/lamdba_test_functions/blob/main/api_add_numbers.py)
This script implements an AWS Lambda function that adds two numbers passed as query string parameters (`value1` and `value2`).
- **Description**: Calculates the sum of two integers provided via API Gateway query parameters.
- **Input Example**:
  ```json
  {
      "queryStringParameters": {
          "value1": "5",
          "value2": "10"
      }
  }
  ```
- **Output**: Returns the sum or an error message if the inputs are invalid.

---

### 2. [`dynamo_db_add_item.py`](https://github.com/josephmsmith/lamdba_test_functions/blob/main/dynamo_db_add_item.py)
This script implements a Lambda function to add an item to a DynamoDB table named `planets`.
- **Description**: Adds a static item (`id: neptune`, `temp: super cold`) to the `planets` table.
- **Output**: Confirms the item was added successfully.

---

### 3. [`dynamo_db_read_tables.py`](https://github.com/josephmsmith/lamdba_test_functions/blob/main/dynamo_db_read_tables.py)
This script implements a Lambda function to read an item from the `planets` DynamoDB table.
- **Description**: Retrieves the item with the key `id: mercury` from the `planets` table and returns the result.
- **Output**: Returns the item's details in JSON format or an empty response if the item is not found.

---

### 4. [`list_s3_buckets.py`](https://github.com/josephmsmith/lamdba_test_functions/blob/main/list_s3_buckets.py)
This script implements a Lambda function to list all S3 buckets in the AWS account.
- **Description**: Fetches and returns a list of all S3 bucket names accessible to the Lambda function.
- **Output**: A JSON array of bucket names.

---

## How to Use

### 1. Deployment
1. Package each script as a separate Lambda function.
2. Deploy to AWS Lambda via the AWS Console, AWS CLI, or infrastructure-as-code tools like Terraform or AWS SAM.
3. Assign the necessary IAM roles for each script:
   - **`api_add_numbers.py`**: No additional permissions required.
   - **`dynamo_db_add_item.py` and `dynamo_db_read_tables.py`**: Requires DynamoDB `PutItem` and `GetItem` permissions for the `planets` table.
   - **`list_s3_buckets.py`**: Requires `s3:ListAllMyBuckets` permission.

### 2. Testing
- Use the AWS Lambda Console or API Gateway to test the functions.
- For DynamoDB functions, ensure the `planets` table exists and has an `id` key defined.

### 3. Logs and Debugging
- Use AWS CloudWatch to view logs and debug errors for each Lambda execution.

## License
This project is open-source and available under the [MIT License](LICENSE).
