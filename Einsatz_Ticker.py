#das der mir nicht auf den sack geht
import ctypes
import time
import os
import requests
import json
import copy
import colorama
import keyboard
from win10toast import ToastNotifier
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from datetime import date

#-------------------------------------------------------------------

import subprocess
import sys
import time
# Module Testen
def install(module):
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", module], shell=False, check=True)
    except subprocess.CalledProcessError:
        error_Nachricht = f"Das Modul {module} konnte nicht installiert werden."
        print(error_Nachricht)
        sys.exit(error_Nachricht)
        
def Test_modul():
    Benoetigte_module = ["ctypes", "time", "os", "requests", "json", "copy", "colorama", "win10toast", "bs4", "prettytable", "datetime", "keyboard" ]

    for module in Benoetigte_module:
        try:
            __import__(module)
        except ImportError:
            print(f"Das Modul {module} ist nicht installiert. Es wird nun installiert.")
            install(module)
            print(f"Das Modul {module} wurde erfolgreich installiert.")
            time.sleep(1)
            
    print('Alle Module wurde überprüft')

# Internet test
def Test_internet():
    URL_noe1 = 'https://www.frig.at/fire'
    URL_noe2 = 'https://infoscreen.florian10.info/ows/wastlmobileweb/'

    connections = [(URL_noe1, "Verbindung NÖ1"), (URL_noe2, "Verbindung NÖ2")]

    for conn in connections:
        try:
            response = requests.get(conn[0], timeout=5)
            response.raise_for_status()
            print(f"{conn[1]} OK")
        except requests.exceptions.RequestException as e:
            print(f"{conn[1]} FEHLER: {e}")
            error_Nachricht = f"Verbindung zu {conn[1]} konnte nicht hergestellt werden."
            print(error_Nachricht)
            sys.exit(error_Nachricht)
    print("Alle Verbindungen sind ok.")
    time.sleep(3)

# Bezirk wählen
def waehle_Bezirk_NOE():
    for i, (k, v) in enumerate(BEZIRKEOE.items()):
        print(f"{i + 1}. {k}")
    auswahl_Bezirk = int(
        input("Wählen Sie den Bezirk aus (1 bis " + str(len(BEZIRKEOE)) + "): "))
    ausgewaehltes_Bezirk = list(BEZIRKEOE.items())[auswahl_Bezirk - 1]
    print(f"Du hast {ausgewaehltes_Bezirk[0]} Ausgewält")
    ctypes.windll.kernel32.SetConsoleTitleW("Einsatzticker V2 NÖ  "'{ausgewaehltes_Bezirk[0]}')
    return ausgewaehltes_Bezirk[1]

BEZIRKEOE = {
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

# Bereich wählen NÖ
def waehle_bereich_NOE():
    while True:
        print("Gib 1 ein, um die laufenden Einsätze zu sehen")
        print("Gib 2 ein, um die Einsatz-Rückblicke zu sehen")
        Ausgewaelt_Bereich_NOE = input()
        if Ausgewaelt_Bereich_NOE == "1":
            print('Du Hast laufenden Einsätze ausgewält')
            time.sleep(1)
            return Ausgewaelt_Bereich_NOE
        elif Ausgewaelt_Bereich_NOE == "2":
            print('Du Hast Einsatz-Rückblicke ausgewält')
            time.sleep(1)
            return Ausgewaelt_Bereich_NOE
        else:
            print("Bitte wähle nur 1-2 aus")
            waehle_bereich_NOE

# Auswahl NÖ
def NOE_Auswahl():
    Bereich_NOE = waehle_bereich_NOE()
    Bezirk_NOE = waehle_Bezirk_NOE()
    if Bereich_NOE ('2'):
        if Bezirk_NOE != 'X':
            Bezirk_NOE = str('bezirk_' (Bezirk_NOE))
        else:
            Bezirk_NOE = 'bezirk_LWZ'
    else:
        return(Bereich_NOE, Bezirk_NOE)

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
    "Niederösterreich": "NOE",
    'Exit': 'EX',
}

def Start(Bereich_NOE, Bezirk_NOE):
    if Bereich_NOE == '1':
        callback = "jQuery18208820398992410197_1677659902952"
        Feuerwehr_im_Einsatz_NOE(Bezirk_NOE,callback)
    else:
        URL_Einsatz_Rueckblicke = URL_Erstellen_Einsatz_Rueckblicke(Bezirk_NOE)
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

def Testmodus():
    os.system('cls')
    print("Testmodus aktiviert")
    ctypes.windll.kernel32.SetConsoleTitleW("Test modus Einsatzticker V2")
    Grund = "Noch nicht gemacht"
    exit(Grund)
        
# Start vorberreitung
if __name__ == "__main__":
    while not keyboard.is_pressed('alt'):
        Test_modul()
        Test_internet()
        # Test Fertig
        subprocess.run("cls", shell=True)
        subprocess.run("echo off", shell=True)
        ctypes.windll.kernel32.SetConsoleTitleW("Einsatzticker V2")
        print('Wilkommen im Einsatzticker')
        print('V2 Von MCBlatt')
        if keyboard.is_pressed('alt'):
                Testmodus()
        while True:
            ausgewaehltes_Bundesland = Auswahl_Bundeslandes()
            time.sleep(2)
            if ausgewaehltes_Bundesland == 'NOE':
                ctypes.windll.kernel32.SetConsoleTitleW("Einsatzticker V2 NÖ")
                os.system('cls')
                NOE_Auswahl()
                Start(Bereich_NOE, Bezirk_NOE)
            elif ausgewaehltes_Bundesland == 'EX':
                exit()