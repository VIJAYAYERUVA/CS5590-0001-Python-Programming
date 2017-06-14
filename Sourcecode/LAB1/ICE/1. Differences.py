from platform import python_version

print('-------------------------------------------')

print('Difference1: print statement')

#print 'Python', python_version())
#print 'Hello, World!'
#print('Hello, World!')
#print "text", ; print 'print more text on the same line'

print('Python', python_version())

print('Hello, World!')

print("some text,", end="")
print('print more text on the same line')

print('-------------------------------------------')

print('Difference2: Integer division')
#print 'Python', python_version()
#print '3 / 2 =', 3 / 2
#print '3 // 2 =', 3 // 2
#print '3 / 2.0 =', 3 / 2.0
#print '3 // 2.0 =', 3 // 2.0

print('Python', python_version())
print('3 / 2 =', 3 / 2)
print('3 // 2 =', 3 // 2)
print('3 / 2.0 =', 3 / 2.0)
print('3 // 2.0 =', 3 // 2.0)

print('-------------------------------------------')

print('Difference3: Unicode/byte/bytearray')
# print type(unicode('this is like a python3 str type'))

print('Python', python_version())
print('strings are now utf-8 \u03BCnico\u0394é!')
print('-------------------------------------------')