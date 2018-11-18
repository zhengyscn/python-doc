from .models import Photo, PhotoGroup

from django.views.generic.list import ListView


class PhotoListView(ListView):
    template_name = 'photo_list.html'
    context_object_name = 'photo_list'

    def get_queryset(self):
        groups = PhotoGroup.objects.all()
        photodata = {}
        for group in groups:
            article_list = Photo.objects.filter(img_group__name=group).filter(display=True)
            photodata[group] = article_list
        return photodata