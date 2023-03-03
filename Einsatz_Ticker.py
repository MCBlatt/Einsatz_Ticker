# requirements.txt = DLC
import subprocess
subprocess.check_output("pip install -r requirements.txt")

#DLC
import time
import os
import requests
import json
import copy
import colorama
from win10toast import ToastNotifier
from bs4 import BeautifulSoup
from prettytable import PrettyTable

#Der Ticker
def Feuerwehr_im_Einsatz(callback,Ausgewaelt_Bezirk):
    old_events = []
    
    completed_events = []

    nb = 0
    toast = ToastNotifier()

    while True:
        data = requests.get(URL_Erstellen(Ausgewaelt_Bezirk)).text
        data = data[len(callback)+1:-1]
        data = json.loads(data)
        data = data["Einsatz"]
        new_events = []

        translationDict = {"B":colorama.Fore.RED, "T":colorama.Fore.BLUE, "S":colorama.Fore.GREEN, "D":colorama.Fore.WHITE}
        
        if len(old_events) != 0:
            completed_events = completed_events + [old_event for old_event in old_events if old_event["i"] not in [new_event["i"] for new_event in data]]
            new_events = [new_event for new_event in data if new_event["i"] not in [old_event["i"] for old_event in old_events]]

            print("Aktuelle Einsaetze:\n")
            for event in old_events:
                color = translationDict.get(event['a'][0])
                print(f"{color + event['a']+colorama.Fore.WHITE:<7} {event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}")
            print()
            
            if len(completed_events) != 0:
                print("Fertige Einsaetze:\n")
                for event in completed_events:
                    color = translationDict.get(event['a'][0])
                    print(f"{color + event['a']+colorama.Fore.WHITE:<7} {event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}")
                print()

            if len(new_events) != 0:      
                print("Neue Einsaetze:\n")
                for event in new_events:
                    color = translationDict.get(event['a'][0])
                    print(f"{color + event['a']+colorama.Fore.WHITE:<7} {event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}")
                    toast.show_toast(
                        "Neuer Einsatz",
                        f"{event['a']:<4}{event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}",
                        duration = 10,
                        threaded = True,
                    )
        
        else:
           print("Aktuelle Einsaetze:\n")
           for event in data:
                color = translationDict.get(event['a'][0])
                print(f"{color + event['a']+colorama.Fore.WHITE:<7} {event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}")

        old_events = copy.copy(data) + new_events
        time.sleep(30)
        os.system('cls')

# URL
def URL_Erstellen(Ausgewaelt_Bezirk):
  callback = "jQuery18208820398992410197_1677659902952"
  url = f"https://infoscreen.florian10.info/OWS/wastlMobile/getEinsatzAktiv.ashx?callback={callback}&id={Ausgewaelt_Bezirk}"
  return url

# Bezirk wählen
def waehle_bezirk():
    for i, (k, v) in enumerate(BEZIRKE.items()):
        print(f"{i + 1}. {k}")
    auswahl_Bezirk = int(input("Wählen Sie den Bezirk aus (1 bis " + str(len(BEZIRKE)) + "): "))
    ausgewaehltes_item = list(BEZIRKE.items())[auswahl_Bezirk - 1]
    print(f"Du hast {ausgewaehltes_item[0]} Ausgewält")
    return ausgewaehltes_item[1]

BEZIRKE = {
 "Amstetten":"bezirk_01",
 "Baden":"bezirk_02",
 "Bruck/Leitha":"bezirk_03",
 "Gänserndorf":"bezirk_04",
 "Gmünd":"bezirk_05",
 "Klosterneuburg":"bezirk_061",
 "Purkersdorf":"bezirk_062",
 "Schwechat":"bezirk_063",
 "Hollabrunn":"bezirk_07",
 "Horn":"bezirk_08",
 "Stockerau":"bezirk_09",
 "Krems/Donau":"bezirk_10",
 "Lilienfeld":"bezirk_11",
 "Melk":"bezirk_12",
 "Mistelbach":"bezirk_13",
 "Mödling":"bezirk_14",
 "Neunkirchen":"bezirk_15",
 "St. Pölten":"bezirk_17",
 "Scheibbs":"bezirk_18",
 "Tulln":"bezirk_19",
 "Waidhofen/T.":"bezirk_20",
 "Wr. Neustadt":"bezirk_21",
 "Zwettl":"bezirk_22",
 'Alle': "bezirk_LWZ"
}

