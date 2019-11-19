from datetime import datetime

now = datetime.now()

hora = "{}:{}:{}".format(now.hour,now.minute,now.second)



print(hora)