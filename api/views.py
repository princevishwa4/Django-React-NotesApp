from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Note
from api.serializers import NoteSerializer
from .utils import updateNote, getNoteDetail, deleteNote, getNotesList, createNote


@api_view(['GET', 'POST'])
def getNotes(request):
    if request.method == 'GET':
        return getNotesList(request)

    if request.method == 'POST':
        return createNote(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):
    if request.method == 'GET':
        return getNoteDetail(request, pk)

    if request.method == 'PUT':
        return updateNote(request, pk)

    if request.method == 'DELETE':
        return deleteNote(request, pk)



# @api_view(['GET'])
# def getNotes(request):
#     notes = Note.objects.all().order_by('-updated')
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getNote(request, pk):
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(note)
#     return Response(serializer.data)


# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(
#         body=data['body']
#     )
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)    


# @api_view(['PUT'])
# def updateNote(request, pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note, data=data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['DELETE'])
# def deletetNote(request, pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return Response("Note deleted succcessfully!")  