"""Trying to do prime number algorithm with functional approach :)

Try online: http://ideone.com/gzLXHh
"""
s=filter(lambda i:all([i%x!=0 for x in range(2,i)]),range(2,1000))
print s
