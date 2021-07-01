from django.views.generic import CreateView, DetailView, ListView

from .models import UploadedImage


class TemplateMatchingListView(ListView):
    model = UploadedImage


class TemplateMatchingCreateView(CreateView):
    model = UploadedImage
    fields = ["image", "needle", "threshold"]


class TemplateMatchingDetailView(DetailView):
    model = UploadedImage
