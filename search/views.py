from rest_framework.response import Response
from rest_framework.views import APIView

from search import models
from search.serializers import MovieSerializer


# Create your views here.


class GetSearchResult(APIView):

    def get(self, request, *args, **kwargs):
        movie = request.query_params["movie"]
        obj = models.Movie.objects.filter(name__contains=movie)
        movies = MovieSerializer(obj, many=True).data
        return Response(data=movies, status=200)


class AddMovie(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        data["popularity"] = data.pop("99popularity")
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"success": True}, status=200)
