from django.http import HttpResponse
from django.shortcuts import render

from entries.forms import UserLoadedFileForm
from django.core.files.storage import FileSystemStorage

from scripts.toLTI.conversion_formats import ConversionFormat
from web_ltiformater import wsgi, settings


def mainpage(request):
    if request.method == 'POST':
        return send_form_postrequest(request)
    return render(request, "index.html", {"form": UserLoadedFileForm()})


def reload_page(request):
    pass


def send_form_postrequest(request):
    # Getting access to the file system storage
    fs = FileSystemStorage()
    form = UserLoadedFileForm(request.POST, request.FILES)

    # Getting params that user are post to the server
    type_of_param = int(request.POST.get('choice', 'undefined'))
    type_to = int(request.POST.get('choice_to', 'undefined'))
    try:
        # Check that form is valid
        if form.is_valid():
            # There are two main classes of formats: that are loaded by file and that are loaded by API.
            # Now only supported Canvas, but in feature it can be realized as list of formats of one class and another
            if type_of_param != int(ConversionFormat.CanvasInstructure):
                # Getting loaded file
                file = request.FILES['submit_your_file_here']
                # Save in local host for next processing
                filename = fs.save(f"logs/{file.name}", file)
                uploaded_file_path = fs.path(filename)

                # Process question
                question = wsgi.manager.process_file_based_question(uploaded_file_path, type_of_param, type_to)

                # Write to the file. In the future, user can save it by pressing button
                if type_to == int(ConversionFormat.MultipleChoiceStepikStep) and isinstance(question, list):
                    wsgi.manager.write_to_archive(make_an_new_file(settings.LATEST_FILE, 'zip'), question,
                                                  wsgi.manager.get_format(type_to))
                else:
                    wsgi.manager.write_to_file(make_an_new_file(settings.LATEST_FILE, wsgi.manager.get_format(type_to)),
                                               question)
            else:
                # This is the questions with API processing
                # So, we need to get course_id and quiz_id from the form.
                course_id = int(request.POST.get('course_id', 'undefined'))
                quiz_id = int(request.POST.get('quiz_id', 'undefined'))

                # Process question
                question = wsgi.manager.process_request_based_question(course_id, quiz_id, type_of_param, type_to)

                # Write to the file. In the future, user can save it by pressing button
                settings.LATEST_FILE = make_an_new_file(settings.LATEST_FILE, wsgi.manager.get_format(type_to))
                wsgi.manager.write_to_file(settings.LATEST_FILE, question)
            return render(request, "result.html",
                          {"answer": wsgi.manager.get_text(question)})

    except Exception as err:
        return render(request, "result.html",
                      {"answer": err, "download_path": "/"})
    return HttpResponse('none!')


def make_an_new_file(directory: str, downl_format: str):
    """
    Creates new file in the directory.
    """
    folder = directory[:(directory.rfind('/') + 1)] + f'file.{downl_format}'
    settings.LATEST_FILE = folder
    return folder


def download_file(request):
    """
    Push file to the browser request and offer user to save it in local computer.
    """
    file_path = settings.LATEST_FILE

    type_of = file_path[(file_path.rfind('.') + 1):]

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/json')
        response['Content-Disposition'] = f'attachment; filename="result.{type_of}"'
        return response
