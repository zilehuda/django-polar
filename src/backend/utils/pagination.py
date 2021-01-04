from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response


class StandardPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_count': self.page.paginator.count,
            'count': len(data),
            'results': data
        })
