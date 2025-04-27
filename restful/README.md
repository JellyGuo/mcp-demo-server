# Product API

This is a serverless application built with AWS SAM that provides a REST API for product information and reviews.

## Architecture

The application consists of:
- API Gateway with two endpoints
- Two Lambda functions:
  - `GetProductsFunction`: Returns a list of products
  - `GetProductReviewsFunction`: Returns reviews for a specific product ID

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /products | Get a list of all products |
| GET | /products/{productId}/reviews | Get reviews for a specific product |

## Setup and Deployment

### Prerequisites

- AWS CLI installed and configured
- AWS SAM CLI installed
- Python 3.9

### Deploy the application

```bash
cd product-api
sam build
sam deploy --guided
```

During the guided deployment, you'll be prompted to provide:
- Stack name
- AWS Region
- Other parameters as defined in the template

### Testing the API

After deployment, you'll receive an API Gateway endpoint URL. You can test the API using:

```bash
# Get all products
curl https://your-api-id.execute-api.region.amazonaws.com/Prod/products

# Get reviews for a specific product
curl https://your-api-id.execute-api.region.amazonaws.com/Prod/products/p001/reviews
```

## Local Development

You can test the Lambda functions locally using SAM CLI:

```bash
# Invoke the get_products function locally
sam local invoke GetProductsFunction

# Invoke the get_product_reviews function with event data
sam local invoke GetProductReviewsFunction --event events/get_product_reviews_event.json
```

## API Documentation

The API is documented using OpenAPI 3.0.1 specification. You can find the full API documentation in the `openapi.yaml` file.

## Mock Data

The Lambda functions currently use mock data. In a production environment, you would replace this with actual database queries or service calls.
