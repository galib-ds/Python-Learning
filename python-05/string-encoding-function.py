import base64
str = 'This is Galib here...!!..Hello, Hello!!'
str = base64.b64encode(str.encode('utf-8'))
print("Encoded string: ", str)
str = base64.b64decode(str).decode('utf-8')
print("Decoded string: ", str)