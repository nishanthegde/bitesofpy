class RecordScore():
    """Class to track a game's maximum score"""

    def __init__(self):
        self.max_score = None

    def __call__(self, new_value):
        # Update the state_attribute based on the new_value
        if self.max_score is None or new_value > self.max_score:
            self.max_score = new_value
        return self.max_score

    def __repr__(self):
        return self.max_score
