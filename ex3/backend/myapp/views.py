import requests
from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Preference
from .serializers import UserSerializer


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    users_data = [{
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "affiliate": user.affiliate,
        "preferences": [pref.preference for pref in user.preferences.all()]  # ← Usa related_name
    } for user in users]
    return JsonResponse({"users": users_data})

@api_view(['POST'])
def post_user(request):
    # Verifica que se han recibido los datos correctos en el request
    name = request.data.get('name')
    email = request.data.get('email')
    preferences = request.data.get('preferences', [])  # Ahora es una lista por defecto
    affiliate = request.data.get('affiliate')

    if not name or not email:
        return Response({"error": "El nombre y el correo son obligatorios"}, status=400)
    
    if not preferences or not isinstance(preferences, list):
        return Response({"error": "Las preferencias deben ser una lista y no pueden estar vacías"}, status=400)

    # Validar que las preferencias sean únicas
    if len(set(preferences)) != len(preferences):
        return Response({"error": "No se permiten preferencias duplicadas"}, status=400)

    # Validar que haya al menos una preferencia par y una impar
    odd_exists = any(int(p) % 2 != 0 for p in preferences if str(p).isdigit())
    even_exists = any(int(p) % 2 == 0 for p in preferences if str(p).isdigit())

    if not (odd_exists and even_exists):
        return Response({"error": "Debe haber al menos una preferencia par y una impar"}, status=400)
    
    try:
        # Crear el usuario
        user = User.objects.create(name=name, email=email, affiliate=affiliate)
        
        # Guardar las preferencias del usuario, asegurándonos de que estén ordenadas
        preferences_sorted = sorted(preferences, key=int)
        Preference.objects.bulk_create([Preference(user=user, preference=p) for p in preferences_sorted])

    except IntegrityError as e:
        return Response({"error": f"Error al crear el usuario o preferencias: {str(e)}"}, status=400)
    
    # Si todo está bien, hacer la petición al servidor de pruebas
    try:
        test_response = requests.post("https://invelonjobinterview.herokuapp.com/api/post_test", json=request.data)
        return Response(test_response.json())  # Responder con el resultado del servidor de pruebas
    except requests.exceptions.RequestException as e:
        return Response({"error": f"Error al conectar con el servidor de pruebas: {str(e)}"}, status=500)
