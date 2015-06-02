"""Trying to do prime number algorithm with functional approach :)

Try online: http://ideone.com/gzLXHh
"""
s=filter(lambda num:len([x for x in range(num+1) if x > 0 and num%x==0])==2,range(1000))
print s
