# DLC installieren
# import subprocess
# subprocess.check_output("pip install -r requirements.txt")

# DLC
import ctypes
import time
import os
import requests
import json
import copy
import colorama
from win10toast import ToastNotifier
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from datetime import date

# URL Erstellen für
def URL_Erstellen_Einsatz_Rueckblicke(Ausgewaelt_Bezirk_NOE):
    if Ausgewaelt_Bezirk_NOE != 'X':
        Ausgewaelt_Bezirk_NOE = '01'
        Datum_heute = date.today().strftime("%d.%m.%Y")
        Sekunden_heute = int(time.strftime("%S"))
        Minuten_Heute = int(time.strftime('%M'))*60
        Stunden_Heute = (int(time.strftime('%H'))*60)*60
        Sekunden_Tag = Sekunden_heute + Minuten_Heute + Stunden_Heute
        Url = 'https://www.feuerwehr-krems.at/CodePages/Wastl/WastlMain/Land_EinsatzHistorie.asp?bezirk=' + \
            Ausgewaelt_Bezirk_NOE + '&' + str(Datum_heute) + str(Sekunden_Tag)
        return Url
    else:
        Url = 'https://www.feuerwehr-krems.at/CodePages/Wastl/WastlMain/Land_EinsatzHistorie.asp'
        return Url

# Der Ticker
def Feuerwehr_im_Einsatz_NOE(callback, Ausgewaelt_Bezirk):
    old_events = []
    completed_events = []
    nb = 0
    toast = ToastNotifier()
    while True:
        data = requests.get(
            URL_Erstellen_Feuerwehr_im_Einsatz(Ausgewaelt_Bezirk)).text
        data = data[len(callback)+1:-1]
        data = json.loads(data)
        data = data["Einsatz"]
        new_events = []
        translationDict = {"B": colorama.Fore.RED, "T": colorama.Fore.BLUE,
                           "S": colorama.Fore.GREEN, "D": colorama.Fore.WHITE}
        if len(old_events) != 0:
            completed_events = completed_events + \
                [old_event for old_event in old_events if old_event["i"]
                    not in [new_event["i"] for new_event in data]]
            new_events = [new_event for new_event in data if new_event["i"] not in [
                old_event["i"] for old_event in old_events]]
            print("Aktuelle Einsaetze:\n")
            for event in old_events:
                color = translationDict.get(event['a'][0])
                print(
                    f"{color + event['a']+colorama.Fore.WHITE:<7} {event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}")
            print()
            if len(completed_events) != 0:
                print("Fertige Einsaetze:\n")
                for event in completed_events:
                    color = translationDict.get(event['a'][0])
                    print(
                        f"{color + event['a']+colorama.Fore.WHITE:<7} {event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}")
                print()
            if len(new_events) != 0:
                print("Neue Einsaetze:\n")
                for event in new_events:
                    color = translationDict.get(event['a'][0])
                    print(
                        f"{color + event['a']+colorama.Fore.WHITE:<7} {event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}")
                    toast.show_toast(
                        "Neuer Einsatz",
                        f"{event['a']:<4}{event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}",
                        duration=10,
                        threaded=True,
                    )
        else:
            print("Aktuelle Einsaetze:\n")
            for event in data:
                color = translationDict.get(event['a'][0])
                print(
                    f"{color + event['a']+colorama.Fore.WHITE:<7} {event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}")
        old_events = copy.copy(data) + new_events
        time.sleep(30)
        os.system('cls')

# URL Erstellen
def URL_Erstellen_Feuerwehr_im_Einsatz(Ausgewaelt_Bezirk_NOE, callback):
    url = f"https://infoscreen.florian10.info/OWS/wastlMobile/getEinsatzAktiv.ashx?callback={callback}&id={Ausgewaelt_Bezirk_NOE}"
    return url

