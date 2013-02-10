from djblets.datagrid.grids import DataGrid

from reviewboard.reviews.datagrids import DashboardDataGrid
from reviewboard.reviews.datagrids import get_sidebar_counts


class CustomDataGrid(DashboardDataGrid):
    def __init__(self, *args, **kwargs):
        DashboardDataGrid.__init__(self, *args, **kwargs)
        self.counts = {}
        self.default_sort = ["-last_updated"]
        self.default_columns = [
            "new_updates", "star", "summary", "submitter",
            "time_added", "last_updated_since"
        ]

    def get_queryset(self, profile):
        raise NotImplementedError("Please implement this method")

    def load_extra_state(self, profile):
        self.queryset = self.get_queryset(profile)
        self.counts = get_sidebar_counts(self.request.user, None)
        return False
