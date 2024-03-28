from django import forms
from .models import Product
from django.utils.translation import gettext_lazy as _

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['sku_id', 'product_name', 'price', 'count', 'image']

    def __init__(self, *args, **kwargs):
        self.language = kwargs.pop('language', None)
        super().__init__(*args, **kwargs)

        if self.language == 'hindi':
            self.fields['sku_id'].label = _('एसकेयू आईडी')
            self.fields['product_name'].label = _('उत्पाद का नाम')
            self.fields['price'].label = _('कीमत')
            self.fields['count'].label = _('गिनती')
            self.fields['image'].label = _('छवि')
        elif self.language == 'tamil':
            self.fields['sku_id'].label = _('எஸ்கியூ ஐடி')
            self.fields['product_name'].label = _('தயாரிப்பின் பெயர்')
            self.fields['price'].label = _('விலை')
            self.fields['count'].label = _('எண்ணிக்கை')
            self.fields['image'].label = _('படம்')
        elif self.language == 'marathi':
            self.fields['sku_id'].label = _('एसकेयू आयडी')
            self.fields['product_name'].label = _('उत्पादनाचे नाव')
            self.fields['price'].label = _('किंमत')
            self.fields['count'].label = _('मोजणी')
            self.fields['image'].label = _('प्रतिमा')





class InputForm(forms.Form):
    sku_id = forms.CharField(label='SKU ID', max_length=100)
    product_name = forms.CharField(label='Product Name', max_length=100)
    count = forms.IntegerField(label='Count')
    price = forms.DecimalField(label='Price', max_digits=10, decimal_places=2)
    image = forms.ImageField(label='Image')