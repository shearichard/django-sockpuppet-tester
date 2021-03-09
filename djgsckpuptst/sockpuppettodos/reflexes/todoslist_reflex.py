from sockpuppet.reflex import Reflex


class TodoslistReflex(Reflex):
    def increment(self, step=1):
        self.count = int(self.element.dataset['count']) + step
