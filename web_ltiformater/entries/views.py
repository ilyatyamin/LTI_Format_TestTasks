from django.http import HttpResponse
from django.shortcuts import render

from entries.forms import UserLoadedFileForm
from django.core.files.storage import FileSystemStorage
from web_ltiformater import wsgi, settings


def mainpage(request):
    if request.method == 'POST':
        return postuser(request)
    return render(request, "index.html", {"form": UserLoadedFileForm()})


def postuser(request):
    fs = FileSystemStorage()
    form = UserLoadedFileForm(request.POST, request.FILES)
    type_of_param = int(request.POST.get('choice', 'undefined'))
    type_to = int(request.POST.get('choice_to', 'undefined'))
    try:
        if form.is_valid():
            file = request.FILES['submit_your_file_here']

            filename = fs.save(f"logs/{file.name}", file)
            uploaded_file_path = fs.path(filename)

            question = wsgi.manager.process_question(uploaded_file_path, type_of_param, type_to)
            settings.LATEST_FILE = uploaded_file_path
            wsgi.manager.write_to_file(settings.LATEST_FILE, question)
            return render(request, "result.html",
                          {"answer": wsgi.manager.get_text(question)})

    except Exception as err:
        return render(request, "result.html",
                          {"answer": err, "download_path" : "/"})
    return HttpResponse('none!')


def download_file(request):
    file_path = settings.LATEST_FILE

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="downloaded_file.json"'
        return response

