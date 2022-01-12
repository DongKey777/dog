from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse
from django.views import View

from .models import Dog
from owners.models import Owner

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        dog = Dog(
            name = data["name"],
            age = data["age"],
            owner_id = data['owner_id']
        )
        dog.save()

        return JsonResponse({"INSERTED_DOG_ID" : dog.id}, status= 201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []

        for dog in dogs:
            results.append({
                "id": dog.id,
                "name": dog.name,
                "age": dog.age,
                "owner": {
                    "id": dog.owner.id,
                    "name": dog.owner.name
                }
            })

        return JsonResponse({"dogs": results}, status=200)


