from rest_framework.pagination import PageNumberPagination

class DefaultPagination(PageNumberPagination):
    # https://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
    page_size = 1
    page_query_param = 'page'
    page_size_query_param = 'size' # None
    max_page_size = 1000
    last_page_strings = ('last','end',)


