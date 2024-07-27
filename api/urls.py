from django.urls import include, path

from drfapp.views import team, user, UserList, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"users_list", UserViewSet, basename="users_list")

urlpatterns = router.urls

urlpatterns = [
    path("",include(router.urls)),
    path("team/", team, name="team"),
    path("user/", user, name="user"),
    path("users/", UserList.as_view(), name="users"),

]