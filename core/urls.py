from django.conf.urls import include, url, patterns
import core.views as coreviews

urlpatterns = [
    url(r'^$', coreviews.LandingView.as_view()),
]