import aiohttp
from asyncflows import AsyncFlows


async def main():
    # Load the flow from the file
    flow = AsyncFlows.from_file("hello_world.yaml")

    MY_NAME = "John"
    # Run the flow
    result = await flow.set_vars(name="MY_NAME").run()

    # Print the result
    print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
