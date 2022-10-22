from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from books.serializers import *
from books.models import *
# Create your views here.


@api_view(['GET', 'POST'])
def books(request):
    print(request.user)
    if request.method == 'GET':
        book = Book.objects.all()
        return Response(BookListSerializer(book, many=True).data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def one_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Book not found'})
    if request.method == 'GET':
        return Response(BookListSerializer(book).data)