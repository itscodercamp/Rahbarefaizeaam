from django.db import models
from django.utils.text import slugify
from django.utils.html import format_html


# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True)
    # discription = RichTextField()
    discription = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    

    # Blog models here including blog slugs auto slugs

class Blog(models.Model):
    title = models.CharField(max_length=200)
    full_description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    slug = models.SlugField(unique=True, blank=True, editable=False)  # Auto-generated slug
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Auto-generate slug from the title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
# Become_volunteer form model

class Events(models.Model):
    event = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    
class Country(models.Model):
    country = models.CharField(max_length=250)
    def __str__(self):
        return self.country
    
class Volunteers(models.Model):
    name = models.CharField(max_length=150 ,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    number = models.IntegerField(blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Donation_form(models.Model):
    name = models.CharField(max_length=150 ,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    country = models.CharField(max_length=150,blank=True,null=True)
    amount = models.IntegerField()
    events = models.ForeignKey(Events,on_delete=models.CASCADE)
    message = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name+" - "+self.email+" - ",self.number
    
# contact form models here
class ContactUs(models.Model):
    name = models.CharField(max_length=150 ,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    number = models.IntegerField(blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name+"_"+self.email
    
    class Meta:
        verbose_name = "Contacts Us Form"
        verbose_name_plural = "Contacts Form"

# making dynamic SLider of home page

class HomeSilder(models.Model):
    Image = models.ImageField(upload_to='Sliders/')
    name = models.CharField(max_length=150 ,blank=True,null=True)
    Description = models.EmailField(blank=True,null=True)
    last_save_time = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    

class DonationForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.IntegerField()
    country = models.CharField(max_length=255)
    event = models.CharField(max_length=255)
    amount = models.IntegerField()
    custom_amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name