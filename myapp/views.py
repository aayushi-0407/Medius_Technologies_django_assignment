# views.py
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required




# views.py

# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login

# def login_view(request):
#     if request.method == 'POST':
#         # Handle login form submission
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             next_url = request.GET.get('next', '/default-url/')  # Get the next parameter or use a default URL
#             return redirect(next_url)
#         else:
#             # Handle invalid login
#             return HttpResponse("Invalid login credentials")
#     else:
#         # Display login form
#         return render(request, 'login.html')

# @login_required
def send_email_function(request):
    if request.method == 'POST': #load all data
        subject = request.POST['subject']
        recipient_email = request.POST['recipient_email']
        cc_email = request.POST.get('cc_email')
        bcc_email = request.POST.get('bcc_email')
        message = request.POST['message']
        images = request.FILES.getlist('images')  # Get list of image files
        pdf = request.FILES.get('pdf')  # Get PDF file

        from_email = settings.EMAIL_HOST_USER
        to_email = [recipient_email]

        # Create EmailMessage object
        email = EmailMessage(subject, message, from_email, to_email)

        # Add CC and BCC if any
        if cc_email:
            email.cc = [cc_email]
        if bcc_email:
            email.bcc = [bcc_email]

        # Attach image files if any
        for image in images:
            email.attach(image.name, image.read(), image.content_type)

        # Attach PDF file if any
        if pdf:
            email.attach(pdf.name, pdf.read(), pdf.content_type)

        # Send email
        email.send()

        return HttpResponse("Email sent successfully!")

    return render(request, 'email.html')
