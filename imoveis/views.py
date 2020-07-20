from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse,request, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from django.utils.html import strip_tags
from django.views.generic import CreateView
from .models import Imoveis,ImoveisImage, TIPOS_CHOICES
from .forms import ImoveisForm, SearchForm
from djangoProject import settings
from .filters import ImoveisFilter, ImoveisFilterAlt
from django.db.models import Q

def is_valid_queryparam(param):
    return param != '' and param is not None

def imoveis_index(request):
    #ordenar os posts
    imoveis = Imoveis.objects.all().order_by('date')
    form = SearchForm
    getDic = {}

    if 'term' in request.GET:
        term = request.GET.get('term')
        query = Imoveis.objects.filter(Q(nome__icontains=term) | Q(endereco__icontains=term))

        imoveisList = []
        for imovel in query:
            imoveisList.append(imovel.nome)
            imoveisList.append(imovel.endereco)

        imoveisJson = JsonResponse(imoveisList, safe=False)

        return imoveisJson

    if 'Search' in request.GET:
        tipo = request.GET.get('Tipo')
        search = request.GET.get('Search')
        quartos = request.GET.get('Quartos')
        suites = request.GET.get('Suites')
        banheiros = request.GET.get('Banheiros')
        vagas = request.GET.get('Vagas')

        if is_valid_queryparam(tipo):
            if tipo != 'Todos':
                imoveis = imoveis.filter(tipo__icontains=tipo)
            getDic['Tipo'] = tipo    

        if is_valid_queryparam(search):
            imoveis = imoveis.filter(Q(nome__icontains=search) | Q(endereco__icontains=search))
            getDic['Search'] = search    

        if is_valid_queryparam(quartos):
            imoveis = imoveis.filter(quartos__iexact=quartos)
            getDic['Quartos'] = quartos    

        if is_valid_queryparam(suites):
            imoveis = imoveis.filter(suites__iexact=suites)
            getDic['Suites'] = suites    

        if is_valid_queryparam(banheiros):
            imoveis = imoveis.filter(banheiros__iexact=banheiros)
            getDic['Banheiros'] = banheiros    

        if is_valid_queryparam(vagas):
            imoveis = imoveis.filter(vagas__iexact=vagas)
            getDic['Vagas'] = vagas    

    #organiza os imóveis em páginas
    paginator = Paginator(imoveis, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    #renderizar a pagina html para o browser
    return render(request,"imoveis/imoveis_index.html",{'imoveis':imoveis, 'page_obj': page_obj, 'form': form, 'getDic': getDic})

def imoveis_details(request,slug):
    imovel = Imoveis.objects.get(slug=slug)
    images = ImoveisImage.objects.filter(imovel=imovel)
    form = ImoveisForm()

    if request.method == "POST": 
        msgNome = request.POST['Nome']
        msgEmail = request.POST['Email']
        msgCelular = request.POST['Telefone']
        msgComentarios = request.POST['Comentarios']
        msgContato = request.POST['Contato']
        template_email = settings.BASE_DIR + "/templates/imovel_email.html"
        msgDic ={'Nome': msgNome, 'Email': msgEmail, 'Celular': msgCelular, 'Comentarios': msgComentarios, 'Contato': msgContato,'Imovel': imovel.nome}

        mensagemEmail = render_to_string(template_email, { 'msgDic': msgDic, })

        send_mail(
            f"{msgNome} - {imovel.nome}",
            strip_tags(mensagemEmail), 
            msgEmail,
            ['winckdeveloper@gmail.com'],
            html_message=mensagemEmail,
            fail_silently=False,
        )

    
    else:
        msgDic ={'Nome': '', 'Email': '', 'Celular': '', 'Comentarios': '', 'Imovel': ''}

    return render(request,'imoveis/imoveis_details.html',{'imovel':imovel,'images':images, 'form':form, 'msgDic': msgDic})
