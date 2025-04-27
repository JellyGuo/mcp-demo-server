from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import urllib.parse

# 创建服务器参数，用于连接到server.py
server_params = StdioServerParameters(
    command="uv",  # 可执行文件
    args=["run", "mcp", "run", "server.py"],  # 命令行参数
    env=None,  # 环境变量
)


async def run():
    print("启动MCP客户端...")
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 初始化连接
            await session.initialize()
            print("已连接到MCP服务器")

            print("\n===== 调用add工具 =====")
            # 列出可用工具
            tools = await session.list_tools()
            print(f"可用工具: {tools}")

            # 调用add工具
            a, b = 5, 7
            add_result = await session.call_tool("add", arguments={"a": a, "b": b})
            # 从返回结果中提取计算结果
            result_text = add_result.content[0].text if add_result.content else "无结果"
            print(f"调用add工具: {a} + {b} = {result_text}")

            # 再次调用add工具，使用不同的参数
            a, b = 10, 20
            add_result = await session.call_tool("add", arguments={"a": a, "b": b})
            result_text = add_result.content[0].text if add_result.content else "无结果"
            print(f"再次调用add工具: {a} + {b} = {result_text}")

            print("\n===== 访问greeting资源 =====")
            # 列出可用资源
            resources = await session.list_resources()
            print(f"可用资源: {resources}")

            # 访问greeting资源
            name = "世界"
            greeting_uri = f"greeting://{name}"
            print(f"尝试访问资源: {greeting_uri}")
            result = await session.read_resource(greeting_uri)

            # 从返回结果中提取问候语
            if result.contents and len(result.contents) > 0:
                greeting_text = result.contents[0].text
                # URL解码问候语
                try:
                    decoded_text = urllib.parse.unquote(greeting_text)
                    print(f"问候语 (已解码): {decoded_text}")
                except:
                    print(f"问候语 (原始): {greeting_text}")
            else:
                print("未收到问候语")

            # 再次访问greeting资源，使用不同的名称
            name = "MCP用户"
            greeting_uri = f"greeting://{name}"
            print(f"\n再次尝试访问资源: {greeting_uri}")
            result = await session.read_resource(greeting_uri)

            # 从返回结果中提取问候语
            if result.contents and len(result.contents) > 0:
                greeting_text = result.contents[0].text
                # URL解码问候语
                try:
                    decoded_text = urllib.parse.unquote(greeting_text)
                    print(f"问候语 (已解码): {decoded_text}")
                except:
                    print(f"问候语 (原始): {greeting_text}")
            else:
                print("未收到问候语")


if __name__ == "__main__":
    asyncio.run(run())
