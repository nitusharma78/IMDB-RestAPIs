from django.shortcuts import render
from rest_framework import status
from .models import User, StreamPlatForm, WatchList,Review
from .serializers import ReviewSerializer, WatchListSerializer, StreamPlatFormSerializer
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response


# Review Class
class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

# Stream Class

class StreamPlatFormAv(APIView):

    def get(self, request):
        platfrom = StreamPlatForm.objects.all()
        serializer = StreamPlatFormSerializer(platfrom, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        platform = StreamPlatForm.objects.create()
        serializer = StreamPlatFormSerializer(platform,  data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class StreamDetailsAV(APIView):

    def get(self, request, pk):
        platform = StreamPlatForm.objects.get(pk=pk)
        serializer = StreamPlatFormSerializer(platform)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, pk):
        platform = StreamPlatForm.objects.get(pk=pk)
        serializer = StreamPlatFormSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request,pk):
        platform = StreamPlatForm.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# watchlist class

class WatchListAv(APIView):

    def get(self, request):
        watchlist = WatchList.objects.all()
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class WatchListDetailsAV(APIView):

    def get(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(movie, data=request.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
        