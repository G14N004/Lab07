import flet as ft

from UI.view import View
from model.model import Model
from model.situazione import Situazione


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        lista = self._model.getAllSituazioni()
        match= self._mese
        dizionario={}
        for elm in lista :
            if isinstance(elm,Situazione):
                mese = int(elm.data.month)
                if mese == match:
                    if elm.localita not in dizionario:
                        dizionario[elm.localita]=[]

                    dizionario[elm.localita].append(elm.umidita)


        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text("L'umidità media nel mese selezionato è : "))

        dizionario_media={}
        for chiave,valore in dizionario.items():
            media = sum(valore)/len(valore)
            dizionario_media[chiave]=media
            self._view.lst_result.controls.append(ft.Text(f"{chiave} : {dizionario_media[chiave]:.4f}"))

        self._view.update_page()









    def handle_sequenza(self, e):
        lista=self._model.getAllSituazioni()
        match= self._mese
        lista_filtrata=[elm for elm in lista if elm.data.month == match]
        lista_finale=[elm for elm in lista_filtrata if 1<=elm.data.day<=15]
        self._view.lst_result.controls.clear()



        self._view.update_page()





    def read_mese(self, e):
        self._mese = int(e.control.value)

