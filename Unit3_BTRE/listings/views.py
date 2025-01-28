from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator
from .choices import price_choices, bedroom_choices, state_choices
from .models import Listing


# Create your views here.
def index(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings':paged_listings
    }
    return render(request, 'listings/listings.html', context)
    
def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html',context)
    
def search(request):
    # listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    queryset_listings = Listing.objects.order_by('-list_date')
    # Filter by contains keywords
    if 'keywords' in request.GET:
        keywords  = request.GET['keywords']
        if keywords:
            queryset_listings = queryset_listings.filter(description__icontains = keywords)
    # Filter by state
    if 'state' in request.GET:
        state  = request.GET['state']
        if state:
            queryset_listings = queryset_listings.filter(state__iexact = state)
    # Filter by city
    if 'city' in request.GET:
        city  = request.GET['city']
        if city:
            queryset_listings = queryset_listings.filter(city__iexact = city)
    # Filter by max bedrooms
    if 'bedrooms' in request.GET:
        bedrooms  = request.GET['bedrooms']
        if bedrooms:
            queryset_listings = queryset_listings.filter(bedrooms__lte = bedrooms)
    # Filter by max price
    if 'price' in request.GET:
        price  = request.GET['price']
        if price:
            queryset_listings = queryset_listings.filter(price__lte = price)
        
    context = {
        'listings': queryset_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values' : request.GET
    }
    return render(request, 'listings/search.html',context)