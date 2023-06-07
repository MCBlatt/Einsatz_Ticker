# Importieren der benötigten Module
import subprocess
import sys
# Testen und Installieren der Module
def install(module):
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", module], shell=False, check=True)
    except subprocess.CalledProcessError:
        error_Nachricht = f"Das Modul {module} konnte nicht installiert werden."
        print(error_Nachricht)
        sys.exit(error_Nachricht)
        
def Test_modul():
    Benoetigte_module = ["ctypes", "time", "requests", "json", "copy", "colorama", "bs4", "prettytable", "datetime","subprocess", "sys", "time", "msvcrt", "plyer"]
    for module in Benoetigte_module:
        try:
            __import__(module)
        except ImportError:
            print(f"Das Modul {module} ist nicht installiert. Es wird nun installiert.")
            install(module)
            print(f"Das Modul {module} wurde erfolgreich installiert.")
            time.sleep(1)
    print('Alle Module wurde überprüft')

# Internetverbindung testen
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
            print(f"{conn[1]} Debug: FEHLER: {e}")
            notification.notify(
                title="Fehler",
                message="Verbindung Zum Server konnte nicht hergestellt werden.",
                timeout=10,
                )
            error_Nachricht = colorama.Fore.RED + f"Verbindung zu {conn[1]} konnte nicht hergestellt werden. Prgramm Beendet" + colorama.Fore.WHITE
            sys.exit(error_Nachricht)
    print("Alle Verbindungen sind ok.")
    time.sleep(3)

# Bezirk in Niederösterreich auswählen
def waehle_Bezirk_NOE():
    for i, (k, v) in enumerate(BEZIRKEOE.items()):
        print(f"{i + 1}. {k}")
    while True:
        try:
            auswahl_Bezirk = int(input("Wählen Sie den Bezirk aus (1 bis " + str(len(BEZIRKEOE)) + "): "))
            if 1 <= auswahl_Bezirk <= len(BEZIRKEOE):
                break
            else:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und " + str(len(BEZIRKEOE)) + " ein.")
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
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

# Bereich in Niederösterreich auswählen
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
            waehle_bereich_NOE()

# Auswahl für Niederösterreich
def NOE_Auswahl():
    Bereich_NOE = waehle_bereich_NOE()
    Bezirk_NOE = waehle_Bezirk_NOE()
    if Bereich_NOE == '1':
        if Bezirk_NOE != 'X':
            Bezirk_NOE = ('bezirk_' + Bezirk_NOE)
        else:
            Bezirk_NOE = 'bezirk_LWZ'
    return(Bereich_NOE, Bezirk_NOE)

# Auswahl des Bundeslandes
def Auswahl_Bundeslandes():
    for i, (k, v) in enumerate(BUNDESLAND.items()):
        print(f"{i + 1}. {k}")
    while True:
        try:
            auswahl_Bundesland = int(input("Wählen Sie den Bezirk aus (1 bis " + str(len(BUNDESLAND)) + "): "))
            if 1 <= auswahl_Bundesland <= len(BUNDESLAND):
                break
            else:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und " + str(len(BUNDESLAND)) + " ein.")
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
    ausgewaehltes_item_Bund = list(BUNDESLAND.items())[auswahl_Bundesland - 1]
    print(f"Du hast {ausgewaehltes_item_Bund[0]} Ausgewält")
    return ausgewaehltes_item_Bund[1]
# Bundesländer-Liste
BUNDESLAND = {
    "Niederösterreich": "NOE",
    'Exit': 'EX',
}

# URL für Einsatz-Rückblicke erstellen
def URL_Erstellen_Einsatz_Rueckblicke(Ausgewaelt_Bezirk_NOE):
    if Ausgewaelt_Bezirk_NOE != 'X':
        Datum_heute = date.today().strftime("%d.%m.%Y")
        Sekunden_heute = int(time.strftime("%S"))
        Minuten_Heute = int(time.strftime('%M'))*60
        Stunden_Heute = (int(time.strftime('%H'))*60)*60
        Sekunden_Tag = Sekunden_heute + Minuten_Heute + Stunden_Heute
        Url = 'https://www.feuerwehr-krems.at/CodePages/Wastl/WastlMain/Land_EinsatzHistorie.asp?bezirk=' + Ausgewaelt_Bezirk_NOE + '&' + str(Datum_heute) + str(Sekunden_Tag)
        return Url
    else:
        return 'https://www.feuerwehr-krems.at/CodePages/Wastl/WastlMain/Land_EinsatzHistorie.asp'
# URL für Feuerwehr im Einsatz erstellen
def URL_Erstellen_Feuerwehr_im_Einsatz(Bezirk_NOE, callback):
    return f"https://infoscreen.florian10.info/OWS/wastlMobile/getEinsatzAktiv.ashx?callback={callback}&id={Bezirk_NOE}"

