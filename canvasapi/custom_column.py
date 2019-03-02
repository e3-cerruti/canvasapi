from __future__ import absolute_import, division, print_function, unicode_literals

from six import python_2_unicode_compatible

from canvasapi.canvas_object import CanvasObject
from canvasapi.column_data import ColumnData
from canvasapi.paginated_list import PaginatedList
from canvasapi.util import combine_kwargs


@python_2_unicode_compatible
class CustomColumn(CanvasObject):

    def __str__(self):
        return "{} ({})".format(self.title, self.id)

    def delete(self):
        """
        Delete a custom gradebook column

        Permanently deletes a custom column and its associated data.


        :calls: `DELETE /api/v1/courses/:course_id/custom_gradebook_columns/:id \
        <https://canvas.instructure.com/doc/api/custom_gradebook_columns.html#method.custom_gradebook_columns_api.destroy>`_

        :rtype: :class:`canvasapi.custom_column.CustomColumn`
        """

        response = self._requester.request(
            'DELETE',
            'courses/{}/custom_gradebook_columns/{}'.format(self.course_id, self.id)
        )
        return CustomColumn(self._requester, response.json())

    def get_entries(self, course, **kwargs):
        """
        List Entries for a Column


        :calls: `GET /api/v1/courses/:course_id/custom_gradebook_columns/:id/data \
        <https://canvas.instructure.com/doc/api/custom_gradebook_columns.html#method.custom_gradebook_column_data_api.index>`_

        :rtype: :class:`canvasapi.paginated_list.PaginatedList` of
            :class:`canvasapi.column_data.ColumnData`
        """
        return PaginatedList(
            ColumnData,
            self._requester,
            'GET',
            'courses/{}/custom_gradebook_columns/{}/data'.format(course.id, self.id),
            _kwargs=combine_kwargs(**kwargs)
        )
