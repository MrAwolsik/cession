from typing import ContextManager
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator


from .models import Author, Publishing_company, Book, Agency, Agent, Cession

# Create your views here.

def index(request):
    Cessions = Cession.objects.filter()[:20]
    template = loader.get_template('cessions/index.html')

    Context = {
        'cessions': Cessions,
    }

    return HttpResponse(template.render(Context, request=request))

def listing(request):
    books = Book.objects.filter()
    formatted_albums = ["<li>{}</li>".format(book.title) for book in books]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    return HttpResponse(message)

def detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    author_first_name = book.author.first_name
    author_last_name = book.author.last_name
    message = "Le nom du livre est {}. Il a été écrit par {} {}".format(book.title, author_first_name, author_last_name) 
    return HttpResponse(message)

def search(request):
    query = request.GET.get('query')
    if not query:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(title__icontains=query)

        if not books.exists():
            books = Book.objects.filter(authors__first_name__icontains=query)
        
        if not books.exists():
            message = "Aucun Resultat"
        else:
            books = ["<li>{}</li>".format(book.title) for book in books]
            message = """
                Nous avons trouvé les livres correspondant à votre recherche ! Les voici :
                <ul>
                    {}
                </ul>
            """.format("</li><li>".join(books))
    return HttpResponse(message)
