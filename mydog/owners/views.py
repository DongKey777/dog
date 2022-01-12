from django.shortcuts import render

# Create your views here.

import json

from django.http import JsonResponse,HttpResponse
from django.views import View

from .models import Owner

class OwnersView(View):
    def post(self,request):

        input_data = json.loads(request.body)

        owner = Owner.objects.create(
            age = input_data["age"],
            name = input_data["name"],
            email = input_data["email"]
        )

        return JsonResponse({"owner_id" : owner.id}, status = 201)

    def get(self,request):

        owners = Owner.objects.all()

        results = []

        for owner in owners:
            results.append({
                "id" : owner.id,
                "name" : owner.name,
                "age" : owner.age,
                "dogs" : [{"id": dog.id,"name" : dog.name} for dog in owner.dog_set.all()]
            })

        return JsonResponse({"owners" : results}, status= 200)
