import pytest
from Read_Excel_file_paramerization import get_test_data   # adjust file name

test_data = get_test_data(
    "Read_Excel.xlsx",
    "Sheet1"
)

@pytest.mark.parametrize("username,password", test_data)
def test_login(username, password):

    print(username, password)