# Start NÖ
def Start_NÖ(Ausgewaelt_Bereich_NOE, Ausgewaelt_Bezirk_NOE):
    if Ausgewaelt_Bereich_NOE == '1':
        callback = "jQuery18208820398992410197_1677659902952"
        url.text = URL_Erstellen_Feuerwehr_im_Einsatz(Ausgewaelt_Bezirk_NOE, callback)
        Feuerwehr_im_Einsatz_NOE(callback, Ausgewaelt_Bezirk_NOE)
    else:
        URL_Einsatz_Rueckblicke = URL_Erstellen_Einsatz_Rueckblicke(Ausgewaelt_Bezirk_NOE)
        translationDict = {"B": colorama.Fore.RED, "T": colorama.Fore.BLUE,
                           "S": colorama.Fore.GREEN, "D": colorama.Fore.WHITE}
        response = requests.get(URL_Einsatz_Rueckblicke)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")
        eine_Tabelle = PrettyTable()
        eine_Tabelle.field_names = ['Melder', 'Ort', 'Stichwort', 'Zeit']
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells:
                stichword = cells[3].text
                color = translationDict.get(stichword[0])
                eine_Tabelle.add_row([cells[1].text, cells[2].text, str(
                    color) + stichword + colorama.Fore.RESET, cells[4].text])
        print(eine_Tabelle)

# Bezirk wählen laufenden_Einsätze
def Einsatz_Rueckblicke_waehle_Bezirk_NOE():
    for i, (k, v) in enumerate(RBEZIRKENOE.items()):
        print(f"{i + 1}. {k}")
    auswahl_Bezirk = int(
        input("Wählen Sie den Bezirk aus (1 bis " + str(len(RBEZIRKENOE)) + "): "))
    ausgewaehltes_Bezirk = list(RBEZIRKENOE.items())[auswahl_Bezirk - 1]
    print(f"Du hast {ausgewaehltes_Bezirk[0]} Ausgewält")
    return ausgewaehltes_Bezirk[1]

RBEZIRKENOE = {
    "Amstetten": "01",
    "Baden": "02",
    "Bruck/Leitha": "03",
    "Gänserndorf": "04",
    "Gmünd": "05",
    "Klosterneuburg": "061",
    "Purkersdorf": "062",
    "Schwechat": "063",
    "Hollabrunn": "07",
    "Horn": "08",
    "Stockerau": "09",
    "Krems/Donau": "10",
    "Lilienfeld": "11",
    "Melk": "12",
    "Mistelbach": "13",
    "Mödling": "14",
    "Neunkirchen": "15",
    "St. Pölten": "17",
    "Scheibbs": "18",
    "Tulln": "19",
    "Waidhofen/T.": "20",
    "Wr. Neustadt": "21",
    "Zwettl": "22",
    'Alle': "X"
}

# Bezirk wählen laufenden_Einsätze
def laufenden_Einsaetze_waehle_Bezirk_NOE():
    for i, (k, v) in enumerate(RBEZIRKENOE.items()):
        print(f"{i + 1}. {k}")
    auswahl_Bezirk = int(
        input("Wählen Sie den Bezirk aus (1 bis " + str(len(RBEZIRKENOE)) + "): "))
    ausgewaehltes_Bezirk = list(RBEZIRKENOE.items())[auswahl_Bezirk - 1]
    print(f"Du hast {ausgewaehltes_Bezirk[0]} Ausgewält")
    ctypes.windll.kernel32.SetConsoleTitleW('{ausgewaehltes_Bezirk[0]}')
    return ausgewaehltes_Bezirk[1]

RBEZIRKENOE = {
    "Amstetten": "bezirk_01",
    "Baden": "bezirk_02",
    "Bruck/Leitha": "bezirk_03",
    "Gänserndorf": "bezirk_04",
    "Gmünd": "bezirk_05",
    "Klosterneuburg": "bezirk_061",
    "Purkersdorf": "bezirk_062",
    "Schwechat": "bezirk_063",
    "Hollabrunn": "bezirk_07",
    "Horn": "bezirk_08",
    "Stockerau": "bezirk_09",
    "Krems/Donau": "bezirk_10",
    "Lilienfeld": "bezirk_11",
    "Melk": "bezirk_12",
    "Mistelbach": "bezirk_13",
    "Mödling": "bezirk_14",
    "Neunkirchen": "bezirk_15",
    "St. Pölten": "bezirk_17",
    "Scheibbs": "bezirk_18",
    "Tulln": "bezirk_19",
    "Waidhofen/T.": "bezirk_20",
    "Wr. Neustadt": "bezirk_21",
    "Zwettl": "bezirk_22",
    'Alle': "bezirk_LWZ"
}

