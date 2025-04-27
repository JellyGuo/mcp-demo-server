from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("product")

# Constants
API_BASE = "https://j9nxuk46wf.execute-api.us-west-2.amazonaws.com/Prod"
USER_AGENT = "product-app/1.0"

async def make_api_request(url: str) -> dict[str, Any] | None:
    """Make a request to the Product API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

def format_product(product: dict) -> str:
    """Format a product into a readable string."""
    return f"""
Product ID: {product.get('productId', 'Unknown')}
Name: {product.get('name', 'Unknown')}
Price: ${product.get('price', 0):.2f}
Category: {product.get('category', 'Unknown')}
Description: {product.get('description', 'No description available')}
"""

def format_review(review: dict) -> str:
    """Format a review into a readable string."""
    return f"""
Review ID: {review.get('reviewId', 'Unknown')}
Rating: {review.get('rating', 0)}/5.0
Comment: {review.get('comment', 'No comment')}
Reviewer: {review.get('reviewer', 'Anonymous')}
Date: {review.get('date', 'Unknown')}
"""

@mcp.tool()
async def get_products() -> str:
    """Get all available products."""
    url = f"{API_BASE}/products"
    data = await make_api_request(url)

    if not data or "products" not in data:
        return "Unable to fetch products or no products found."

    if not data["products"]:
        return "No products available."

    products = [format_product(product) for product in data["products"]]
    return "\n---\n".join(products)

@mcp.tool()
async def get_product_reviews(product_id: str) -> str:
    """Get reviews for a specific product.
    
    Args:
        product_id: ID of the product to get reviews for
    """
    url = f"{API_BASE}/products/{product_id}/reviews"
    data = await make_api_request(url)

    if not data:
        return "Unable to fetch reviews for this product."

    if "error" in data:
        return f"Error: {data['error']}"

    if "reviews" not in data or not data["reviews"]:
        return f"No reviews found for product {product_id}."

    reviews = [format_review(review) for review in data["reviews"]]
    return f"Reviews for product {product_id}:\n\n" + "\n---\n".join(reviews)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
