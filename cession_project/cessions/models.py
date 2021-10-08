from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class Territory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.name

class Publishing_company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    territories = models.ManyToManyField(Territory, related_name='publishing_companies', blank=True)

    def __str__(self):
        return self.name

class Publisher_contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField( max_length=254)
    publishing_company = models.ForeignKey(Publishing_company, on_delete=models.CASCADE)
    def __str__(self):
        return self.last_name

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField( max_length=254)

    def __str__(self):
        return self.last_name

class Illustrator(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField( max_length=254)

    def __str__(self):
        return self.last_name

class Topic(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=300, unique=True)
    summary = models.CharField(max_length=1000)
    cover = models.URLField(max_length=500)
    published_at = models.DateTimeField(auto_now_add=False, null=True)
    number_pages = models.IntegerField(null=True)
    format = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='books', blank=True)
    illustrators = models.ManyToManyField(Illustrator, related_name='books', blank=True)
    topic = models.ManyToManyField(Topic, related_name='books', blank=True)
    publishing_company = models.ForeignKey(Publishing_company, on_delete=models.DO_NOTHING, null=True)
    collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.title

class Agency(models.Model):
    name = models.CharField(max_length=200, unique=True)
    territories = models.ManyToManyField(Territory, related_name='agencies', blank=True)

    def __str__(self):
        return self.name

class Agent(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField( max_length=254)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    def __str__(self):
        return self.last_name

class Royalties(models.Model):
    year = models.IntegerField(null=True)
    royalties_percent = models.IntegerField(null=True)
    paid = models.BooleanField(default=False)


class Cession(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True)
    publishing_company = models.ForeignKey(Publishing_company, on_delete=models.CASCADE, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    publisher_contact = models.ForeignKey(Publisher_contact, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=False, null=True)
    end_at = models.DateTimeField(auto_now_add=False, null=True)
    duration = models.IntegerField(null=True)
    pdf_sent_at = models.DateTimeField(auto_now_add=False, null=True)
    contract_sent_at = models.DateTimeField(auto_now_add=False, null=True)
    contract_signed_at = models.DateTimeField(auto_now_add=False, null=True)
    bill_sent_at = models.DateTimeField(auto_now_add=False, null=True)
    book_sent_at =  models.DateTimeField(auto_now_add=False, null=True)
    advance_price = models.IntegerField(null=True)
    advance_price_paid_at =  models.DateTimeField(auto_now_add=False, null=True)
    data_price = models.IntegerField(null=True)
    data_price_paid_at =  models.DateTimeField(auto_now_add=False, null=True)
    files_sent_at =  models.DateTimeField(auto_now_add=False, null=True)
    model_received_at =  models.DateTimeField(auto_now_add=False, null=True)
    territories =  models.ManyToManyField(Territory, related_name='cessions', blank=True)
    royalties = models.ManyToManyField(Royalties, related_name='cessions', blank=True)
    language = models.CharField(max_length=200, null=True)
    occasion = models.CharField(max_length=200, null=True)
    comment = models.CharField(max_length=200, null=True)
    completed = models.BooleanField(default=False)
    dropped = models.BooleanField(default=False)
    def __str__(self):
        return self.book.title