import json

def lambda_handler(event, context):
    """
    Lambda function to get a list of products.
    
    Returns:
        A list of mock products with their details.
    """
    # Mock product data
    products = [
        {
            "productId": "p001",
            "name": "Smartphone X",
            "price": 799.99,
            "category": "Electronics",
            "description": "Latest smartphone with advanced features"
        },
        {
            "productId": "p002",
            "name": "Laptop Pro",
            "price": 1299.99,
            "category": "Electronics",
            "description": "High-performance laptop for professionals"
        },
        {
            "productId": "p003",
            "name": "Wireless Headphones",
            "price": 199.99,
            "category": "Audio",
            "description": "Noise-cancelling wireless headphones"
        },
        {
            "productId": "p004",
            "name": "Smart Watch",
            "price": 249.99,
            "category": "Wearables",
            "description": "Fitness and health tracking smartwatch"
        },
        {
            "productId": "p005",
            "name": "Bluetooth Speaker",
            "price": 89.99,
            "category": "Audio",
            "description": "Portable waterproof bluetooth speaker"
        }
    ]
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"products": products})
    }
