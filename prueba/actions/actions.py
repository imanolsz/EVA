from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher

TEMAS = ["ciudadanía", "recaudación"]
DEPARTAMENTOS = ["acción social","hacienda", "finanzas"]
DESTINATARIOS = ["empresas", "personas físicas", "personas jurídicas"]
TRAMITES = ["Trámite 1", "Trámite 2", "Trámite 3", "Trámite 4"]

class ActionHelloWorld(FormValidationAction):

    def name(self) -> Text:
        return "validate_tramite_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")


        return []
