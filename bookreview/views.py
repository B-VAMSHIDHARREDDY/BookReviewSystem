from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Save book data
    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    #List of books
    def list(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        author = request.query_params.get('author', None)
        publication_year = request.query_params.get('publication_year', None)

        if author:
            queryset = queryset.filter(author__name__icontains=author)
        if publication_year:
            queryset = queryset.filter(publication_year=publication_year)

        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        book_title = self.request.query_params.get('book', None)

        #Get Reviews based on book title
        if book_title:
            reviews = Review.objects.filter(book__title__icontains=book_title)
        else:
            reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    # Save the Review for books 
    def create(self, request, *args, **kwargs):
        serializer = ReviewSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
