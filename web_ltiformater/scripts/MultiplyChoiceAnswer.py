class MultiplyChoiceAnswer:
    """
    Introduce answer-class for questions with type "multiply choice"
    """
    def __init__(self):
        self.text: dict = {}
        self.points = None
        self.is_correct = None
        self.feedback: dict = {}
