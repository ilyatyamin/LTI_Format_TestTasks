from django import forms
from scripts.toLTI.conversion_formats import ConversionFormat as cf


class UserLoadedFileForm(forms.Form):
    choice = forms.ChoiceField(choices=
                               ((int(cf.MultipleChoiceMoodleXML), "MultipleChoice - Moodle XML"),
                                (int(cf.MultipleChoiceMoodleCSV), "MultipleChoice - Moodle CSV"),
                                (int(cf.MultipleChoiceMoodleWord), "MultipleChoice - Moodle Word"),
                                (int(cf.MultipleChoiceStepikStep), "MultipleChoice - Stepik Step"),
                                (int(cf.MultipleChoiceMoodleWord), "MultipleChoice - Testmoz Word")))
    choice.label = 'Выберите тип загружаемого вопроса:'
    submit_your_file_here = forms.FileField()

    submit_your_file_here.label = 'Загрузите свой файл здесь'
    submit_your_file_here.allow_empty_file = True

    choice_to = forms.ChoiceField(choices=
    (
        (int(cf.LTI), "LTI"),
        (int(cf.MultipleChoiceMoodleXML), "Moodle XML"),
        (int(cf.MultipleChoiceMoodleCSV), "Moodle CSV"),
        (int(cf.MultipleChoiceMoodleWord), "Moodle Word"),
        (int(cf.MultipleChoiceStepikStep), "Stepik Step"),
        (int(cf.MultipleChoiceMoodleWord), "Testmoz Word")))
    choice_to.label = 'Выберите во что преобразовать:'

    required_css_class = "forms_text"


class DownloadButton(forms.Form):
    pass
