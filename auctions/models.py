from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class User(AbstractUser):
    pass

class Category(models.Model):
    category=models.CharField(max_length=50)
    
    def __str__(self):
        return self.category
    

class Listing(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField()
    starting_bid=models.IntegerField()
    image_url=models.CharField(max_length=10000,blank=True)
    category=models.ForeignKey(Category,blank=True,on_delete=models.CASCADE)
    closed=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now=True)
    watchlist_users = models.ManyToManyField(User, blank=True, related_name="watchlist_items")
    winner=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return f"(Owner : {self.owner} , Title : {self.title} , Price : {self.starting_bid}, category: {self.category})"

    
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.CharField(max_length=1000)
    listing=models.ForeignKey(Listing,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} :--> {self.message} "

class Bid(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    offer_price=models.IntegerField()
    listing=models.ForeignKey(Listing,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.offer_price} - {self.listing.title} "
    
    
    