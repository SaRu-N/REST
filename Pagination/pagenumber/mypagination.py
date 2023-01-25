from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

# class MyPagination(PageNumberPagination):
#     page_size =3
#     # page_query_param='p'
#     page_size_query_param='records'
#     max_page_size=8
#     last_page_strings = 'end'

class MyPagination(LimitOffsetPagination):
    default_limit =5
    # limit_query_param ='mtlimit'
    # offset_query_param='myoffset'
    max_limit=7

