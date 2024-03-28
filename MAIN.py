import json

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

class Salone