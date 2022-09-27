

from django import forms

from userapp.models import Orders, Product




class ProductCreationForm(forms.ModelForm):
    # extra_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    
        # self.fields['pro_name'].widget = forms.TextInput()

    class Meta:
        model = Product
        fields= "__all__"
        # include= ["extra_image"]
        exclude= ['id','created_at',"updated_at"]


        widgets = {
            'pro_name':forms.TextInput(attrs={'class':'form-control form-control-line'}),
            'Pro_desc':forms.TextInput(attrs={'class':'form-control form-control-line'}),
            'rate_product':forms.NumberInput(attrs={'class':'form-control form-control-line'}),
            'pro_catagory':forms.Select(attrs={'class':'form-control form-select'}),
            'pro_brnd':forms.Select(attrs={'class':'form-select form-select'}),
            'pro_collection':forms.Select(attrs={'class':'form-control form-select',}),
            'tags':forms.SelectMultiple(attrs={'class':'form-select form-select choices-multiple-remove-button'}),
            'color':forms.SelectMultiple(attrs={'class':'form-control form-control-line choices-multiple-remove-button'}),
            'product_type':forms.SelectMultiple(attrs={'class':'form-control multiselect choices-multiple-remove-button'}),
            'price':forms.NumberInput(attrs={'class':'form-control form-control-line'}),
            'old_price':forms.NumberInput(attrs={'class':'form-control form-select'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control form-select'}),
            # # 'main_image':forms.FileInput(),
            'events':forms.Select(attrs={'class':'form-control form-control-line'}),
            'discount':forms.NumberInput(attrs={'class':'form-control form-control-line'}),
            
        }
        
  
    
class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields= "__all__"
        exclude = ["id"]

        widgets={
        'order_date':forms.DateTimeInput(attrs={'class':'form-control'}),
        'order_by':forms.Select(attrs={'class':'form-control'}),
        'order_product':forms.Select(attrs={'class':'form-control'}),
        'payment':forms.Select(attrs={'class':'form-control'}),
        'total_amount':forms.NumberInput(attrs={'class':'form-control'}),
        'delivart_status':forms.Select(attrs={'class':'form-control mb-5'}),

        }