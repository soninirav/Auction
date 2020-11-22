from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User,Listing,Comment,Bid,Category
from .forms import ListingForm,CommentForm,BidForm


def index(request):
    al=Listing.objects.all().exclude(closed=True)
    context={
        'active_listings':al
    }
    return render(request,'auctions/index.html',context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    form = ListingForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            listing=form.save(commit=False)
            listing.owner=request.user
            listing.save()
            message="Listing Successful"
            return HttpResponseRedirect(reverse('index'))

    return render(request,'auctions/create_listing.html',{
        'listing_form':form
    })


def detail(request,listing_id):
    data=Listing.objects.all().filter(id=listing_id).values()[0] 
    comments=Comment.objects.all().filter(listing=listing_id)
    form=CommentForm(request.POST)
    bidform=BidForm(request.POST)
    # a=Listing.objects.get(id=listing_id)
    # a.closed=True
    # a.save()
    is_owner=Listing.objects.get(id=listing_id).owner
    is_closed=Listing.objects.get(id=listing_id).closed

    message=False
    item_in_watchlist=False
    alert_color='danger'
    try:
        listing_for_watchlist=Listing.objects.get(id=listing_id)
        user_for_watchlist=User.objects.get(id=request.user.id)
        print(user_for_watchlist.watchlist_items.get(id=listing_id))
        item_in_watchlist=True
    except:
        pass
    
    if request.method=="POST":
        if form.is_valid():
            ls=form.save(commit=False)
            ls.user=request.user
            ls.listing=Listing.objects.get(id=listing_id)
            ls.save()
            return HttpResponseRedirect(reverse("detail_listing",args=(listing_id,)))
        if bidform.is_valid():
            offer_price=int(request.POST['offer_price'])
            listing_price=Listing.objects.values().filter(id=listing_id)[0]['starting_bid']
            if offer_price<=listing_price:
                message="Please Make Sure Bid Price is Greater than Starting Bid"
            else:
                l=Listing.objects.get(id=listing_id)
                l.starting_bid=offer_price
                l.save()
                obj=Listing.objects.get(id=listing_id)
                obj.winner=request.user.username
                obj.save()
                message="Bid placed Successfully !"
                alert_color='success'
    winnerx=Listing.objects.get(id=listing_id).winner

    context={
        'data':data,
        'comment_form':form,
        'comments':comments,
        'item_in_watchlist':item_in_watchlist,
        'message':message,
        'is_closed':is_closed,
        'is_owner':is_owner,
        'color':alert_color,
        'bidform':bidform,
        'winner':winnerx
        }
    return render(request,'auctions/detail.html',context)

def category(request):
    category=Category.objects.all()
    al=Listing.objects.all().exclude(closed=True)
    return render(request,'auctions/category.html',{'category':category,'active_listings':al})

def category_listing(request,id):
    category_listings=Listing.objects.values().exclude(closed=True).filter(category=id)
    category=Category.objects.all()
    context={
        'category':category,
        'category_listings':category_listings
    }
    return render(request,'auctions/category_wise_listing.html',context)

@login_required
def close_listing(request,listing_id):
    a=Listing.objects.get(id=listing_id)
    a.closed=True
    a.save()
    return HttpResponseRedirect(reverse('detail_listing',args=(listing_id,)))

@login_required
def watchlist(request):
    watchlist_items=User.objects.get(id=request.user.id).watchlist_items.all()
    return render(request,'auctions/watchlist.html',{'watchlist_items':watchlist_items})


@login_required
def add_to_watchlist(request,listing_id):
    l=Listing.objects.get(id=listing_id)
    u=User.objects.get(id=request.user.id)
    l.watchlist_users.add(u)
    return HttpResponseRedirect(reverse('watchlist'))


@login_required
def remove_from_watchlist(request,listing_id):
    l=Listing.objects.get(id=listing_id)
    u=User.objects.get(id=request.user.id)
    l.watchlist_users.remove(u)
    return HttpResponseRedirect(reverse('detail_listing',args=(listing_id,)))

        
