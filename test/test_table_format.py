"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""


import pytest

from pytablewriter import FormatAttr, TableFormat


class Test_TableFormat_search_table_format:
    @pytest.mark.parametrize(
        ["value", "expected"],
        [
            [
                FormatAttr.TEXT,
                [
                    TableFormat.CSV,
                    TableFormat.HTML,
                    TableFormat.JAVASCRIPT,
                    TableFormat.JSON,
                    TableFormat.JSON_LINES,
                    TableFormat.LATEX_MATRIX,
                    TableFormat.LATEX_TABLE,
                    TableFormat.LTSV,
                    TableFormat.MARKDOWN,
                    TableFormat.MEDIAWIKI,
                    TableFormat.NUMPY,
                    TableFormat.PANDAS,
                    TableFormat.PYTHON,
                    TableFormat.RST_CSV_TABLE,
                    TableFormat.RST_GRID_TABLE,
                    TableFormat.RST_SIMPLE_TABLE,
                    TableFormat.SPACE_ALIGNED,
                    TableFormat.TOML,
                    TableFormat.TSV,
                    TableFormat.UNICODE,
                ],
            ],
            [FormatAttr.BIN, [TableFormat.EXCEL_XLS, TableFormat.EXCEL_XLSX, TableFormat.SQLITE]],
            [FormatAttr.API, [TableFormat.ELASTICSEARCH]],
            [0, []],
        ],
    )
    def test_normal(self, value, expected):
        assert set(TableFormat.find_all_attr(value)) == set(expected)
