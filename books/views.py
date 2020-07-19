from django.shortcuts import render, redirect
from login.models import User
from books.models import Book
from django.contrib import messages

# Create your books views here.
def index(request):
  context = {
    'users': User.objects.all(),
    'books': Book.objects.all(),
    'current_user': User.objects.get(id=request.session['user_id'])
  }
  if 'user_id' not in request.session:
    return redirect('/')
  else:

    return render(request, 'books/index.html', context)
    
#add new books 
def add_books(request):
  errors = User.objects.validate_books(request.POST)
  book_uploader = User.objects.get(id=request.session['user_id'])

  if errors:
    for value in errors.values():
      messages.error(request, value)
    return redirect('/books')

  else:
    new_book = Book.objects.create(title = request.POST['title'],
    description = request.POST['des'],
    uploader = book_uploader,
    )
    likers = book_uploader.liked_books.add(new_book)
    return redirect('/books')
  
#book details
def book_details(request, book_id):
  current_book = Book.objects.get(id=book_id)
  context = {
    'cur_book': current_book
  }
  if 'user_id' not in request.session:
      return redirect('/')
  else:
      return render(request, 'books/book.html', context)

def fav(request, book_id):
  fav_book = Book.objects.get(id=book_id)
  who_fav = User.objects.get(id=request.session['user_id'])
  who_fav.liked_books.add(fav_book)
  return redirect('/books')

def un_favorite(request, book_id):
  dislike_book = Book.objects.get(id=book_id)
  user_disliking = User.objects.get(id=request.session['user_id'])
  user_disliking.liked_books.remove(dislike_book)
  return redirect('/books')

def update_book(request, book_id):
  book_to_update = Book.objects.get(id=book_id)
  errors = User.objects.validate_books(request.POST)

  if len(errors) >0:
    for values in errors.values():
      messages.error(request, values)
    return redirect(f'/books/{book_to_update.id}')
  else:
    book_to_update.title = request.POST['title']
    book_to_update.description = request.POST['des']
    book_to_update.save()
    return redirect('/books')
  
def delete_book(request, book_id):
  book_to_destroy = Book.objects.get(id=book_id)
  if book_to_destroy.uploader.id == request.session['user_id']:
    book_to_destroy.delete()
    return redirect('/books')
  else:
    return redirect('/')