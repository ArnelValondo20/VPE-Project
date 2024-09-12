from typing import List, Optional

from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.pagination import LimitOffsetPagination


class MultiQuerysetPagination(LimitOffsetPagination):
    def paginate(self,
                 querysets: List[QuerySet],
                 request: Request,
                 *args, **kwargs) -> Optional[List[QuerySet]]:
        self.limit = self.get_limit(request)
        self.offset = self.get_offset(request)
        self.count = self._count_all(querysets)
        limit = self.limit
        offset = self.offset
        item = 0
        queryset = querysets[item]
        count = self.get_count(queryset)
        while offset > count and len(querysets) - 1 != item:
            offset -= count
            item += 1
            queryset = querysets[item]
            count = self.get_count(queryset)
        result = self.paginate_queryset(queryset, request, offset, limit)
        while self.limit > len(result) and len(querysets) - 1 != item:
            limit = self.limit - len(result)
            item += 1
            queryset = querysets[item]
            result += self._paginate_queryset(queryset, request, limit=limit)
        return result

    def _count_all(self, querysets: List[QuerySet]) -> int:
        count = 0
        for queryset in querysets:
            count += queryset.count()
        return count

    def _paginate_queryset(self,
                           queryset: QuerySet,
                           request: Request,
                           offset: int = 0,
                           limit: int = None) -> Optional[List[QuerySet]]:
        if limit is None:
            return
        self.request = request
        count = self.get_count(queryset)
        if count > limit and self.template is not None:
            self.display_page_controls = True

        if count == 0 or offset > count:
            return []
        return list(queryset[offset:offset + limit])
