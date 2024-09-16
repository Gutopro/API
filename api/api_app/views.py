import logging
import time
import json
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.views.decorators.vary import vary_on_headers

logger = logging.getLogger('api_logger')


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("Authorization"))
    def get(self, request):
        # Start time
        start_time = time.time()

        content = {'message': 'Hello, World!'}
        response = Response(content)
        # End time
        end_time = time.time()
        duration = end_time - start_time

        # Log request and response details
        log_data = {
            'user': request.user.username if request.user.is_authenticated else 'Anonymous',
            'method': request.method,
            'url': request.build_absolute_uri(),
            'request_data': request.data if request.method != 'GET' else {},
            'response_status': response.status_code,
            'response_data': response.data,
            'start_time': start_time,
            'end_time': end_time,
            'duration': duration
        }

        # Log to file in JSON format
        logger.debug(json.dumps(log_data, indent=4))

        return response
