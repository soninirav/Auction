from django.forms import ModelForm,Textarea
from .models import Listing,Comment,Bid

from django import forms

class ListingForm(ModelForm):
    
    class Meta:
        model = Listing
        fields = ['title','description','starting_bid','image_url','category']
        labels={
            'title':'Title',
            'description':'Description',
            'starting_bid':'Starting Bid',
            'image_url':'Image URL',
            'category':'Category'
        }
        widgets={
            'description':Textarea(attrs={'style':'height:50px; width:400px;'})
            
        }
    
class CommentForm(ModelForm):
    
    class Meta:
        model=Comment
        fields=['message']
       
       
class BidForm(ModelForm):
    class Meta:
        model=Bid
        fields=['offer_price']
