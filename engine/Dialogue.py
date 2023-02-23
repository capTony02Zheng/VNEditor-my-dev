import Character


class Dialogue:
    def __init__(self, dialogue: str, character: Character = None):
        """
        constructor for character

        :param dialogue: dialogue text
        :param character: who speak it
        """
        self.dialogue = dialogue
        self.character = character
