import datetime
print("Введите первую дату через xxxx-xx-xx xx:xx:xx")
a=input()
print("Введите вторую дату через xxxx-xx-xx xx:xx:xx")
b=input()
d1 = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')
d3=d2-d1
print(d3.days * 24 * 3600 + d3.seconds)

