import json


class QuestionEncoder(json.JSONEncoder):
    """
    Creates JSON from class "Multiply Choice Question"
    """

    def default(self, obj):
        if obj is None:
            return ''
        return super().default(obj)
