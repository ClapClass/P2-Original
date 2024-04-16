"""
Python-basierte Auslese für die csv-Listen im params-Verzeichnis.

Die csv-Liste wird von der Funktion read(...) ausgelesen und als Liste von 
python dictionaries zurückgegeben. Eine mögliche Form der Auslese ist unter 
__main__ gezeigt. 

Für die Kalibrations-Tabelle des Thermoelements ist die Temperatur ist in 
°C und die Spannung des Thermoelements in mV angegeben. 

Für die Langzeitmessung zur Bestimmung des Wärmegangs der Apparatur für 
Aufgabe 2 ist die Zeit in Sekunden und die Spannung des Thermoelements in 
mV angegeben. 
"""

import csv

def read(path="./params/calibration.csv", *columns):
    """
    Return values of cvs-file as a list of python dictionaries
    """
    d=[]
    with open(path) as f:
        for i,r in enumerate(csv.DictReader(f, delimiter=",")):
            buf={}
            for c in columns:
                if i>0:
                    buf[c] = float(r[c])
                else:
                    buf[c] = r[c]
            d.append(buf)
    return d

if __name__=="__main__":
    d = read("./params/waermegang.csv", "t", "U")
    #d = read("calibration.csv", "T", "U")
    for r in d:
        print("t (in s)=", r["t"], " U (in mV)=", r["U"])
        #print("T (in °C)=", r["T"], " U (in mV)=", r["U"])
  
__version__=1.0    
