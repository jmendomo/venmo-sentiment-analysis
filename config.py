#declaring constant variables for transaction and graph lists

weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

YEAR = 0
MONTH = 1
DAY_M = 2
DAY_W = 3
TIME = 4
SCORE = 5
EMOJIS = 6
JULY = 0
AUGUST = 1
OCTOBER = 2
Y_19 = 3
Y_18 = 4

for i in range(31):
    exec("D_{} = {}".format(i+1,i+5))
for i in range(len(weekDays)):
    exec("{} = {}".format(weekDays[i].upper(),i+36))
for i in range(24):
    exec("H_{} = {}".format(i,i+44))
    
july = []
august = []
october = []
y_19 = []
y_18 = []
stats_list = [july, august, october, y_19, y_18]

for i in range(31):
    exec("d_{} = []".format(i+1))
    exec("stats_list.append(d_{})".format(i+1))

for i in range(len(weekDays)):
    exec("{} = []".format(weekDays[i].lower()))
    exec("stats_list.append({})".format(weekDays[i].lower()))

for i in range(24):
    exec("h_{} = []".format(i))
    exec("stats_list.append(h_{})".format(i))
    
venmo_data = []
score_data = []
