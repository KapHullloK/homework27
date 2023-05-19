import json

from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from categories.models import Categories


@method_decorator(csrf_exempt, name="dispatch")
class PostCategoriesView(View):
    def get(self, request):
        categories_data = Categories.objects.all()
        response = []

        for inform in categories_data:
            response.append({
                "id": inform.id,
                "name": inform.name})

        return JsonResponse(response, safe=False)

    def post(self, request):
        ads_data = json.loads(request.body)

        categories_ = Categories()
        categories_.name = ads_data["name"]

        try:
            categories_.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        categories_.save()

        return JsonResponse(ads_data, safe=False)


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        categories_ = self.get_object()

        return JsonResponse({
            "id": categories_.id,
            "name": categories_.name,
        })


# TODO unsafe
@method_decorator(csrf_exempt, name="dispatch")
class DownloadCategoriesView(View):
    def get(self, request):
        with open('datasets/categories.json', 'r') as file:
            data = json.load(file)

            for item in data:
                categories_ = Categories(name=item['name'])
                categories_.save()

        return JsonResponse({"status": "ok"}, status=200)
