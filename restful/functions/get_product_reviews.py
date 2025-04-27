import json

def lambda_handler(event, context):
    """
    Lambda function to get reviews for a specific product.
    
    Parameters:
        event: Contains API Gateway event information including path parameters
        
    Returns:
        Reviews for the specified product ID.
    """
    # Extract product ID from path parameters
    product_id = event.get('pathParameters', {}).get('productId', '')
    
    # Mock reviews data based on product ID
    reviews_by_product = {
        "p001": [
            {
                "reviewId": "r101",
                "rating": 4.5,
                "comment": "Great phone, excellent camera quality!",
                "reviewer": "John D.",
                "date": "2025-03-15"
            },
            {
                "reviewId": "r102",
                "rating": 5.0,
                "comment": "Best smartphone I've ever owned. Battery life is amazing.",
                "reviewer": "Sarah M.",
                "date": "2025-03-10"
            }
        ],
        "p002": [
            {
                "reviewId": "r201",
                "rating": 4.0,
                "comment": "Powerful laptop, but runs a bit hot under heavy load.",
                "reviewer": "Michael T.",
                "date": "2025-02-28"
            },
            {
                "reviewId": "r202",
                "rating": 4.8,
                "comment": "Perfect for my development work. Fast and reliable.",
                "reviewer": "Lisa K.",
                "date": "2025-03-05"
            }
        ],
        "p003": [
            {
                "reviewId": "r301",
                "rating": 4.7,
                "comment": "Excellent noise cancellation and sound quality.",
                "reviewer": "Robert J.",
                "date": "2025-03-20"
            }
        ],
        "p004": [
            {
                "reviewId": "r401",
                "rating": 3.5,
                "comment": "Good features but battery life could be better.",
                "reviewer": "Emma S.",
                "date": "2025-03-12"
            },
            {
                "reviewId": "r402",
                "rating": 4.2,
                "comment": "Accurate fitness tracking and comfortable to wear.",
                "reviewer": "David L.",
                "date": "2025-03-18"
            }
        ],
        "p005": [
            {
                "reviewId": "r501",
                "rating": 4.9,
                "comment": "Amazing sound quality for its size. Truly waterproof!",
                "reviewer": "Jennifer P.",
                "date": "2025-03-22"
            }
        ]
    }
    
    # Get reviews for the specified product ID or return empty list if not found
    reviews = reviews_by_product.get(product_id, [])
    
    # If product ID doesn't exist in our mock data, return a 404
    if not product_id or product_id not in reviews_by_product:
        return {
            "statusCode": 404,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Product not found"})
        }
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "productId": product_id,
            "reviews": reviews
        })
    }
