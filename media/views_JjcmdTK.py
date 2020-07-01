from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.files.base import ContentFile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
import json

from .models import Posts, Images

class PostsListView(ListView):
    model = Posts
    template_name = 'posts_list.html'

def PostsDetailView(request,pk):
    post = Posts.objects.get(pk=pk)
    images = Images.objects.filter(location=post)
    context ={
        'object':post,
        'images':images
    }
    return render(request,'posts_detail.html',context)




class PostsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ('title', 'body')
    template_name = 'posts_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author ==self.request.user


class PostsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Posts
    template_name = 'posts_delete.html'
    success_url = reverse_lazy('posts_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author ==self.request.user


class PostsCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    template_name = 'posts_new.html'
    fields = ('title', 'body', 'background', 'terrain', 'fname','images','posx','posy','posz')
    login_url = 'login'
    raise_exception = True

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def check_user_name(request):
        if request.GET:
            background = request.GET[""]

    def post(self, request, *args, **kwargs):
        #self.object = None
        #post = super().post(request, *args, **kwargs)
        #return HttpResponse({post.url})
        if request.method in  ('POST','FILES'):
            post = Posts()
            post.title = request.POST.get('title')
            post.body = request.POST.get('body')
            post.background = request.POST.get('background')
            post.terrain = request.POST.get('terrain')
            post.fname = request.POST.get('checkname')
            post.author_id = request.POST.get('author_id')
            post.posx = float(request.POST.get('posx'))
            post.posy = float(request.POST.get('posy'))
            post.posz = float(request.POST.get('posz'))
            post.rotx = float(request.POST.get('rotx'))
            post.roty = float(request.POST.get('roty'))
            post.rotz = float(request.POST.get('rotz'))
            post.save()
            list_posx = list(reversed(request.POST.getlist('posx')))
            list_posy = list(reversed(request.POST.getlist('posy')))
            list_posz = list(reversed(request.POST.getlist('posz')))
            list_rotx = list(reversed(request.POST.getlist('rotx')))
            list_roty = list(reversed(request.POST.getlist('roty')))
            list_rotz = list(reversed(request.POST.getlist('rotz')))
            for f in request.FILES.getlist('images'):
                data = f.read()
                image = Images(location=post,posx=float(list_posx.pop()),posy=float(list_posy.pop()),posz=float(list_posz.pop()),rotx=float(list_rotx.pop()),roty=float(list_roty.pop()),rotz=float(list_rotz.pop()))
                image.image.save(f.name,ContentFile(data))
                image.save()
            obj = Posts.objects.latest('id')
            response = redirect(obj)
            return response
        else:
            return render(request, '', {})



class PostsManual(ListView):
    model = Posts
    template_name = 'manual.html'

class PostsYouProject(ListView):
    model = Posts
    template_name = 'user.html'