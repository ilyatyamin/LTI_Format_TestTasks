from django import forms
from scripts.toLTI.conversion_formats import ConversionFormat as cf


class UserLoadedFileForm(forms.Form):
    choice = forms.ChoiceField(choices=
                               ((int(cf.MultipleChoiceMoodleXML), "MultipleChoice - Moodle XML"),
                                (int(cf.MultipleChoiceMoodleCSV), "MultipleChoice - Moodle CSV"),
                                (int(cf.MultipleChoiceMoodleWord), "MultipleChoice - Moodle Word"),
                                (int(cf.MultipleChoiceStepikStep), "MultipleChoice - Stepik Step"),
                                (int(cf.MultipleChoiceMoodleWord), "MultipleChoice - Testmoz Word"),
                                (int(cf.CanvasInstructure), "Canvas Instructure (via API)")))
    choice.label = 'Выберите тип загружаемого вопроса:'
    choice.help_text = 'При выборе Canvas, убедитесь, что в Ваш курс добавлен аккаунт с почтой ltiformmatters@gmail.com как администратор.'
    submit_your_file_here = forms.FileField()

    submit_your_file_here.label = 'Загрузите свой файл здесь'
    submit_your_file_here.allow_empty_file = True
    submit_your_file_here.required = False

    course_id = forms.IntegerField()
    course_id.label = 'ID курса в Canvas: '
    course_id.required = False

    quiz_id = forms.IntegerField()
    quiz_id.label = 'ID квиза в Canvas: '
    quiz_id.required = False

    choice_to = forms.ChoiceField(choices=
    (
        (int(cf.LTI), "LTI"),
        (int(cf.MultipleChoiceMoodleXML), "Moodle XML"),
        (int(cf.MultipleChoiceStepikStep), "Stepik Step"),
        (int(cf.CanvasInstructure), "Canvas Instructure")))
    choice_to.label = 'Выберите во что преобразовать:'

    required_css_class = "forms_text"


class DownloadButton(forms.Form):
    pass
