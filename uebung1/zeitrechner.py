#! python3
import sys

sekunden = int(sys.argv[1])
minuten = sekunden // 60
stunden = minuten // 60
tage = stunden // 24
jahre = tage // 360
sekunden = sekunden - minuten * 60
minuten = minuten - stunden * 60
stunden = stunden - tage * 24
tage = tage - jahre * 360
print("{0} Sekunden sind {1} Jahre, {2} Tag(e), {3} Stunde(n), {4} Minute(n) und {5} Sekunde(n)".format(sys.argv[1],jahre,tage,stunden,minuten,sekunden))