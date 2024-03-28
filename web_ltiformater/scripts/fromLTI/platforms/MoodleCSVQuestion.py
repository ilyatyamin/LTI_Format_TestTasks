from scripts.fromLTI.platforms.AbstractPlatformQuestion import AbstractPlatformQuestion
from scripts.toLTI import MultipleChoiceQuestion
from scripts.toLTI.conversion_formats import ConversionFormat


class MoodleCSVQuestion(AbstractPlatformQuestion):
    def parse_one_question(self, parsed_question: MultipleChoiceQuestion, type_of_question: ConversionFormat):
        pass

    def __init__(self, type_of_question="multiply_choice"):
        self.type_of_question = type_of_question


