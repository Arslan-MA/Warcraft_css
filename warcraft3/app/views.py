from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from app.models import *


class StartPage(TemplateView):
    template_name = 'app/start_page.html'


class AboutUsPage(TemplateView):
    template_name = 'app/about_us_page.html'


class PictureListPage(ListView):
    model = Picture
    template_name = 'app/picture_list.html'
    context_object_name = 'photo_list'


class VideoListPage(TemplateView):
    template_name = 'app/video_page.html'


class AudioListPage(TemplateView):
    template_name = 'app/audio_page.html'


class CutsceneListPage(ListView):
    model = Video
    template_name = 'app/video/cutscenes_list.html'
    context_object_name = 'cutscenes_list'


class GameplayListPage(ListView):
    model = Video
    template_name = 'app/video/gameplay_list.html'
    context_object_name = 'gameplay_list'


class MusicListPage(ListView):
    model = Audio
    template_name = 'app/audio/music_list.html'
    context_object_name = 'music_list'


class ReplicasListPage(ListView):
    model = Audio
    template_name = 'app/audio/replicas_list.html'
    context_object_name = 'replicas_list'
