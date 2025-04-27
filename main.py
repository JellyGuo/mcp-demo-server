"""
MCP 计算器示例项目主入口
"""

import asyncio
from mcp_client.fast_calculator_client import CalculatorClient


async def main():
    """主函数，演示计算器客户端的使用"""
    print("MCP 计算器示例 (使用 fastMCP)")
    print("============================")

    calculator = CalculatorClient()

    # 演示基本操作
    operations = [
        ("add", 10, 5),
        ("subtract", 10, 5),
        ("multiply", 10, 5),
        ("divide", 10, 5),
    ]

    for op, a, b in operations:
        try:
            result = await calculator.calculate(op, a, b)
            print(f"{a} {op} {b} = {result.get('result')}")
        except Exception as e:
            print(f"操作 {op} 失败: {e}")

    print("\n计算器服务测试完成！")


if __name__ == "__main__":
    asyncio.run(main())
