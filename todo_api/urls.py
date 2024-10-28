from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# initializing router which handles auto-generation of URL
router = DefaultRouter() 

# registering TaskViewSet with router and specifying URL pattern
router.register(r'tasks', TaskViewSet, basename='task')

# connecting the router to urlpatterns (in main project urls..py)
urlpatterns = router.urls