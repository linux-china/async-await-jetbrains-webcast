import unittest
import asyncio
import uvloop

uvloop.install()
loop = asyncio.get_event_loop()


async def do_some_work(x):
    print('Waiting: ', x)


class EventLoopTest(unittest.TestCase):

    def test_runtask(self):
        coroutine = do_some_work(2)
        # task = asyncio.ensure_future(coroutine)
        task = loop.create_task(coroutine)
        loop.run_until_complete(task)


if __name__ == '__main__':
    unittest.main()
