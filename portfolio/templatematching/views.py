from django.views.generic import CreateView, DetailView, ListView

from .models import UploadedImage


class TemplateMatchingListView(ListView):
    model = UploadedImage


class TemplateMatchingCreateView(CreateView):
    model = UploadedImage
    fields = ["image", "needle"]


class TemplateMatchingDetailView(DetailView):
    model = UploadedImage
