from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ads
import json


@method_decorator(csrf_exempt, name="dispatch")
class StatusView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class PostAdsView(View):
    def get(self, request):
        ads_data = Ads.objects.all()
        response = []

        for inform in ads_data:
            response.append({
                "id": inform.id,
                "name": inform.name,
                "author": inform.author,
                "price": inform.price,
                "description": inform.description,
                "address": inform.address,
                "is_published": inform.is_published})

        return JsonResponse(response, safe=False)

    def post(self, request):
        ads_data = json.loads(request.body)

        ads_ = Ads()
        ads_.name = ads_data["name"]
        ads_.author = ads_data["author"]
        ads_.price = ads_data["price"]
        ads_.description = ads_data["description"]
        ads_.address = ads_data["address"]
        ads_.is_published = ads_data["is_published"]

        try:
            ads_.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        ads_.save()

        return JsonResponse(ads_data, safe=False)


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads_ = self.get_object()

        return JsonResponse({
            "id": ads_.id,
            "name": ads_.name,
            "author": ads_.author,
            "price": ads_.price,
            "description": ads_.description,
            "address": ads_.address,
            "is_published": ads_.is_published,
        })


# TODO unsafe
@method_decorator(csrf_exempt, name="dispatch")
class DownloadAdsView(View):
    def get(self, request):
        with open('datasets/ads.json', 'r') as file:
            data = json.load(file)

            for item in data:
                ads_ = Ads(name=item['name'], author=item['author'], price=item['price'],
                           description=item['description'], address=item['address'], is_published=item["is_published"])
                ads_.save()

        return JsonResponse({"status": "ok"}, status=200)
