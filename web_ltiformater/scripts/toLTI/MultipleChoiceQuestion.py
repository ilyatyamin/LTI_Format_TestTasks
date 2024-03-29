# pip install python-docx
# pip install PyPDF2
# pip install django

import xml.etree.ElementTree as ElTree
from scripts.toLTI.MultiplyChoiceAnswer import MultiplyChoiceAnswer
from scripts.toLTI.Question import Question


class MultiplyChoiceQuestion(Question):
    """
    Class that introduced answer with one or multiply choice answer
    """

    def __init__(self):
        # Obligatory fields
        self.question_type = "multiply_choice"
        self.question_id = None  #
        self.question_name = None  #
        self.question_text: dict = {}
        self.is_single_answer = None
        self.text_style = None
        self.options: list = []
        self.is_needed_feedback = None
        self.is_always_correct = False

        # Optional fields. Depends on the platform
        self.associated_quiz_id = None
        self.assessment_question_id = None
        self.defaultLocale = None
        self.creation_time = None
        self.shuffle_answer = None
        self.corrected_feedback: dict = {}
        self.particular_corrected_feedback: dict = {}
        self.incorrect_feedback: dict = {}
        self.default_grade = None
        self.penalty = None
        self.hidden = None
        self.answer_numbering = None
        self.show_standard_instruction = None
        self.show_num_correct = None
        self.video_link = None
        self.subtitle_files: list = []
        self.is_deprecated = None
        self.has_review = None
        self.preserve_order = None
        self.output_format = None
        self.general_feedback: dict = {}  #
        self.course_id = None
        self.creation_time = None
        self.tags: list = []
        self.prompts: list = []
        self.weight = None

    @staticmethod
    def __converter_to_bool(option):
        if isinstance(option, bool):
            return option
        if isinstance(option, str):
            stripped_option = option.strip()
            if stripped_option == "true" or stripped_option == "1":
                return True
            if stripped_option == "false" or stripped_option == "0":
                return False
        if isinstance(option, int):
            if option == 0:
                return False
            if option == 1:
                return True
        return option

    def parse_one_question_from_moodle_xml(self, parsed_file: ElTree.Element):
        """Parse one question from Moodle XML format. Get ELTree.Element and fill the attributes in himself"""
        if parsed_file.tag != 'question' or parsed_file.attrib['type'] != 'multichoice':
            raise Exception("Not Multiply Choice Question.")

        self.question_name = parsed_file.find("name").find("text").text

        # Parsing question's text and question's text style
        tag_text = parsed_file.find("questiontext")
        if tag_text is not None:
            if 'format' in tag_text.attrib.keys():
                self.question_text['format'] = tag_text.attrib['format']
            else:
                self.question_text['format'] = "text"
            self.question_text['text'] = tag_text.find("text").text

        # Parsing general feedback and it's format
        tag_general_feedback = parsed_file.find("generalfeedback")
        if tag_general_feedback is not None:
            if 'format' in tag_general_feedback.attrib.keys():
                self.general_feedback['format'] = tag_general_feedback.attrib['format']
            else:
                self.general_feedback['format'] = "text"
            self.general_feedback['text'] = tag_general_feedback.find("text").text

        # Parsing default grade
        tag_default_grade = parsed_file.find("defaultgrade")
        if tag_default_grade is not None:
            self.default_grade = tag_default_grade.text

        # Parsing penalty
        tag_penalty = parsed_file.find("penalty")
        if tag_penalty is not None:
            self.penalty = tag_penalty.text

        # Parsing hidden
        tag_hidden = parsed_file.find("hidden")
        if tag_hidden is not None:
            self.hidden = tag_hidden.text

        # Parsing course id
        tag_course_id = parsed_file.find("idnumber")
        if tag_course_id is not None:
            self.course_id = tag_course_id.text

        # Parsing is_single_answer
        tag_is_single_answer = parsed_file.find("single")
        if tag_is_single_answer is not None:
            if tag_is_single_answer.text == "true":
                self.is_single_answer = 1
            else:
                self.is_single_answer = 0

        # Parsing shuffleanswers
        tag_shuffleanswers = parsed_file.find("shuffleanswers")
        if tag_shuffleanswers is not None:
            if tag_shuffleanswers.text == "true":
                self.shuffle_answer = 1
            else:
                self.shuffle_answer = 0

        # Parsing answer numbering style
        tag_answernumbering = parsed_file.find("answernumbering")
        if tag_answernumbering is not None:
            self.answer_numbering = tag_answernumbering.text

        # Parsing showstandardinstruction
        tag_showstandardinstruction = parsed_file.find("showstandardinstruction")
        if tag_showstandardinstruction is not None:
            self.show_standard_instruction = tag_showstandardinstruction.text

        # Parsing correctfeedback: it's format and text
        tag_correctfeedback = parsed_file.find("correctfeedback")
        if tag_correctfeedback is not None:
            if 'format' in tag_correctfeedback.attrib.keys():
                self.corrected_feedback['format'] = tag_correctfeedback.attrib['format']
            else:
                self.corrected_feedback['format'] = "text"
            self.corrected_feedback['text'] = tag_correctfeedback.find("text").text

        # Parsing particullary correctfeedback: it's format and text
        tag_partcorrectfeedback = parsed_file.find("partiallycorrectfeedback")
        if tag_partcorrectfeedback is not None:
            if 'format' in tag_partcorrectfeedback.attrib.keys():
                self.particular_corrected_feedback['format'] = tag_partcorrectfeedback.attrib['format']
            else:
                self.particular_corrected_feedback['format'] = "text"
            self.particular_corrected_feedback['text'] = tag_partcorrectfeedback.find("text").text

        # Parsing incorrect feedback: it's format and text
        tag_incorrfeedback = parsed_file.find("incorrectfeedback")
        if tag_incorrfeedback is not None:
            if 'format' in tag_incorrfeedback.attrib.keys():
                self.incorrect_feedback['format'] = tag_incorrfeedback.attrib['format']
            else:
                self.incorrect_feedback['format'] = "text"
            self.incorrect_feedback['text'] = tag_incorrfeedback.find("text").text

        # Parsing shownumcorrect
        tag_shownumcorrect = parsed_file.find("shownumcorrect")
        if tag_shownumcorrect is not None:
            self.show_num_correct = 1
        else:
            self.show_num_correct = 0

        # Parsing all answers
        all_answers = parsed_file.findall("answer")
        if len(all_answers) != 0:
            for tag_answer in all_answers:
                result = MultiplyChoiceAnswer()
                if "format" in tag_answer.attrib.keys():
                    result.text['format'] = tag_answer.attrib['format']
                else:
                    result.text['format'] = "text"

                # Fraction in this case means points that you have if you will correctly answer on the question
                if "fraction" in tag_answer.attrib.keys():
                    result.points = tag_answer.attrib['fraction']
                else:
                    result.points = "1"

                text = tag_answer.find("text")
                if text is not None:
                    result.text['text'] = text.text

                feedback = tag_answer.find("feedback")
                if "format" in feedback.attrib.keys():
                    result.feedback['format'] = feedback.attrib['format']
                else:
                    result.feedback['format'] = "text"
                feedback_text = feedback.find("text")
                if feedback_text is not None:
                    result.feedback['text'] = feedback_text.text

                self.options.append(result)

    def parse_one_question_moodle_csv(self, lines: list[list[str]], idx: int = 1):
        """
        Parse one question using Moodle CSV format
        Obligatory requirement is headers in first row
        If they are not saved in first row, method throws an exception
        """
        # Check structure
        tags_line = lines[0]
        if len(lines) < idx:
            raise Exception("Incorrect index")
        working_line = lines[idx]

        if "questionname" in tags_line:
            # Checking question_name
            self.question_name = working_line[tags_line.index("questionname")]
            self.question_text = working_line[tags_line.index("questiontext")]

            answers = [working_line[x].strip() for x in range(len(tags_line)) if "Answer " in tags_line[x]]
            # Checking options
            for letter_idx in range(65, 91):  # ['A', 'Z']
                if chr(letter_idx) in tags_line:
                    option = MultiplyChoiceAnswer()
                    idx = tags_line.index(chr(letter_idx))

                    # In CSV there are no format, so we put it "text"
                    option.text['format'] = "text"
                    option.text['text'] = working_line[idx]

                    # Checking is it correct?
                    if chr(letter_idx) in answers:
                        option.is_correct = 1
                    else:
                        option.is_correct = 0
                    self.options.append(option)

            # Checking answer_numbering
            if "answernumbering" in tags_line:
                self.answer_numbering = working_line[tags_line.index("answernumbering")]

            # Checking correctfeedback
            if "correctfeedback" in tags_line:
                self.corrected_feedback['format'] = "text"
                self.corrected_feedback['text'] = working_line[tags_line.index("correctfeedback")]
            if "partiallycorrectfeedback" in tags_line:
                self.particular_corrected_feedback['format'] = "text"
                self.particular_corrected_feedback['text'] = working_line[tags_line.index("partiallycorrectfeedback")]
            if "incorrectfeedback" in tags_line:
                self.incorrect_feedback['format'] = "text"
                self.incorrect_feedback['text'] = working_line[tags_line.index("incorrectfeedback")]

            # Checking default_mark
            if "defaultmark" in tags_line:
                self.default_grade = working_line[tags_line.index("defaultmark")]
        else:
            raise Exception("Structure is not correct")

    def parse_one_question_moodle_docx(self, doc, idx=0):
        """
        Parse one question from Moodle Docx Format
        """

        dict_variables = {'Штраф за каждую неправильную попытку:': "penalty", 'ID-номер:': "question_id",
                          'Случайный порядок ответов': "shuffle_answer", 'Балл по умолчанию:': "default_grade",
                          'Нумеровать варианты ответов?': "answer_numbering"}

        # Divide all variables that can be shown in table for 3 groups: strings, lists and dictionaries (often,
        # format and text)
        dict_noniterable_footer_variables = {
            'ID-номер:': "question_id",
            'Для любого частично правильного ответа:': "particular_corrected_feedback",
            'Для любого правильного ответа:': "corrected_feedback",
            'Для любого неправильного ответа:': "incorrect_feedback"}
        dict_list_footer_variables = {'Теги:': "tags", 'Показать отзыв для выбранных ответов. (Подсказка ):': "",
                                      'Подсказка :': "prompts", }
        dict_dict_footer_variables = {'Общий отзыв к вопросу:': "general_feedback"}

        tables_in_doc = doc.tables
        need_table = tables_in_doc[idx]

        # self.question_name - NEED TO DO
        # question_name in this format highlights af Heading 2
        all_names = [paragraph for paragraph in doc.paragraphs if paragraph.style.name == "Heading 2"]
        self.question_name = all_names[idx].text

        # In first row cell - name
        self.question_text['format'] = "text"  # in this format it is not required
        self.question_text['text'] = need_table.rows[0].cells[0].text

        # Find index of row with answer's header
        idx_answers_headers = -1
        for item in range(len(need_table.rows)):
            if any(x.text == '#' for x in need_table.rows[item].cells):
                idx_answers_headers = item
                break

        # All params that higher than answers
        for row in need_table.rows[1:idx_answers_headers]:
            if row.cells[0].text in dict_variables:
                setattr(self, dict_variables[row.cells[0].text], row.cells[-1].text)

        # Find end on answers
        # Indication: first cell in row is empty (in other rows first row is style of numering (A, B, C))
        end_of_answers = -1
        for idx in range(idx_answers_headers + 1, len(need_table.rows)):
            if need_table.rows[idx].cells[-1].text.isspace():
                end_of_answers = idx
                break

        # Analyzing all answers
        for idx in range(idx_answers_headers + 1, end_of_answers):
            option = MultiplyChoiceAnswer()
            option.text['format'] = 'text'  # default
            option.text['text'] = need_table.rows[idx].cells[1].text
            option.feedback = need_table.rows[idx].cells[2].text
            option.points = need_table.rows[idx].cells[3].text
            if option.points != "0":
                option.is_correct = "1"
            else:
                option.is_correct = "0"
            self.options.append(option)

        for ind in range(end_of_answers, len(need_table.rows) - 1):
            name = ''.join([x for x in need_table.rows[ind].cells[1].text if not (x.isdigit())])
            if name in dict_noniterable_footer_variables.keys():
                setattr(self, dict_noniterable_footer_variables[name],
                        need_table.rows[ind].cells[2].text)
            elif name in dict_list_footer_variables.keys():
                alias = dict_list_footer_variables[name]
                if alias == "tags":
                    self.tags.append(need_table.rows[ind].cells[2].text)
                elif alias == "is_needed_feedback":
                    self.is_needed_feedback = 1
                elif alias == "prompts":
                    self.prompts.append(need_table.rows[ind].cells[2].text)
            elif name in dict_dict_footer_variables.keys():
                alias = dict_dict_footer_variables[name]
                if alias == "general_feedback":
                    self.general_feedback['format'] = 'text'
                    self.general_feedback['text'] = need_table.rows[ind].cells[2].text

    def parse_one_question_stepik(self, parsed_file: dict):
        """
        Parses one question using Stepik format (.step)
        """
        if "block" in parsed_file.keys():
            block = parsed_file['block']
            block_keys = block.keys()
            if "name" in block_keys and block['name'] == "choice":
                self.question_type = "multiply_choice"
            else:
                raise Exception("Not Multiple Choice Question")
            if "text" in block_keys:
                self.question_name = block['text']
                if block['source']['is_html_enabled']:
                    self.question_text['format'] = "html"
                else:
                    self.question_text['format'] = "text"
                self.question_text['text'] = block['text']
            if "video" in block_keys:
                self.video_link = block['video']
            if "is_deprecated" in block_keys:
                self.is_deprecated = self.__converter_to_bool(block['is_deprecated'])
            if 'source' in block_keys:
                source = block['source']
                if "is_multiple_choice" in source.keys():
                    self.is_single_answer = self.__converter_to_bool(source['is_multiple_choice'])
                if 'is_always_correct' in source.keys():
                    self.is_always_correct = self.__converter_to_bool(source['is_always_correct'])
                if 'preserve_order' in source.keys():
                    self.preserve_order = self.__converter_to_bool(source['preserve_order'])

                if source['is_html_enabled']:
                    format_of_answers = 'html'
                else:
                    format_of_answers = 'text'

                if 'options' in source.keys():
                    options = source['options']
                    for option in options:
                        answer = MultiplyChoiceAnswer()
                        if 'is_correct' in option.keys():
                            answer.is_correct = self.__converter_to_bool(option['is_correct'])
                        if 'text' in option.keys():
                            answer.text['format'] = format_of_answers
                            answer.text['text'] = (option['text'])
                        if 'feedback' in option.keys():
                            answer.feedback['format'] = 'text'
                            answer.feedback['text'] = (option['feedback'])
                        self.options.append(answer)
            if 'feedback_correct' in block_keys:
                self.corrected_feedback['format'] = 'text'  # default
                self.corrected_feedback['text'] = block['feedback_correct']
            if 'feedback_wrong' in block_keys:
                self.incorrect_feedback['format'] = 'text'  # default
                self.incorrect_feedback['text'] = block['feedback_wrong']
        if 'id' in parsed_file.keys():
            self.question_id = parsed_file['id']
        if 'has_review' in parsed_file.keys():
            self.has_review = parsed_file['has_review']
        if 'time' in parsed_file.keys():
            self.creation_time = parsed_file['time']

    def parse_one_question_testmoz_word(self, doc, idx=1):
        # print(*([(x.text, x.style.name) for x in doc.paragraphs]), sep='-- END\n')
        all_tables_in_doc = doc.tables
        symbols = ['⬜', '⬛', '⚫', '⚪']
        correct_symbols = ['⚫', '⬛']

        tables_with_def = [x for x in all_tables_in_doc if str(idx) in x.rows[0].cells[0].text.strip()]

        if len(tables_with_def) == 0:
            raise Exception("No question with this index")

        condition = tables_with_def[0]
        idx_table_def = all_tables_in_doc.index(condition)

        if idx_table_def < len(all_tables_in_doc) - 1:
            next_table = all_tables_in_doc[idx_table_def + 1]

            # check that it is multiply choice question
            if not (any(any(y in symbols for y in x.cells[1].text) for x in next_table.rows)):
                raise Exception("Not multiply choice question, no special symbols")
        else:
            raise Exception("Not multiply choice question")

        answer_sheet = all_tables_in_doc[idx_table_def + 1]

        self.question_name = condition.rows[0].cells[1].text

        self.question_text['format'] = 'text'
        self.question_text['text'] = condition.rows[0].cells[1].text
        self.question_id = str(condition.rows[0].cells[0].text).replace('.', '')

        points = ''.join([x for x in condition.rows[0].cells[2].text if x.isdigit()])

        # parsing answers
        num_correct = 0
        for row in answer_sheet.rows:
            cells = row.cells

            answer = MultiplyChoiceAnswer()
            # second column - right / not right
            # third column - answer
            answer.text['format'] = 'text'
            answer.text['text'] = cells[2].text
            if any(x == cells[1].text.strip() for x in correct_symbols):
                answer.is_correct = True
                num_correct += 1
            else:
                answer.is_correct = False
            self.options.append(answer)

        # Testmoz doesn't support points for partly correct answers, so point for each correct answer is $POINT_TASK / NUM_CORRECT$
        for option in self.options:
            option.points = int(points) / num_correct

        if num_correct != 1:
            self.is_single_answer = False
        else:
            self.is_single_answer = True

    def parse_one_question_canvas(self, question_info: dict):
        if self.is_correct(question_info['id']):
            self.question_id = question_info['id']

        if self.is_correct(question_info['quiz_id']):
            self.associated_quiz_id = question_info['quiz_id']

        if self.is_correct(question_info['assessment_question_id']):
            self.assessment_question_id = question_info['assessment_question_id']

        if self.is_correct(question_info['question_name']):
            self.question_name = question_info['question_name']

        if self.is_correct(question_info['question_text']):
            self.question_text['text'] = question_info['question_text']
            self.question_text['format'] = 'text'

        if self.is_correct(question_info['points_possible']):
            self.question_text['weight'] = question_info['points_possible']

        if self.is_correct(question_info['correct_comments']):
            self.corrected_feedback['text'] = question_info['correct_comments']
            self.corrected_feedback['format'] = 'text'

        if self.is_correct(question_info['correct_comments_html']):
            self.corrected_feedback['text'] = question_info['correct_comments_html']
            self.corrected_feedback['format'] = 'html'

        if self.is_correct(question_info['neutral_comments']):
            self.particular_corrected_feedback['text'] = question_info['neutral_comments']
            self.particular_corrected_feedback['format'] = 'text'

        if self.is_correct(question_info['neutral_comments_html']):
            self.particular_corrected_feedback['text'] = question_info['neutral_comments_html']
            self.particular_corrected_feedback['format'] = 'html'

        if self.is_correct(question_info['incorrect_comments']):
            self.incorrect_feedback['text'] = question_info['incorrect_comments']
            self.incorrect_feedback['format'] = 'text'

        if self.is_correct(question_info['incorrect_comments_html']):
            self.particular_corrected_feedback['text'] = question_info['incorrect_comments_html']
            self.particular_corrected_feedback['format'] = 'html'

        if self.is_correct(question_info['answers']):
            for answer in question_info['answers']:
                option = MultiplyChoiceAnswer()
                if self.is_correct(answer['id']):
                    option.id = answer['id']
                if self.is_correct(answer['text']):
                    option.text['text'] = answer['text']
                    option.text['format'] = 'text'
                if self.is_correct(answer['html']):
                    option.text['text'] = answer['html']
                    option.text['format'] = 'html'
                if self.is_correct(answer['comments']):
                    option.feedback['text'] = answer['comments']
                    option.feedback['format'] = 'text'
                if self.is_correct(answer['comments_html']):
                    option.feedback['text'] = answer['comments_html']
                    option.feedback['format'] = 'html'
                if self.is_correct(answer['weight']):
                    option.points = answer['weight']
                self.options.append(option)

