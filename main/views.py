from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView

from .models import Tutorial, TutorialCategory, TutorialSeries, News
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm, TutorForm, SeriesForm, CategoryForm


# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name="static/home.html",
                  context={"categories": TutorialCategory.objects.all})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("main:homepage")

    else:
        form = UserRegisterForm()
    return render(request, 'static/register.html', {'form': form})


def logout_request(request):
    logout(request);
    messages.info(request, "Logged out successfully.")
    return redirect("main:homepage")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are logged in as {username} ")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request, "static/login.html", {"form": form, "categories": TutorialCategory.objects.all})


def courses_request(request):
    return render(request=request,
                  template_name="static/courses.html",
                  context={"tutorials": Tutorial.objects.all, "categories": TutorialCategory.objects.all})


def about_request(request):
    return render(request=request,
                  template_name="static/about.html",
                  context={"tutorials": Tutorial.objects.all, "categories": TutorialCategory.objects.all})


def blog_request(request):
    return render(request=request,
                  template_name="static/blog.html",
                  context={"tutorials": Tutorial.objects.all, "categories": TutorialCategory.objects.all,
                           'news': News.objects.all()})


def contact_request(request):
    return render(request=request,
                  template_name="static/contact.html",
                  context={"tutorials": Tutorial.objects.all, "categories": TutorialCategory.objects.all})


def profile(request):
    return render(request=request,
                  template_name="static/profile.html",
                  context={"tutorials": Tutorial.objects.all, "categories": TutorialCategory.objects.all})


def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        series_urls = {}
        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("published")
            series_urls[m] = part_one.tutorial_slug
        return render(request,
                      "static/courses.html",
                      {"tutorial_series": matching_series, "part_ones": series_urls,
                       "categories": TutorialCategory.objects.all})

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
        tutorials_from_series = Tutorial.objects.filter(
            tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by("published")
        this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)
        return render(request,
                      "static/course.html",
                      {"tutorial": this_tutorial, "sidebar": tutorials_from_series,
                       "this_tutorial_idx": this_tutorial_idx, "categories": TutorialCategory.objects.all})
    news = [n.header for n in News.objects.all()]
    if single_slug in news:
        return render(request, "static/blog_single.html",
                      {"categories": TutorialCategory.objects.all, "news": News.objects.all})

    return HttpResponse(f"{single_slug} doesn't corresponded")


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = TutorialCategory
    form_class = CategoryForm

    def get_form_kwargs(self):
        kwargs = super(CategoryCreateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)


class SeriesCreateView(LoginRequiredMixin, CreateView):
    model = TutorialSeries
    form_class = SeriesForm

    def get_form_kwargs(self):
        kwargs = super(SeriesCreateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)


class TutorCreateView(LoginRequiredMixin, CreateView):
    model = Tutorial
    form_class = TutorForm

    def get_form_kwargs(self):
        kwargs = super(TutorCreateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)
