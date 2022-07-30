import io
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter



from .models import Menu

# Create your views here.


def index(request):
    menus = Menu.objects.all()
    context = {
        'menus': menus,
        }
    return render(request, 'menu/index.html', context)


def generate_pdf(request):
    menus = Menu.objects.all()
    template_path = 'menu/pdf.html'
    context = {'menus': menus}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="menu.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response