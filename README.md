# MCP Product Reviews Server

A Model Context Protocol (MCP) server that provides product review data and search functionality.

## Features

- Exposes product list as resources
- Provides tools for searching reviews by product ID, rating, and keywords
- Mock API based on AWS Lambda functions in `/product-api/functions/`
- Designed to be used with CLINE as an SSE server

## Installation

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# Install dependencies
uv pip install "mcp[cli]"
```

## Usage

### Running the MCP Server

```bash
# Run the server directly
python product_mcp_server.py

# Or use the MCP CLI
mcp run product_mcp_server.py
```

### Development Mode

For testing and debugging:

```bash
mcp dev product_mcp_server.py
```

#### 在本地部署
transport 选择 `stdio`,  MCP Client 与 Server 之间通过本地标准 I/O通信
```python
mcp.run(transport='stdio')
```
1. 如果 server 在本地，配置启动命令， CLINE 会通过`mcp run` / `uv run mcp run` / `unx` 等命令启动这个 server， CLINE 集成了 MCP Client 代码，可以与server 通信
2. 如果 server 在远端部署，无论是通过配置 `/etc/systemd/system/mcp-server.service` 使用 `systemctl start mcp-server` 命令启动，还是通过`mcp run` / `uv run mcp run` / `unx` 等命令启动，都可以通过`{host}:{port}/sse`访问，在 CLINE中配置如下进行使用
   ```json
   "{server name}": {
        "url": "http://{host}:{port}:8000/sse",
        "disabled": false,
        "autoApprove": []
      }
   ```

### Integration with CLINE

To use this server with CLINE:

1. Start the MCP server:
   ```bash
   python product_mcp_server.py
   ```

2. Configure CLINE to connect to the server (refer to CLINE documentation for specific steps)

## Available Resources

- `products://all` - Get a list of all products
- `products://{product_id}` - Get details for a specific product
- `reviews://{product_id}` - Get reviews for a specific product

## Available Tools

- `get_products()` - Get a list of all available products
- `get_product_reviews(product_id)` - Get reviews for a specific product
- `search_reviews_by_rating(min_rating)` - Search for reviews with a minimum rating
- `search_reviews_by_keyword(keyword)` - Search for reviews containing a specific keyword

## AWS Lambda Functions

The server includes mock implementations of AWS Lambda functions found in `/product-api/functions/`:

- `get_products.py` - Returns a list of products
- `get_product_reviews.py` - Returns reviews for a specific product

## License

This project is licensed under the MIT License - see the LICENSE file for details.
