from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods

from samples.models import Sample, Category, CategoryForm, SampleForm

# from samples.forms import CategoryForm


@require_http_methods(["GET"])
def index(request):
    return render(request, 'index.html')


# sample
@require_http_methods(["GET"])
def index_sample(request):
    samples = Sample.objects.all()
    context = {
        "samples": samples,
    }
    return render(request, 'sample/index.html', context)


@require_http_methods(["GET"])
def detail_sample(request, sample_id):
    sample = get_object_or_404(Sample, pk=sample_id)
    return render(request, 'sample/detail.html', {'sample': sample})


# category
@require_http_methods(["GET"])
def index_category(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, 'category/index.html', context)


@require_http_methods(["GET"])
def detail_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'category/detail.html', {'category': category})


@require_http_methods(["GET", "POST"])
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.name = request.POST['name']
            form.description = request.POST['description']
            form.save()
            return redirect('detail_category', category_id=form.pk)
    else:
        form = CategoryForm()
    return render(request, 'category/create.html', {'form': form})


@require_http_methods(["GET", "POST"])
def create_sample(request):
    if request.method == "POST":
        form = SampleForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.serial_number = request.POST["serial_number"]
            form.name = request.POST["name"]
            form.arrival_date = request.POST["arrival_date"]
            form.content = request.POST["content"]
            form.comments = request.POST["comments"]
            try:
                form.category = Category.objects.get(pk=request.POST["category"])
            except Category.DoesNotExist:
                raise
            form.save()
            return redirect('detail_sample', sample_id=form.pk)
    else:
        form = SampleForm()
    return render(request, 'sample/create.html', {'form': form})