# Bereich wählen NÖ
def waehle_bereich_NOE():
    print("Gib 1 ein, um die laufenden Einsätze zu sehen")
    print("Gib 2 ein, um die Einsatz-Rückblicke zu sehen")
    print("Gib 3 ein, um das Programm zu Beenden")
    Ausgewaelt_Bereich_NOE = input()
    if Ausgewaelt_Bereich_NOE == "1":
        print('Du Hast Feuerwehr im Einsatz ausgewält')
        time.sleep(2)
        return Ausgewaelt_Bereich_NOE
    elif Ausgewaelt_Bereich_NOE == "2":
        print('Du Hast Einsatz-Rückblicke ausgewält')
        time.sleep(2)
        return Ausgewaelt_Bereich_NOE
    elif Ausgewaelt_Bereich_NOE == "3":
        print('Tschüss')
        time.sleep(2)
        exit()
    else:
        print("Bitte wähle nur 1-3 aus")
        return waehle_bereich_NOE

# Auswahl NÖ
def NOE_Auswahl():
    Ausgewaelt_Bereich_NOE = waehle_bereich_NOE()
    if Ausgewaelt_Bereich_NOE == '1':
        Ausgewaelt_Bezirk_NOE = laufenden_Einsaetze_waehle_Bezirk_NOE()
        Start_NÖ(Ausgewaelt_Bereich_NOE, Ausgewaelt_Bezirk_NOE)
    if Ausgewaelt_Bereich_NOE == '2':
        Ausgewaelt_Bezirk_NOE = Einsatz_Rueckblicke_waehle_Bezirk_NOE()
        Start_NÖ(Ausgewaelt_Bezirk_NOE, Ausgewaelt_Bereich_NOE)
    else:
        exit

# Auswahl des Bundeslandes
def Auswahl_Bundeslandes():
    for i, (k, v) in enumerate(BUNDESLAND.items()):
        print(f"{i + 1}. {k}")
    auswahl_Bundesland = int(
        input("Wählen Sie den Bezirk aus (1 bis " + str(len(BUNDESLAND)) + "): "))
    ausgewaehltes_item_Bund = list(BUNDESLAND.items())[auswahl_Bundesland - 1]
    print(f"Du hast {ausgewaehltes_item_Bund[0]} Ausgewält")
    return ausgewaehltes_item_Bund[1]


BUNDESLAND = {
    "Burgenland": "Bgld",
    "Oberösterreich": "OOE",
    "Niederösterreich": "NOE",
}

# Verbindungskontrolle
def Verbindungskontrolle():
    URL_Burgenland = 'https://www.lsz-b.at/leistungen/feuerwehr-einsatzkarte/'
    URL_ooe = 'http://intranet.ooelfv.at'
    URL_noe1 = 'https://www.frig.at/fire'
    URL_noe2 = 'https://infoscreen.florian10.info/ows/wastlmobileweb/'

    connections = [(URL_Burgenland, "Verbindung Bgld"), (URL_ooe, "Verbindung OÖ"),
                   (URL_noe1, "Verbindung NÖ1"), (URL_noe2, "Verbindung NÖ2")]

    for conn in connections:
        try:
            response = requests.get(conn[0], timeout=5)
            response.raise_for_status()
            print(f"{conn[1]} OK")
        except requests.exceptions.RequestException as e:
            print(f"{conn[1]} FEHLER: {e}")
            exit(1)
    print("Alle Verbindungen sind ok.")
    time.sleep(3)
# Start vorberreitung
if __name__ == "__main__":
    os.system('cls')
    os.system('echo off')
    ctypes.windll.kernel32.SetConsoleTitleW("Einsatzticker V2")
    print('Wilkommen im Einsatzticker')
    print('V2 Von MCBlatt')
    time.sleep(3)
    Verbindungskontrolle()
    time.sleep(5)
    os.system('cls')
    while True:
        ausgewaehltes_Bundesland = Auswahl_Bundeslandes()
        time.sleep(2)
        if ausgewaehltes_Bundesland == 'NOE':
            ctypes.windll.kernel32.SetConsoleTitleW("Einsatzticker V2 NÖ")
            os.system('cls')
            NOE_Auswahl()
        elif ausgewaehltes_Bundesland == 'OOE':
            OOE_Start()
        elif ausgewaehltes_Bundesland == 'Bgld':
            Bgld_Start()