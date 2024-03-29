import json 
import datetime

class Cliente:
    def __init__(self, nome, cognome, email):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.storico_appuntamenti = []

class Appuntamento:
    def __init__(self, data, ora, tipo_di_servizio, cliente):
        self.data = data
        self.ora = ora
        self.tipo_di_servizio = tipo_di_servizio
        self.cliente = cliente

class Salone:

    def __init__(self):
        self.agenda = []

    def aggiungi_appuntamento(self, appuntameto):
        self.agenda.append(appuntameto)
    def rimuovi_appuntamento(self, appuntamento):
        self.agenda.remove(appuntamento)
    def ricerca_appuntamento_per_cliente(self, cliente):
        return [appuntamento for appuntamento in self.agenda if appuntamento.cliente == cliente]
    def ricerca_appuntamento_per_data(self, data):
        return [appuntamento for appuntamento in self.agenda if appuntamento.data == data]
    
    def carica_file_json(self, nomeFile):
        with open("rubrica.txt", "r") as file:
            contenuto_file = file.read()
            data = json.load(file)
            for x in data:
                cliente_appuntamento = x ["cliente"]
                cliente = Cliente(cliente_appuntamento["nome"], cliente_appuntamento["cognome"], cliente_appuntamento["email"])
                appuntamento = Appuntamento(cliente_appuntamento["data"], cliente_appuntamento["ora"], cliente_appuntamento["tipo_di_servizio"], cliente)
                self.agenda.append(appuntamento)
    def salva_su_file_json(self, nomeFile):
        data = [{"data" : appuntamento.data, "ora" : appuntamento.ora, "tipo_di_servizio" :
                  appuntamento.tipo_di_servizio, 
                 "cliente" : {"nome" : appuntamento.nome, "cognome" : appuntamento.cognome, "email" : appuntamento.email}} 
                for appuntamento in self.agenda]
        with open(nomeFile, "w") as file:
            file.write(data)
            json.dump(data, file, indent=4)

def principale():

    salone = Salone()
    nomeF = "rubrica.txt"
    salone.carica_file_json(nomeF)

    while True:
        print("MENU")
        print("1) Aggiungi un appuntamento: ")
        print("2) Rimuovi un appuntamento: ")
        print("3) Modifica un appuntamento: ")
        print("4) Ricerca un appuntamento per cliente: ")
        print("5) Ricerca un appuntamento per data: ")
        print("6) Esci. ")

        scelta = input("Fai la tua scelta! ")

        if scelta == "1":
            data = input("Inserisci la data (yyyy-mm-dd): ")
            ora = input("Inserisci l'ora (hh:mm): ")
            tipo_di_servizio = input("Inserisci il tipo di servizio: ")
            nome = input("Inserisci il nome: ")
            cognome = input("Inserisci il cognome: ")
            email = input("Inserisci l'emal: ")
            cliente = Cliente(nome, cognome, email)
            appuntamento = (data, ora, tipo_di_servizio, cliente)
            salone.aggiungi_appuntamento(appuntamento)
        elif scelta == "2":
            data = input("Inserisci la data (yyyy-mm-dd): ")
            ora = input("Inserisci l'ora (hh:mm): ")
            tipo_di_servizio = input("Inserisci il tipo di servizio: ")
            nome = input("Inserisci il nome: ")
            cognome = input("Inserisci il cognome: ")
            email = input("Inserisci l'emal: ")
            cliente = Cliente(nome, cognome, email)
            appuntamento = (data, ora, tipo_di_servizio, cliente)
            salone.rimuovi_appuntamento(appuntamento)
        elif scelta == "3":
            data = input("Inserisci la data (yyyy-mm-dd): ")
            ora = input("Inserisci l'ora (hh:mm): ")
            tipo_di_servizio = input("Inserisci il tipo di servizio: ")
            nome = input("Inserisci il nome: ")
            cognome = input("Inserisci il cognome: ")
            email = input("Inserisci l'emal: ")
            cliente = Cliente(nome, cognome, email)
            appuntamento = (data, ora, tipo_di_servizio, cliente)
            salone.rimuovi_appuntamento(appuntamento)
            data = input("Inserisci la data (yyyy-mm-dd): ")
            ora = input("Inserisci l'ora (hh:mm): ")
            tipo_di_servizio = input("Inserisci il tipo di servizio: ")
            nome = input("Inserisci il nome: ")
            cognome = input("Inserisci il cognome: ")
            email = input("Inserisci l'emal: ")
            cliente = Cliente(nome, cognome, email)
            appuntamento = (data, ora, tipo_di_servizio, cliente)
            salone.aggiungi_appuntamento(appuntamento)
        elif scelta == "4":
            nome = input("Inserisci il nome: ")
            cognome = input("Inserisci il cognome: ")
            cliente = Cliente(nome, cognome)
            salone.ricerca_appuntamento_per_cliente(cliente)
        elif scelta == "5":
            data = Cliente(input("Inserisci la data (yyyy-mm-dd): "))
            salone.ricerca_appuntamento_per_data(data)
        elif scelta == "6":
            break

            




principale()

    