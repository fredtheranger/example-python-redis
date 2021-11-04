import redis

r = redis.Redis()

r.set('foo', 'bar')
x = r.get('foo')
print(x)

