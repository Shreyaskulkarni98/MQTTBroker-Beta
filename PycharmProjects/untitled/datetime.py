import datetime

a=datetime.datetime.now().strftime("%d/%B/%Y %I:%M:%S %p")
print(a)
a=datetime.datetime.now().strftime("%c")
print(a)
a=datetime.datetime.now().strftime("%X %x %z %U")
print(a)