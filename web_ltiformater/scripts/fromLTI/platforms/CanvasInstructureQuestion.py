import json

from scripts.fromLTI.platforms.AbstractPlatformQuestion import AbstractPlatformQuestion
from scripts.toLTI import MultipleChoiceQuestion
from scripts.toLTI.conversion_formats import ConversionFormat


class CanvasInstructureQuestion(AbstractPlatformQuestion):
    def parse_one_question(self, parsed_question: MultipleChoiceQuestion, type_of_question: ConversionFormat, presentation='string'):
        result = {}
        if type_of_question == ConversionFormat.CanvasInstructure:
            if parsed_question.question_type == 'multiply_choice':
                result['question_type'] = 'multiple_choice_question'
                if self.is_correct(parsed_question.question_id):
                    result['id'] = parsed_question.question_id

                if self.is_correct(parsed_question.associated_quiz_id):
                    result['quiz_id'] = parsed_question.associated_quiz_id

                if self.is_correct(parsed_question.assessment_question_id):
                    result['assessment_question_id'] = parsed_question.assessment_question_id

                if self.is_correct(parsed_question.question_name):
                    result['question_name'] = parsed_question.question_name

                if self.is_correct(parsed_question.question_text, 'text'):
                    result['question_text'] = parsed_question.question_text['text']

                if self.is_correct(parsed_question.weight):
                    result['points_possible'] = str(parsed_question.weight)

                if (self.is_correct(parsed_question.corrected_feedback, 'text')
                        and parsed_question.corrected_feedback['format'] == 'text'):
                    result['correct_comments'] = parsed_question.corrected_feedback['text']
                if (self.is_correct(parsed_question.corrected_feedback, 'text')
                        and parsed_question.corrected_feedback['format'] == 'html'):
                    result['correct_comments_html'] = parsed_question.corrected_feedback['text']

                if (self.is_correct(parsed_question.particular_corrected_feedback, 'text')
                        and parsed_question.particular_corrected_feedback['format'] == 'text'):
                    result['neutral_comments'] = parsed_question.particular_corrected_feedback['text']
                if (self.is_correct(parsed_question.particular_corrected_feedback, 'text')
                        and parsed_question.particular_corrected_feedback['format'] == 'html'):
                    result['neutral_comments_html'] = parsed_question.particular_corrected_feedback['text']

                if (self.is_correct(parsed_question.incorrect_feedback, 'text')
                        and parsed_question.incorrect_feedback['format'] == 'text'):
                    result['incorrect_comments'] = parsed_question.incorrect_feedback['text']
                if (self.is_correct(parsed_question.incorrect_feedback, 'text')
                        and parsed_question.incorrect_feedback['format'] == 'html'):
                    result['incorrect_comments_html'] = parsed_question.incorrect_feedback['text']

                if self.is_correct(parsed_question.options):
                    answers = []
                    for answer in parsed_question.options:
                        file = {}
                        if self.is_correct(answer.id):
                            file['id'] = answer.id

                        if self.is_correct(answer.text, 'text') and answer.text['format'] == 'text':
                            file['text'] = answer.text['text']
                            file['html'] = ''
                        if self.is_correct(answer.text, 'text') and answer.text['format'] == 'html':
                            file['html'] = answer.text['text']
                            file['text'] = ''

                        if self.is_correct(answer.feedback, 'text') and answer.feedback['format'] == 'text':
                            file['comments'] = answer.feedback['text']
                            file['comments_html'] = ''
                        if self.is_correct(answer.feedback, 'text') and answer.feedback['format'] == 'html':
                            file['comments'] = ''
                            file['comments_html'] = answer.feedback['text']

                        if self.is_correct(answer.points):
                            file['weight'] = answer.points

                        answers.append(file)
                    result['answers'] = answers
        if presentation == 'string':
            return json.dumps(result, ensure_ascii=False, indent=4)
        elif presentation == 'self':
            return result
        else:
            raise Exception('Incorrect presentation tag!')

    def parse_questions(self, parsed_questions: list, type_of_question: ConversionFormat, presentation='string'):
        result = []
        for question in parsed_questions:
            json_present = self.parse_one_question(question, ConversionFormat.CanvasInstructure, presentation='self')
            result.append(json_present)
        if presentation == 'string':
            return json.dumps(result, ensure_ascii=False, indent=4)
        elif presentation == 'self':
            return result
        else:
            raise Exception('Incorrect presentation tag!')