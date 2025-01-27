from django.shortcuts import render
from django.http import JsonResponse
import subprocess


# Create your views here.
def editor_view(request):
    return render(request, 'editor/editor.html')


def execute_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')

        try:
            result = subprocess.run(['python', '-c', code], capture_output=True, text=True, check=True)
            output = result.stdout
        except subprocess.CalledProcessError as e:
            output = e.stderr

        return JsonResponse({'output': output})

    return render(request, 'editor/editor.html')
