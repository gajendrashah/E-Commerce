from datetime import datetime
from django.core.mail import EmailMessage
from django.http import HttpResponse
import json
from django.conf import settings
from django.core.mail import send_mail

from .cart import Cart
from django.db.models import Q
from django.shortcuts import render,redirect
from .models import Banner, Brand, Color, Customers, Events, Orders, ProductImage, catagory, Slider,Product
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .whishlist import Whishlist
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

def index(request):
    cat = catagory.objects.all()[:9] #for the header_menu
    products = Product.objects.all()
    pro = products[:10]
    evt = Events.objects.all()
    sli = evt.get(event_name="slider demo").slider.all()
   
    top_banner = Banner.objects.filter(title="banner3")
    print(top_banner)

        
   
        
    
    
    on_sale = []
    Featured =[]
    Top_selling =[]
    for product in products:
        print(str(product.product_collection))
        if "Featured" in str(product.product_collection):
            print("here ")
            Featured.append(product)


        elif "On sale" in str(product.product_collection):
            on_sale.append(product)

        elif "Top selling" in str(product.product_collection):
            Top_selling.append(product)
    print(Featured)
    sale_product = products.filter(pro_collection="On sale").order_by("-updated_at")[:2]
  


        
    offer_product = products.filter(pro_collection="Deals").latest("updated_at")
    time_now =  datetime.today().timestamp()
    start_time = datetime.strptime(str(offer_product.updated_at),"%Y-%m-%d %H:%M:%S.%f").timestamp()
    # print(start_time)
    of_time =  start_time - time_now
   
    
    
    
   

    context={"catagory":cat,"slider":sli,"product":on_sale,"Featured":Featured,
    "top_banner":top_banner,
    "product":pro,"offer_product": offer_product,"sale_product":sale_product,
    "onsale":on_sale,"Topselling":Top_selling,"hr":int(of_time)}

    return render(request,"userapp/index.html",context)

def category_page(request,cat_slug):
    product = Product.objects.filter(pro_catagory__slug=cat_slug)
    context={"products":product,"slug":cat_slug,}
    return render(request,"userapp/category_page.html",context)


def quickview(request,pk):
    # prod = Product.objects.get(id=pk)
    prod = get_object_or_404(Product,id=pk)
    

    pro = prod.product.all()
    varients = prod.varients.all()
    
   
    context={"product":prod,"image":pro,"varients":varients}
    return render(request,"userapp/quickView.html",context)


def wishlist_add(request, id):
    wishlist = Whishlist(request)
    product = Product.objects.get(id=id)
    wishlist.add(product=product)
    return redirect("index")

def wishlist_item_clear(request, id):
    wishlist = Whishlist(request)
    product = Product.objects.get(id=id)
    wishlist.remove(product)
    return redirect("wishlist_detail")

def wishlist_detail(request):
    return render(request,"userapp/wishlist.html")


@csrf_exempt
def shop_page(request):
 
      
    
    cat = catagory.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()
    all_products = Product.objects.all().order_by("-updated_at")

    page_num = request.GET.get('page', 1)
    paginator = Paginator(all_products, 12)
    
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {"products":page_obj,"catagory":cat,"brands":brands,"colors":colors}
    return render(request,"userapp/shop.html",context)




def search_result(request):
    query =request.GET.get("term")
    result = []
    obj = Product.objects.filter(pro_name__icontains=query)
    for res in obj:
        
        result.append(res.id)
        result.append(res.pro_name)
    
    
    return JsonResponse(list(result),safe=False)


@csrf_exempt
def filter_result(request):
    product = []
    if request.method == "POST":
        minimum_price = int(request.POST.get("minimum_price").replace("Rs.",""))
        maximum_price = int(request.POST.get("maximum_price").replace("Rs.",""))
        brand = request.POST.getlist("brand[]")
        category = request.POST.getlist("category[]")
        color = request.POST.getlist("colors[]")

        if brand != [] or category != [] or color !=[]:
            from_price = set(Product.objects.filter(Q(pro_brnd__brantitem__in=brand) |
                Q(pro_catagory__catagoryname__in=category) |
                Q(color__color_name__in=color) |
                Q(price__range=(minimum_price,maximum_price))))


            # print(len(set(from_price)))

            for pro in from_price:
                proimg = ProductImage.objects.filter(product__id=pro.id)
                a =[pro.id,pro.pro_name,pro.price,str(pro.get_absolute_image_url),
                
                    pro.rate_product,str(pro.pro_catagory),
                    
                    
                ] 
                proImg = []
                for img in proimg:
                    c = (str(img.get_absolute_image_url))
                    proImg.append(c)
                
                a.append(proImg)
                     
                product.append(a)


        # print(brand,category,color)
    return JsonResponse(product,safe=False)



def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return JsonResponse({"message": len(request.session['cart'])})


def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@csrf_exempt
def item_increment(request, id):
    if request.method != "POST" :
        return JsonResponse("Cant acess ",safe=False)

    qty = json.loads(request.body)
    qty=qty.get("produc_qty")
    cart = Cart(request)
   
    product = Product.objects.get(id=id)
    cart.add(product=product,quantity=qty)

    new_item = request.session["cart"].get(str(id))
    total_price = int(new_item["price"])*int(new_item["quantity"])

    return JsonResponse({"total_price":total_price},safe=False)

@csrf_exempt
def item_decrement(request, id):
    if request.method != "POST" :
        return JsonResponse("Cant acess ",safe=False)
    qty = json.loads(request.body)
    qty=qty.get("produc_qty")
    cart = Cart(request)

    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    
    new_item = request.session["cart"].get(str(id))
    total_price = int(new_item["price"])*int(new_item["quantity"])


    return JsonResponse({"total_price":total_price},safe=False)


def cart_clear(request):
    
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request):
   

    return render(request, 'userapp/cart_detail.html')


@login_required(login_url="account_login")
@csrf_exempt
def place_order(request):
    if request.method =="POST":
        data = json.loads(request.body)
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        company_name = data.get("company_name")
        country = data.get("country")
        address1 = data.get("address1")
        address2= data.get("address2")
        city = data.get("city")
        state = data.get("state")
        postcode = data.get("postcode")
        phonenumber =data.get("phonenumber")
        email = data.get("email")
        note = data.get("notes")

        cart  = request.session["cart"]
        user = cart.get("userid")
        
        if user is None:
            obj =  Customers.objects.create(user =request.user,first_name = first_name,last_name=last_name,email=email,address1=address1,address2=address2,city=city,zip_code= postcode,country=country,nearest_location =state,note=note,
               contact=phonenumber ) 
            obj.save()
            for key,value in cart.items():
                product_id = (value['product_id'])
                prodct_qty = float((value['quantity']))
                product_price = float(value['price'])        
                total_ammount = prodct_qty * product_price
                x = Orders.objects.create(order_by= request.user,order_product_id=product_id,total_amount=total_ammount)
                x.save()
            subject = 'welcome to GFG world'
            message = f'Hi {first_name + last_name}, thank you for purchase the product.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )


        
       
        return JsonResponse("this is me ",safe=False)
    return render(request, "userapp/checkout.html")




def wat_on_sale(request):
    return HttpResponse("<h1> Site will lunching soon </h1>")


def how_to_order(request):
    return HttpResponse("<h2> Site will lunching soon </h2>")


def faqs(request):
    return HttpResponse("<h2> Site will lunching soon </h2>")