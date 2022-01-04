from django.contrib.auth.middleware import get_user
from django.http import HttpResponse, JsonResponse
from messenger_backend.models import Profile, User
from rest_framework.views import APIView


class Profiles(APIView):

    def post(self, request):
        try:
            user = get_user(request)

            if user.is_anonymous:
                return HttpResponse(status=401)

            user_id = user.id
            body = request.data
            address = body.get("address")
            phone = body.get("phone")
            gender = body.get("gender")
            age = body.get("age")
            
            if user_id:
                user = User.objects.filter(id=user_id).first()         
                profile = Profile(
                    address=address,
                    phone=phone,
                    gender=gender,
                    age=age,
                    user=user
                )
                
                profile.save()

                profile_json = profile.to_dict()

                return JsonResponse({"profile": profile_json})

            return HttpResponse(status=401)

        except Exception as e:
            return HttpResponse(status=500)


    def get(self, request):
        try:
            user = get_user(request)

            if user.is_anonymous:
                return HttpResponse(status=401)
            
            profile = Profile.objects.filter(user=user.id).first()
            profile_json = profile.to_dict()

            return JsonResponse({"profile": profile_json})

        except Exception as e:
            return HttpResponse(status=500)


    def patch(self, request):
        try:
            user = get_user(request)

            if user.is_anonymous:
                return HttpResponse(status=401)

            profile = Profile.objects.get(user=user.id)

            body = request.data

            if "address" in body:
                profile.address = body.get("address")

            if "phone" in body:
                profile.phone = body.get("phone")

            if "gender" in body:
                profile.gender = body.get("gender")

            if "age" in body:
                profile.age = body.get("age")

            profile.save()

            profile_json = profile.to_dict()

            return JsonResponse({"profile": profile_json})

        except Exception as e:
            return HttpResponse(status=500)

    def delete(self, request):
        try:
            user = get_user(request)

            if user.is_anonymous:
                return HttpResponse(status=401)
            
            profile = Profile.objects.filter(user=user.id).first()
            profile.delete()
            profile_json = profile.to_dict()

            return JsonResponse({"profile": profile_json})

        except Exception as e:
            return HttpResponse(status=500)