# pip install python-docx

import json
import xml.etree.ElementTree as ET
from docx import Document
from CourseWork.MultiplyChoice.MultiplyChoiceAnswer import MultiplyChoiceAnswer


class MultiplyChoiceQuestion:
    """
    Class that introduced answer with one or multiply choice answer
    """
    def __init__(self):
        # Obligatory fields
        self.question_id = None  #
        self.question_name = None  #
        self.question_text: dict = {}
        self.is_single_answer = None
        self.text_style = None
        self.options: list = []
        self.is_needed_feedback = None
        self.is_always_correct = False

        # Optional fields. Depends on the platform
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
        self.subtitle_files = None
        self.is_deprecated = None
        self.has_review = None
        self.preserve_order = None
        self.output_format = None
        self.general_feedback: dict = {}  #
        self.course_id = None
        self.tags: list = []
        self.prompts: list = []

    def __strip_file(self, path_to_file: str):
        lines = []
        with open(path_to_file, 'r+') as file:
            for line in file:
                if not line.isspace():
                    lines.append(line)
        with open(path_to_file, 'r+') as file:
            for line in lines:
                file.write(line)
            file.truncate()
            file.close()

    def __encoder(self, dictionary: dict):
        values_to_delete = []
        for item, value in dictionary.items():
            if value is None:
                values_to_delete.append(item)
        for value in values_to_delete:
            dictionary.pop(value)
        return dictionary

    def __open_file(self, path: str) -> list[str]:
        with open(path, encoding='utf8') as file:
            return file.readlines()

    def parseOneQuestionFromMoodleXML(self, path_to_file: str):
        self.__strip_file(path_to_file)

        parsed_file = ET.parse(path_to_file).getroot()
        file_as_txt = open(path_to_file).readlines()

        if parsed_file.tag != 'question' or parsed_file.attrib['type'] != 'multichoice':
            raise Exception("Not Multiply Choice Question.")

        self.question_name = parsed_file.find("name").find("text").text

        # Parsing question id (if file contains it)
        if any("<!-- question:" in x for x in file_as_txt):
            line_with_num = None
            for line in file_as_txt:
                if "<!-- question:" in line:
                    line_with_num = line
                    break
            self.question_id = "".join([x for x in line_with_num if x.isdigit()])
        else:
            self.question_id = "0"

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

    def parseOneQuestionMoodleCSV(self, file_name: str, idx: int = 1):
        """
        Parse one question using Moodle CSV format
        Obligatory requirement is headers in first row
        If they are not saved in first row, method throws an exception
        """
        lines = [x.split(',') for x in self.__open_file(file_name) if not (x.isspace())]

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

    def parseOneQuestionMoodleDocx(self, path_to_word: str, idx=0):
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

        doc = Document(path_to_word)
        tables_in_doc = doc.tables
        need_table = tables_in_doc[idx]

        # self.question_name - NEED TO DO

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
            if option.points != 0:
                option.is_correct = "1"
            else:
                option.is_correct = "0"
            self.options.append(option)

        for ind in range(end_of_answers, len(need_table.rows) - 1):
            name = ''.join([x for x in need_table.rows[ind].cells[1].text if not(x.isdigit())])
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


    def saveToFormat(self, file_name: str):
        with open(file_name, 'w', encoding='utf-8') as f:
            # Serialize the data and write it to the file
            json.dump(self, f, default=lambda o: self.__encoder(o.__dict__), ensure_ascii=False)
