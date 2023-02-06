name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

h = list()
hour = dict()
hourfreq = dict()
#count = 0
for line in fh:
    if line.startswith("From:") : continue
    if not line.startswith("From") : continue
    line = line.split()
    line = line[5]
    line = line[0:2]
    #print(line)
    h.append(line)
    #print(h)



for hour in h:
    hourfreq[hour] = hourfreq.get(hour,0) +1
    #print(hour)
    #print(hourfreq)

freqhourlist = list()
for h,f in hourfreq.items():
    freqhour = (h,f)
    #print(freqhour)
    freqhourlist.append(freqhour)
freqhourlist = sorted(freqhourlist)

for h,f in freqhourlist:
    print(h,f)

#print (freqhourlist)





    #time.append(email[5])
#print(time)
