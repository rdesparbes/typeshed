from _typeshed import Incomplete

from openpyxl.worksheet.worksheet import Worksheet

def read_dimension(source): ...

class ReadOnlyWorksheet:
    cell: Incomplete
    iter_rows: Incomplete
    @property
    def values(self): ...
    @property
    def rows(self): ...
    __getitem__ = Worksheet.__getitem__
    __iter__ = Worksheet.__iter__
    parent: Incomplete
    title: str
    sheet_state: str
    def __init__(self, parent_workbook, title: str, worksheet_path, shared_strings) -> None: ...
    def calculate_dimension(self, force: bool = False): ...
    def reset_dimensions(self) -> None: ...
    @property
    def min_row(self): ...
    @property
    def max_row(self): ...
    @property
    def min_column(self): ...
    @property
    def max_column(self): ...
