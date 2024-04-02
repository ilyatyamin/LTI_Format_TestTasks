import json

from scripts.fromLTI.platforms.AbstractPlatformQuestion import AbstractPlatformQuestion
from scripts.toLTI import MultipleChoiceQuestion
from scripts.toLTI.conversion_formats import ConversionFormat


class StepikStepQuestion(AbstractPlatformQuestion):

    def parse_one_question(self, parsed_question: MultipleChoiceQuestion, type_of_question: ConversionFormat) -> str:
        if type_of_question == ConversionFormat.MultipleChoiceStepikStep:
            file = {'block': {'source': {}}}

            file['block']['name'] = 'choice'

            if self.is_correct(parsed_question.question_id):
                file['id'] = parsed_question.question_id

            if self.is_correct(parsed_question.has_review):
                file['has_review'] = parsed_question.has_review
            else:
                file['has_review'] = False

            if self.is_correct(parsed_question.creation_time):
                file['time'] = parsed_question.creation_time

            if self.is_correct(parsed_question.question_name):
                file['block']['text'] = parsed_question.question_name

            if self.is_correct(parsed_question.question_text, 'format'):
                if parsed_question.question_text['format'] == 'html':
                    file['block']['source']['is_html_enabled'] = True
                else:
                    file['block']['source']['is_html_enabled'] = False

            if self.is_correct(parsed_question.is_single_answer):
                file['block']['source']['is_multiple_choice'] = not parsed_question.is_single_answer
            else:
                file['block']['source']['is_multiple_choice'] = True

            if self.is_correct(parsed_question.is_always_correct):
                file['block']['source']['is_always_correct'] = parsed_question.is_always_correct
            else:
                file['block']['source']['is_always_correct'] = False

            if self.is_correct(parsed_question.preserve_order):
                file['block']['source']['preserve_order'] = parsed_question.preserve_order
            else:
                file['block']['source']['preserve_order'] = False

            file['block']['source']['sample_size'] = len(parsed_question.options)

            file['block']['source']['is_options_feedback'] = any(len(x.feedback) > 0 for x in parsed_question.options)

            if self.is_correct(parsed_question.video_link):
                file['block']['video'] = parsed_question.video_link

            if self.is_correct(parsed_question.is_single_answer):
                file['block']['options'] = {}
                file['block']['options']['is_multiple_choice'] = parsed_question.is_single_answer

            if self.is_correct(parsed_question.is_deprecated):
                file['block']['is_deprecated'] = parsed_question.is_deprecated
            else:
                file['block']['is_deprecated'] = False

            if self.is_correct(parsed_question.corrected_feedback, 'text'):
                file['block']['feedback_correct'] = parsed_question.corrected_feedback['text']

            if self.is_correct(parsed_question.incorrect_feedback, 'text'):
                file['block']['feedback_wrong'] = parsed_question.incorrect_feedback['text']

            # Options
            if len(parsed_question.options) > 0:
                options = []
                for option in parsed_question.options:
                    opt_json = {}

                    if self.is_correct(option.is_correct):
                        opt_json['is_correct'] = option.is_correct
                    if self.is_correct(option.text, 'text'):
                        opt_json['text'] = option.text['text']
                    if self.is_correct(option.feedback, 'text'):
                        opt_json['feedback'] = option.feedback['text']
                    else:
                        opt_json['feedback'] = ''

                    options.append(opt_json)
                file['block']['source']['options'] = options

            return json.dumps(file, ensure_ascii=False, indent=4)

    def parse_questions(self, parsed_questions: list, type_of_question: ConversionFormat):
        results = []
        if type_of_question == ConversionFormat.MultipleChoiceStepikStep:
            for question in parsed_questions:
                results.append(self.parse_one_question(question, type_of_question))
        return results
