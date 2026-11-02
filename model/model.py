import mysql

from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO

        # Richiedo una connessione al database, se non è stato possibile collegarsi, restituisco None
        cnx = get_connection()

        if cnx is None:
            return None

        cursor = None

        try:
            # Creo il cursore per eseguire le query SQL
            cursor = cnx.cursor()

            # Query per recuperare tutti gli strumenti
            query = """
                SELECT codice, tipo, marca, anno_acquisto, valore, disponibile
                FROM strumento
            """

            # Eseguo la query
            cursor.execute(query)

            # Recupero tutte le righe restituite dal database
            rows = cursor.fetchall()


            strumenti = []


            for row in rows:
                strumento = Strumento(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5]
                )

                strumenti.append(strumento)

            return strumenti

        except mysql.connector.Error as err:
            print("Errore durante il recupero degli strumenti:", err)
            return None

        finally:
            # Chiudo il cursore e la connessione anche in caso di errore
            if cursor is not None:
                cursor.close()

            cnx.close()


    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO


        cnx = get_connection()


        if cnx is None:
            return None

        cursor = None

        try:

            cursor = cnx.cursor()

            # Query parametrizzata per cercare gli strumenti del tipo indicato
            query = """
                SELECT codice, tipo, marca, anno_acquisto, valore, disponibile
                FROM strumento
                WHERE tipo = %s
            """

            # Il parametro viene passato separatamente dalla query
            cursor.execute(query, (tipo,))

            # Recupero tutte le righe che corrispondono al tipo cercato
            rows = cursor.fetchall()


            strumenti = []

            # Trasformo ogni riga in un oggetto Strumento
            for row in rows:
                strumento = Strumento(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5]
                )

                strumenti.append(strumento)

            return strumenti

        except mysql.connector.Error as err:
            print("Errore durante la ricerca degli strumenti:", err)
            return None

        finally:
            # Chiudo il cursore e la connessione
            if cursor is not None:
                cursor.close()

            cnx.close()