# Bereich wählen
def waehle_bereich():
 print("Gib 1 ein, um die laufenden Einsätze zu sehen")
 print("Gib 2 ein, um die Einsatz-Rückblicke zu sehen")
 print("Gib 3 ein, um das Programm zu Beenden")
 Ausgewaelt_Bereich = input()
 if Ausgewaelt_Bereich == "1": 
  print ('Du Hast Feuerwehr im Einsatz ausgewält')
  time.sleep(2)
  return Ausgewaelt_Bereich
 elif Ausgewaelt_Bereich == "2":
  print ('Du Hast Einsatz-Rückblicke ausgewält')
  time.sleep(2)
  return Ausgewaelt_Bereich
 elif Ausgewaelt_Bereich == "3":
   print ('Tschüss')
   time.sleep(2)
   exit()
 else:
  print("Bitte wähle nur 1-2 aus")
  return waehle_bereich

# Start 
def Start(Ausgewält_Bezirk, Ausgewält_Bereich):
 if (Ausgewält_Bereich) == '1':
  callback = "jQuery18208820398992410197_1677659902952"
  URL_Erstellen(Ausgewält_Bezirk,)
  Feuerwehr_im_Einsatz(callback,Ausgewaelt_Bezirk)
 elif (Ausgewält_Bereich) == '2':
  translationDict = {"B":colorama.Fore.RED, "T":colorama.Fore.BLUE, "S":colorama.Fore.GREEN, "D":colorama.Fore.WHITE}
  url = "https://www.feuerwehr-krems.at/CodePages/Wastl/WastlMain/Land_EinsatzHistorie.asp"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  table = soup.find("table")
  eine_Tabelle = PrettyTable()
  eine_Tabelle.field_names = ['Melder','Ort','Stichwort','Zeit']
  rows = table.find_all("tr")
  for row in rows:
    cells = row.find_all("td")
    if cells:
     stichword = cells[3].text
     color = translationDict.get(stichword[0])
     eine_Tabelle.add_row([cells[1].text,cells[2].text,str(color) + stichword + colorama.Fore.RESET,cells[4].text])
  print (eine_Tabelle)
  waehle_bereich
  
#Verbindungskontrolle 
def Verbindungskontrolle():
 Haupt_URL = 'https://infoscreen.florian10.info/ows/wastlmobileweb/'
 print("Verbindung wird überprüft")
 try:
  Aufgerufene_Haupt_URL = requests.get(Haupt_URL)
  Aufgerufene_Haupt_URL.raise_for_status()
  print("Verbindung hergestellt!")
  time.sleep(5)
 except requests.exceptions.RequestException:
  print("Verbindung fehlgeschlagen.")
  time.sleep(5)
  exit() 

# Vorbereitung Start
if __name__ == "__main__":
 os.system('echo off')
 os.system('cls')
 print("Willkommen beim Einsatzmonitor")
 print('V1.7 von MCBlatt')
 time.sleep(1)
 Verbindungskontrolle()
 time.sleep(2)
 os.system('cls')
 while True:
  Ausgewaelt_Bereich = waehle_bereich()
  time.sleep(2)
  os.system('cls')
  if Ausgewaelt_Bereich == '2':
   Ausgewaelt_Bezirk = ('')
  else:
   Ausgewaelt_Bezirk = waehle_bezirk()
   time.sleep(2)
   os.system('cls')
  Start(Ausgewaelt_Bezirk, Ausgewaelt_Bereich)