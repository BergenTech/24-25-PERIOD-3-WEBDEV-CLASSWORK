from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        
        # If user is already made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request,"You already made an inquiry for the listing!" )
                return redirect('/listings/'+listing_id)
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        # Send an email to the ADMIN
        send_mail(
            "Property Listing Inquiry",
            "There has been an inquiry for " + listing + ".Sign into admin panel for more information.",
            "emregemici@gmail.com", # Your Email
            ["emrgem@bergen.org"], # Admin Email - Recipient
            fail_silently=False,
        )
        messages.success(request, "Your request submitted! A realtor will get back to you soon!")
        return redirect('/listings/'+listing_id)
        
            