from django.urls import path
from .views import (ReviewDetail, 
                    ReviewList,
                    StreamPlatFormAv, 
                    StreamDetailsAV, 
                    WatchListAv,
                    WatchListDetailsAV)


urlpatterns = [
    path('list/', WatchListAv.as_view(), name='watchlist'),
    path('list/<int:pk>/', WatchListDetailsAV.as_view(), name='watchlist-details'),
    path('stream/', StreamPlatFormAv.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamDetailsAV.as_view(), name='watchlist-details'),
    path('review/', ReviewList.as_view(), name='Review-List'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='Review-Detail'),


]

