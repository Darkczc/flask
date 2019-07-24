# -*- coding: utf-8 -*-
from captcha.image import ImageCaptcha
from redis import Redis,ConnectionPool
image=ImageCaptcha()
url_id='abcd'
TIME_CACHE=5
data=image.generate('1234')
image.write('1234','out.png')
redis_pool=ConnectionPool(host='192.168.95.26',port=6379,password='l1zll0twUzyF',decode_responses=True)
redis_con=Redis(connection_pool=redis_pool)
redis_con.setex(url_id,300,'1234')
