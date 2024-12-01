from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import CustomUser as User, Note
from .utils import send_email
import random
import datetime

# Create your views here.


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # check weather the email in currect format or not
        if "@" not in email or "." not in email.split("@")[1]:
            messages.info(request, "Invalide email")
            return redirect('/register/')

        user = User.objects.filter(email=email)

        if user.exists():
            messages.info(request, "Already registered please login.")
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        user.set_password(password)
        user.save()
        login(request, user)
        if not user.is_verified:
            otp = random.randint(100000, 999999)
            user.otp = otp
            send_email(user, otp)
            user.save()
            messages.info(request, "Please verify your email")
            return redirect('/verify/')

    return render(request, 'register.html')


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if "@" not in email or "." not in email.split("@")[1]:
            messages.info(request, "Invalide email")
            return redirect('/login/')

        if not User.objects.filter(email=email).exists():
            messages.info(request, "Invalide Email")
            return redirect('/login/')

        user = authenticate(email=email, password=password)

        if user is None:
            messages.info(request, "Invalide password")
            return redirect('/login/')

        else:
            login(request, user)
            if not user.is_verified:
                messages.info(request, "Please verify your email")
                return redirect('/verify/')
            else:
                return redirect('/new/')

    return render(request, 'login.html')


@login_required(login_url='/login/')
def verify_email(request):
    user = request.user
    if user.is_verified:
        return redirect('/')
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if not User.objects.filter(id=user.id, otp=otp).exists():
            messages.error(request, "Invalid OTP for this user")
            return redirect('/verify/')

        # Clear OTP after successful verification
        user.is_verified = True
        user.otp = None
        user.save()
        # Redirect to home page or any other appropriate page
        return redirect('/')
    if not messages.get_messages(request):
        messages.success(request, "Verify your email.")
        messages.success(request, "Account Created successfully.")
    return render(request, 'verify.html')


def log_out(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')
def new_note(request):
    if not request.user.is_verified:
        messages.info(request, "Please verify your email")
        return redirect('/verify/')
    if request.method == 'POST':
        note_new = Note()
        note_new.title = request.POST.get('note_title')
        note_new.content = request.POST.get('note_content')
        note_new.author = request.user
        note_new.id = note_new.title[:10] + '-' + \
            datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        note_new.save()
        return redirect('/note/' + str(note_new.id))
    return render(request, 'new.html')


def note_detail(request, pk):
    try:
        note_instance = Note.objects.get(id=pk)
        print(f"Note found - Title: {note_instance.title}, Content: {note_instance.content}")
    except Note.DoesNotExist:
        print(f"Note not found with id: {pk}")
        return HttpResponse("Note not found", status=404)

    return render(request, 'note.html', {'note': note_instance})


@login_required
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)
    return render(request, 'note_detail.html', {'note': note})


def home(request):
    user = request.user
    if user.is_authenticated:
        if not user.is_verified:
            messages.info(request, "Please verify your email")
            return redirect('/verify/')
    return render(request, 'index.html')


@login_required(login_url='/login/')
def resend_mail(request):
    user = request.user
    if user.is_verified:
        return redirect('/')
    otp = random.randint(100000, 999999)
    user.otp = otp
    send_email(user, otp)
    user.save()
    messages.info(request, "OTP sent to your email")
    return redirect('/verify/')


def about(request):
    return render(request, 'about.html')


@login_required
def notes_view(request):
    notes = Note.objects.filter(author=request.user)
    
    # Update any notes without IDs
    for note in notes:
        if not note.id:
            note_id = note.title.lower()[:10].replace(' ', '-') + '-' + timezone.now().strftime("%Y%m%d%H%M%S")
            note.id = note_id
            note.save()
    
    notes = notes.order_by('-created_at')
    return render(request, 'notes.html', {'notes': notes})


@login_required
def new_note_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_public = request.POST.get('is_public') == 'on'
        if title and content:
            # Generate a unique ID for the note
            note_id = title.lower()[:10].replace(' ', '-') + '-' + timezone.now().strftime("%Y%m%d%H%M%S")
            Note.objects.create(
                id=note_id,
                author=request.user,
                title=title,
                content=content,
                is_public=is_public,
                created_at=timezone.now()
            )
            messages.success(request, 'Note created successfully!')
            return redirect('notes')
        else:
            messages.error(request, 'Title and content are required.')
    return render(request, 'new_note.html')


@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_public = request.POST.get('is_public') == 'on'
        if title and content:
            note.title = title
            note.content = content
            note.is_public = is_public
            note.save()
            messages.success(request, 'Note updated successfully!')
            return redirect('notes')
        else:
            messages.error(request, 'Title and content are required.')
    return render(request, 'edit_note.html', {'note': note})


@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)
    note.delete()
    messages.success(request, 'Note deleted successfully!')
    return redirect('notes')


@login_required
def toggle_note_visibility(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)
    note.is_public = not note.is_public
    note.save()
    return HttpResponse(status=200)
