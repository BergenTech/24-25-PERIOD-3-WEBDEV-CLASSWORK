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
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'listings/search.html',context)