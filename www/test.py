import asyncio
import www.orm
import random
from www.models import User,Blog,Comment

async def test(loop):
    await www.orm.create_pool(loop,user='root',password='jianmeng123',db='awesome')
    u =User(name='test',email='test%s@example.com' % random.randint(0,10000000),passwd='abc123456',image='about:blank')
    await u.save()


#要运行协程，需要使用事件循环
if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test(loop))
        print('Test finished.')
        loop.close()