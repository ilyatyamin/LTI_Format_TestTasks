from scripts.toLTI import MultipleChoiceQuestion


class MoodleCSVQuestion:
    def __init__(self, type_of_question="multiply_choice"):
        self.type_of_question = type_of_question

    def parse_one_question(self, parsed_question: MultipleChoiceQuestion):
        text = ''

