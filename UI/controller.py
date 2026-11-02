import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO

    # Mostra tutti gli strumenti presenti nel database
    def mostra_strumenti(self, e):

        # Recupero gli strumenti dal Model
        strumenti = self._model.get_strumenti()

        # Svuoto la lista prima di inserire i nuovi risultati
        self._view.lista_strumenti.controls.clear()


        if strumenti is None:
            self._view.show_alert("Errore durante il recupero degli strumenti dal database.")


        elif len(strumenti) == 0:
            self._view.lista_strumenti.controls.append(
                ft.Text("Non sono presenti strumenti nel deposito.")
            )


        else:
            for strumento in strumenti:
                self._view.lista_strumenti.controls.append(
                    ft.Text(str(strumento))
                )


        self._view.update()

    # Cerca tutti gli strumenti appartenenti a un determinato tipo
    def cerca_strumenti(self, e):

        # Leggo il tipo inserito dall'utente
        tipo = self._view.input_tipo_strumento.value


        if tipo is None or tipo.strip() == "":
            self._view.show_alert("Inserisci il tipo di strumento da cercare.")
            return


        tipo = tipo.strip()

        # Recupero dal Model gli strumenti del tipo indicato
        strumenti = self._model.cerca_strumenti_per_tipo(tipo)

        # Svuoto la lista dei risultati precedenti
        self._view.lista_strumenti_ricerca.controls.clear()


        if strumenti is None:
            self._view.show_alert("Errore durante la ricerca nel database.")


        elif len(strumenti) == 0:
            self._view.lista_strumenti_ricerca.controls.append(
                ft.Text(f"Nessuno strumento trovato per il tipo: {tipo}")
            )


        else:
            for strumento in strumenti:
                self._view.lista_strumenti_ricerca.controls.append(
                    ft.Text(str(strumento))
                )


        self._view.update()
