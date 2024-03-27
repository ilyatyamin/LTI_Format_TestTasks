from scripts.fromLTI.platforms.MoodleXMLQuestion import MoodleXMLQuestion
from scripts.fromLTI.platforms.StepikStepQuestion import StepikStepQuestion
from scripts.toLTI import MultipleChoiceQuestion

from scripts.toLTI.conversion_formats import ConversionFormat


class PlatformsMultipleChoice:
    def __init__(self):
        self.moodle_xml_formatter = MoodleXMLQuestion()
        self.stepik_formatter = StepikStepQuestion()

    def parse_one_question(self, parsed_question: MultipleChoiceQuestion, type_of_question):
        if type_of_question == ConversionFormat.MultipleChoiceMoodleXML:
            return self.moodle_xml_formatter.parse_one_question(parsed_question, ConversionFormat.MultipleChoiceMoodleXML)
        elif type_of_question == ConversionFormat.MultipleChoiceStepikStep:
            return self.stepik_formatter.parse_one_question(parsed_question, ConversionFormat.MultipleChoiceStepikStep)

