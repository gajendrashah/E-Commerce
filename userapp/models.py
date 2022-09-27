from statistics import mode
from colorfield.fields import ColorField
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
class catagory(models.Model):
    catagoryname = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True,blank=True,null=True)
    icon = models.TextField(max_length=255,blank=True)

    def __str__(self):
        return self.catagoryname
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.catagoryname)
        super(catagory, self).save(*args, **kwargs)

class Brand(models.Model):
    brantitem = models.CharField(max_length=50)
    def __str__(self):
        return self.brantitem

class Product_type(models.Model):
    product_type = models.CharField( max_length=100)
    def __str__(self):
        return self.product_type

class Color(models.Model):
    color_name = models.CharField(max_length=255,blank=True)
    color_code= ColorField(default='#FF0000')
    def __str__(self) -> str:
        return self.color_name

class Tags(models.Model):
    tag_name = models.CharField(max_length=255,blank=True)

    def __str__(self) -> str:
        return self.tag_name

class metadata(models.Model):
    field = models.CharField( max_length=50)
    value = models.CharField( max_length=50)
    def __str__(self):
        return self.field

class Slider(models.Model):
    title = models.CharField(max_length=255,blank=True)
    desc = models.CharField(max_length=500,blank=True)
    image = models.ImageField(upload_to="slider/")
    offerd_price = models.IntegerField()
    original_price = models.IntegerField()
    

    def __str__(self):
        return self.title




class Events(models.Model):
    slider = models.ManyToManyField(Slider,blank=True)
    # banner = models.ManyToManyField(Banner,blank=True)
    event_name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    slug = models.SlugField(blank=True,unique=True)

        
    def __str__(self):
        return self.event_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.event_name)
        super(Events, self).save(*args, **kwargs)
    


class Product(models.Model):

    COLLECTION_TYPE= (
    ("Featured","Featured"),
    ("On sale","On sale"),
    ("Top selling","Top selling"),
    ("Deals","Deals"),
    ("Clearance","Clearance")
    )
    
    
    pro_name = models.CharField(max_length=200)
    Pro_desc = models.CharField( max_length=50)
    rate_product = models.IntegerField()
    pro_catagory = models.ForeignKey(catagory, on_delete=models.CASCADE)
    pro_brnd = models.ForeignKey(Brand, on_delete=models.CASCADE)
    pro_collection = models.CharField(max_length=100, choices=COLLECTION_TYPE,blank=True)
    tags = models.ManyToManyField(Tags,blank=True)
    color  = models.ManyToManyField(Color,blank=True)
    product_type = models.ManyToManyField(Product_type,blank=True,related_name="product_types")
    price = models.IntegerField()
    old_price = models.IntegerField(blank=True,null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    main_image = models.ImageField(upload_to="product_main_image")
    offer_start = models.DateTimeField(blank=True,auto_now=True,null=True)
    offer_end = models.DateTimeField(blank=True,auto_now=True,null=True)
    discount = models.IntegerField(blank=True,null=True)
    events = models.ForeignKey(Events,null=True,blank=True,on_delete=models.CASCADE,related_name="events")

    def __str__(self):
        return self.pro_name


    

    # def save(self,*args, **kwargs):
    #     initial_price  = self.price
        
    #     if initial_price ==  self.price:
    #        final_price = initial_price
    #        if final_price != self.price:
    #         self.old_price = final_price
    #         super(Product, self).save(*args,**kwargs)

    @property
    def product_rate(self):
        return (self.rate_product/5)*100

    

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.main_image)
    

    @property
    def product_collection(self):
        return self.pro_collection          


class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="banner/",blank=True,null=True)
    desc = models.CharField(max_length=255,blank=True,null=True)
    product = models.ManyToManyField(Product,blank=True,related_name="pros")
    def __str__(self) -> str:
        return self.title






class ProductImage(models.Model):
    product = models.ForeignKey(Product,default=None,on_delete=models.CASCADE,related_name='product')
    proimg = models.ImageField(upload_to="product_image/")
    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.proimg)



class seo(models.Model):
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    seo_title = models.CharField( max_length=150)
    seo_description =  models.CharField( max_length=150)
    meta_data = models.ForeignKey(metadata, on_delete=models.CASCADE)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.slug

class giftcard(models.Model):
    cardname = models.CharField( max_length=150)
    cardimage = models.ImageField(upload_to="giftcard")
    cardamount = models.IntegerField()
    def __str__(self):
        return self.cardname

class Customers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField( max_length=150)
    last_name = models.CharField( max_length=150)
    email = models.EmailField( max_length=254)
    contact = models.IntegerField()
    address1 = models.CharField( max_length=150)
    address2 = models.CharField( max_length=150)
    city = models.CharField( max_length=150)
    zip_code = models.CharField(max_length=255)
    country = models.CharField( max_length=150)
    nearest_location = models.CharField( max_length=150)
    note = models.CharField( max_length=150)
    def __str__(self):
        return self.first_name

class Orders(models.Model):
    PAYMENTTYPE = (('PAID', 'PAID'), ('UNPAID', 'UNPAID'))
    PRODUCTDELIVARY = (('NEW', 'NEW'), ('APPROVED', 'APPROVED'),('CANCLE','CANCLE'),('DISPATCHED','DISPATCHED'),('RECIVED','RECIVED'))
    order_date = models.DateTimeField(auto_now=True)
    order_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="users")
    order_product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    payment = models.CharField(max_length=100, null=True, choices=PAYMENTTYPE,default="UNPAID")
    total_amount = models.FloatField()
    delivart_status = models.CharField(max_length=100, null=True, choices=PRODUCTDELIVARY,default="NEW")
    def __str__(self):
        return self.order_by.username


    

class Size(models.Model):
    size_name= models.CharField(max_length=255,blank=True)
    def __str__(self) -> str:
        return self.size_name

class Variants(models.Model):
    title = models.CharField(max_length=100, blank=True,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="varients")
    color = models.ForeignKey(Color, on_delete=models.CASCADE,blank=True,null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE,blank=True,null=True)
    image_id = models.IntegerField(blank=True,null=True,default=0)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2,default=0)