# Der Ticker
def Feuerwehr_im_Einsatz_NOE(Bezirk_NOE, callback):
    subprocess.run(["cls"], shell=True)
    alte_Einsaetze = []
    abgeschlossene_Einsaetze = []
    while True:
        if msvcrt.kbhit():
            if msvcrt.getwche().lower() == 'q':
                subprocess.run(["cls"], shell=True)
                break
        daten = requests.get(
            URL_Erstellen_Feuerwehr_im_Einsatz(Bezirk_NOE, callback)).text
        daten = daten[len(callback)+1:-1]
        daten = json.loads(daten)
        daten = daten["Einsatz"]
        neue_Einsaetze = []
        translationDict = {"B": colorama.Fore.RED, "T": colorama.Fore.BLUE,
                           "S": colorama.Fore.GREEN, "D": colorama.Fore.WHITE}
        if len(alte_Einsaetze) != 0:
            abgeschlossene_Einsaetze = abgeschlossene_Einsaetze + \
                [altes_event for altes_event in alte_Einsaetze if altes_event["i"]
                    not in [new_event["i"] for new_event in daten]]
            neue_Einsaetze = [neues_event for neues_event in daten if neues_event["i"] not in [
                altes_event["i"] for altes_event in alte_Einsaetze]]
            print("Aktuelle Einsaetze:\n")
            for event in alte_Einsaetze:
                color = translationDict.get(event['a'][0])
                print(
                    f"{color + event['a']+colorama.Fore.WHITE:<7} {event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}")
            if len(neue_Einsaetze) != 0:
                print("\n")
                print("Neue Einsaetze:\n")
                for event in neue_Einsaetze:
                    color = translationDict.get(event['a'][0])
                    print(
                        f"{color + event['a']+colorama.Fore.WHITE:<7} {event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}")
                    notification.notify(
                        title="Neuer Einsatz",
                        message=f"{event['a']:<4}{event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}",
                        timeout=10,
                    )
            print()
            if len(abgeschlossene_Einsaetze) != 0:
                print("\n")
                print("Fertige Einsaetze:\n")
                for event in abgeschlossene_Einsaetze:
                    color = translationDict.get(event['a'][0])
                    print(
                        f"{color + event['a']+colorama.Fore.WHITE:<7} {event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}")
                print()
        else:
            print("Aktuelle Einsaetze:\n")
            for event in daten:
                color = translationDict.get(event['a'][0])
                print(
                    f"{color + event['a']+colorama.Fore.WHITE:<7} {event['m']:<70}{event['o']:<35}{event['t']:<10}{event['d']:<10}")
        alte_Einsaetze = copy.copy(daten) + neue_Einsaetze
        print("-" * 150)
        print ("Wenn du wieder zurück ins Menü gehen willst, dann drücke Q (kann bis zu 30 Sek Dauern)")
        time.sleep(30)
        subprocess.run(["cls"], shell=True)
        try:
            daten = requests.get(
                URL_Erstellen_Feuerwehr_im_Einsatz(Bezirk_NOE, callback), timeout=5).text
            daten = daten[len(callback)+1:-1]
            daten = json.loads(daten)
            daten = daten["Einsatz"]
        except requests.exceptions.RequestException as e:
            notification.notify(
                title="Fehler",
                message="Verbindung Zum Server Verloren.",
                timeout=10,
                )
            error_Nachricht = colorama.Fore.RED + "Verbindung Zum Server Verloren. Programm beendet" + colorama.Fore.WHITE
            sys.exit(error_Nachricht)
 # Starten der Anwendung
def Start(Bereich_NOE, Bezirk_NOE):
    if Bereich_NOE == '1':
        callback = "jQuery18207186704915867632_1686042466773"
        Feuerwehr_im_Einsatz_NOE(Bezirk_NOE,callback)
    else:
        URL_Einsatz_Rueckblicke = URL_Erstellen_Einsatz_Rueckblicke(Bezirk_NOE)
        translationDict = {"B": colorama.Fore.RED, "T": colorama.Fore.BLUE,
                           "S": colorama.Fore.GREEN, "D": colorama.Fore.WHITE}
        response = requests.get(URL_Einsatz_Rueckblicke, timeout=5, verify=True)
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
     
# Start vorberreitung
if __name__ == "__main__":
    subprocess.run(["cls"], shell=True)
    Test_modul()
    import ctypes
    import time
    import requests
    import json
    import copy
    import colorama
    import msvcrt
    from plyer import notification
    from bs4 import BeautifulSoup
    from prettytable import PrettyTable
    from datetime import date
    Test_internet()
    # Test Fertig
    subprocess.run(["cls"], shell=True)
    subprocess.run(["echo", "off"], shell=True)
    ctypes.windll.kernel32.SetConsoleTitleW("Einsatzticker V2")
    print('Wilkommen im Einsatzticker')
    print('V2 Von MCBlatt')
    while True:
        ausgewaehltes_Bundesland = Auswahl_Bundeslandes()
        time.sleep(2)
        if ausgewaehltes_Bundesland == 'NOE':
            ctypes.windll.kernel32.SetConsoleTitleW("Einsatzticker V2 NÖ")
            subprocess.run(["cls"], shell=True)
            Bereich_NOE, Bezirk_NOE = NOE_Auswahl()
            Start(Bereich_NOE, Bezirk_NOE)
        elif ausgewaehltes_Bundesland == 'EX':
            subprocess.run(["cls"], shell=True)
            exit()