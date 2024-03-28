import json

from scripts.fromLTI.platforms.AbstractPlatformQuestion import AbstractPlatformQuestion
from scripts.toLTI import MultipleChoiceQuestion
from scripts.toLTI.conversion_formats import ConversionFormat


class StepikStepQuestion(AbstractPlatformQuestion):
    def parse_one_question(self, parsed_question: MultipleChoiceQuestion, type_of_question: ConversionFormat) -> str:
        if type_of_question == ConversionFormat.MultipleChoiceStepikStep:
            file = {'block': {'source': {}, 'options': []}}

            file['block']['name'] = 'choice'

            if self.__is_correct(parsed_question.question_id):
                file['id'] = parsed_question.question_id

            if self.__is_correct(parsed_question.has_review):
                file['has_review'] = parsed_question.has_review

            if self.__is_correct(parsed_question.creation_time):
                file['time'] = parsed_question.creation_time

            if self.__is_correct(parsed_question.question_name):
                file['block']['text'] = parsed_question.question_name

            if self.__is_correct(parsed_question.question_text, 'format'):
                file['block']['source']['is_html_enabled'] = parsed_question.question_text['format']

            if self.__is_correct(parsed_question.is_single_answer):
                file['block']['source']['is_multiple_choice'] = parsed_question.is_single_answer

            if self.__is_correct(parsed_question.is_always_correct):
                file['block']['source']['is_always_correct'] = parsed_question.is_always_correct

            if self.__is_correct(parsed_question.preserve_order):
                file['block']['source']['preserve_order'] = parsed_question.preserve_order

            if self.__is_correct(parsed_question.video_link):
                file['block']['video'] = parsed_question.video_link

            if self.__is_correct(parsed_question.is_deprecated):
                file['block']['is_deprecated'] = parsed_question.is_deprecated

            if self.__is_correct(parsed_question.corrected_feedback, 'text'):
                file['block']['feedback_correct'] = parsed_question.corrected_feedback['text']

            if self.__is_correct(parsed_question.incorrect_feedback, 'text'):
                file['block']['feedback_wrong'] = parsed_question.incorrect_feedback['text']

            # Options
            if len(parsed_question.options) > 0:
                for option in parsed_question.options:
                    opt_json = {}

                    if self.__is_correct(option.is_correct):
                        opt_json['is_correct'] = option.is_correct
                    if self.__is_correct(option.text, 'text'):
                        opt_json['text'] = option.text['text']
                    if self.__is_correct(option.feedback, 'text'):
                        opt_json['feedback'] = option.feedback['text']

                    file['block']['options'].append(opt_json)

            return json.dumps(file, ensure_ascii=False, indent=4)
