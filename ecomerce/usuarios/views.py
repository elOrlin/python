# Create your views here.
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from usuarios.api.serializers import UsuarioTokenSerializer
from django.contrib.sessions.models import Session

class UsuarioToken(APIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(
                user = UsuarioTokenSerializer().Meta.model().objects.filter(username = username).first()
            )
            
            return Response({
                'token': user_token.key
            })
            
        except:
            return Response({
                'error': 'Credenciales enviadas incorrectas'
            }, status = status.HTTP_400_BAD_REQUEST)

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user:
                token, created = Token.objects.get_or_create(user = user)
                user_serializer = UsuarioTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesion Exitoso!'
                        
                    }, status = status.HTTP_201_CREATED)

                    
                elif token:
                        token = Token.objects.create(user = user)
                        return Response({
                            'message': 'Ya se ha iniciado sesion con este usuario!'
                        
                        }, status = status.HTTP_409_CONFLICT)
                        
                else:
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.month)
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()

                    return Response({'error', 'Este usuario no puede iniciar sesion.'}, status = status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error', 'Nombre de usuario o contraseña incorrectos.'}, status = status.HTTP_400_BAD_REQUEST)
        
        return Response({'mensaje': 'has iniciado sesion con exito'}, status = status.HTTP_200_OK)
        
class Logout(APIView):
    
    def get(self, request, *args, **kwargs):
            token = request.GET.get('token')
            print(f'no se ha encontrado {token}')
            token = Token.objects.filter(key = token).first()
           
            if token:
                user = token.user
                
                all_sessions = Session.objects.filter(expire_date__gte = datetime.month)
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                            
                token.delete()
                
                session_message = 'Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado.'
                return Response({'token_message': token_message, 'session_message': session_message}, status = status.HTTP_200_OK)
            
            return Response({'error': 'No se ha encontrado un usuario con estas credenciales.'}, status = status.HTTP_400_BAD_REQUEST)
        
        
        
        
        
        

"""
importa el datetime, status, response, la vista de obtainauthtoken, serializer token de usuario, el token, session

    serializamos los datos que llegan por post 
    confirmamos si los datos serializados son validos
    validamos los datos serializados del usuario
    confirmamos si el usuario existe
    obtenga o crea un token del usuario
    serializamos los datos para mostrar los
    si el token esta creado retorna el token, usuario, y mensaje de inicio de sesion con status creado
    filtra los objectos de sesion expirados 
    si existe una expiracion correcta
    itera todas las sesiones, obtenga la sesion decodificada
    si el usuario id es igual a la session obtenida del usuario autenticado id
    borra la sesion
    si el token existe eliminalo y crea un token nuevo
    retorna un mensaje ya se ha iniciado sesion y un status conflit
     
"""
