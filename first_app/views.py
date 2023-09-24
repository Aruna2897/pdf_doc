
from django.http import HttpResponse
from django.template import loader


from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import UploadFileForm
from pdf2docx import Converter

def upload_pdf(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            pdf_path = uploaded_file.file.path
            docx_path = pdf_path.replace('.pdf', '.docx')

            # Convert PDF to DOCX
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()

            # Save the converted DOCX file
            uploaded_file.converted_file.name = docx_path.replace('media/', '')
            uploaded_file.save()


            return redirect('download', pk=uploaded_file.pk)
    else:
        form = UploadFileForm()
    return render(request, 'myfirst.html', {'form': form})

def download_converted(request, pk):
    uploaded_file = UploadedFile.objects.get(pk=pk)
    if uploaded_file.converted_file:
        docx_path = uploaded_file.converted_file.path
        with open(docx_path, 'rb') as docx_file:
            response = HttpResponse(docx_file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name.replace(".pdf", ".docx")}"'
            return response
    else:
        return HttpResponse("Conversion in progress or failed. Please try again later.")
