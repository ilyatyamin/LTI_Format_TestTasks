from django import forms
from scripts.conversion_formats import ConversionFormat as cf


class UserForm(forms.Form):
    choice = forms.ChoiceField(choices=
                               ((int(cf.MultipleChoiceMoodleXML), "MultipleChoice - Moodle XML"),
                                (int(cf.MultipleChoiceMoodleCSV), "MultipleChoice - Moodle CSV"),
                                (int(cf.MultipleChoiceMoodleWord), "MultipleChoice - Moodle Word"),
                                (int(cf.MultipleChoiceStepikStep), "MultipleChoice - Stepik Step"),
                                (int(cf.MultipleChoiceMoodleWord), "MultipleChoice - Testmoz Word")))
    choice.label = 'Выберите тип вопроса:'
    submit_your_file_here = forms.FileField()

    submit_your_file_here.label = 'Загрузите свой файл здесь'
    submit_your_file_here.allow_empty_file = True

    required_css_class = "forms_text"


class DownloadButton(forms.Form):
    pass
