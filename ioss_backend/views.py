from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import ShortenedURL
from .forms import URLForm
import string, random

# Helper to generate unique short code
def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(chars, k=length))
        if not ShortenedURL.objects.filter(short_code=code).exists():
            return code

def home(request):
    urls = ShortenedURL.objects.all().order_by('-created_at')
    message = None
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_code = generate_short_code()
            obj = ShortenedURL.objects.create(original_url=original_url, short_code=short_code)
            request.session['message'] = {'type': 'success', 'text': f'Short URL created: <a href="/{short_code}/">/{short_code}/</a>'}
            return redirect('home')
        else:
            message = {'type': 'danger', 'text': 'Invalid URL. Please try again.'}
    else:
        form = URLForm()
        if 'message' in request.session:
            message = request.session.pop('message')
    return render(request, 'home.html', {'form': form, 'urls': urls, 'message': message})

def redirect_short_url(request, short_code):
    obj = get_object_or_404(ShortenedURL, short_code=short_code)
    obj.click_count += 1
    obj.save()
    return redirect(obj.original_url)
