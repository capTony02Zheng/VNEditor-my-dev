from Background import Background
from Branch import BranchTree
from Character import Character
from Dialogue import Dialogue
from Music import Music


class Frame:
    last_frame = True
    id = -1

    def __init__(
        self,
        bg: Background,
        chara: Character,
        music: Music,
        dialog: Dialogue,
        branch: BranchTree = BranchTree.DEFAULT,
    ):
        self.bg = bg
        self.chara = chara
        self.music = music
        self.dialog = dialog
        self.branch = branch

        self.id = -1

    def set_id(self, id: int):
        self.id = id

    def get_id(self):
        return self.id
