from django.shortcuts import render, redirect, get_object_or_404
from .forms import AutorForm, LibroForm
from .models import Autor, Libro
from django.utils import timezone



def inicio(request):
    libros = Libro.objects.all().order_by('-id')[:5]  # Muestra los 5 últimos libros
    return render(request, 'inicio.html', {'libros': libros, 'now': timezone.now()})
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm()
    return render(request, 'crear_autor.html', {'form': form})

def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'listar_autores.html', {'autores': autores})

def editar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'editar_autor.html', {'form': form})

# Vista para eliminar un autor
def eliminar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.delete()
    return redirect('listar_autores')

# Vista para crear un libro
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'crear_libro.html', {'form': form})

# Vista para listar libros
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'listar_libros.html', {'libros': libros})

# Vista para editar un libro
def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'editar_libro.html', {'form': form})

# Vista para eliminar un libro
def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.delete()
    return redirect('listar_libros')
