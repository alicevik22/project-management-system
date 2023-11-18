from django.urls import path

from .views import (
    BoardListView,
    ColumnCreateView,
    ColumnUpdateView,
    ColumnUpdateSequenceView,
    ColumnDeleteView
)


urlpatterns = [
    path('board/list/', BoardListView.as_view(), name='board_list'),
    path('column/create/', ColumnCreateView.as_view(), name='column_create'),
    path('column/update/', ColumnUpdateView.as_view(), name='column_update'),
    path(
        'column/update/sequence/',
        ColumnUpdateSequenceView.as_view(),
        name='column_sequence_update'
    ),
    path('column/delete/', ColumnDeleteView.as_view(), name='column_delete')
]
