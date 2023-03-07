import datetime

print("yesterday:", datetime.datetime.now()-datetime.timedelta(1))
print("today:", datetime.datetime.now())
print("tommorow:", datetime.datetime.now()+datetime.timedelta(1))