import asyncio


# 定义了一个简单的协程
async def simple_async():
    print('hello')
    await asyncio.sleep(1)  # 休眠1秒
    print('python')


# 使用asynio中run方法运行一个协程
asyncio.run(simple_async())

# 执行结果为
# hello
# python
