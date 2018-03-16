import weakref

a_set = {0 ,1}
wref = weakref.ref(a_set)
print wref
print wref()
del a_set
print wref() is None
