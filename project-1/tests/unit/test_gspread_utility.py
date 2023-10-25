import pytest
from main import Workbook
import subprocess
from typing import List
import os
from unittest.mock import patch, Mock

EXTRACT_SH_PATH = "/home/bee_nyah/Desktop/DATA_EPIC/Best_Nyah/project-1/extract.sh"

def subprocess_run(argument: List[str]) -> str:
    """_summary_
           This runs a bash script in a subprocess based on on the input arguments
    Args:
        argument (List[str]): takes list of string arguments

    Returns:
        str: output from bash run
    """
    arguments = argument

    return subprocess.run(
        ["bash", EXTRACT_SH_PATH, *arguments],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def test_bash_arguments() -> None:
    """_summary_
    Tests bash script fails with bad argumrnts
    Tests file downlad from bash script
    """
    # test for bad argument
    with pytest.raises(subprocess.CalledProcessError):
        bad_argument = ["2023", "2", "3"]
        result = subprocess_run(bad_argument)

        assert result.returncode == 1


@patch('subprocess.run')
def test_bash_download(mock_run):
    """_summary_
        Mock test that bash download script runs perfectly and retuens download path
    """
    
    # define mock result
    arguments= ["extract.sh" "2023", "2"]
    # define mock return value 
    mock_return_value = subprocess.CompletedProcess(args=["bash", EXTRACT_SH_PATH, *arguments], returncode=0, stdout="./data/ny_taxi_data_2.parquet",stderr="")
    mock_run.return_value = mock_return_value

    args =  ["2023", "2"]
    result = subprocess_run(args)

    # check if successful run
    assert result.returncode == 0

    # check if standard output contains do download path
    assert "./data/ny_taxi_data_2.parquet" in result.stdout


@patch('main.gspread.authorize', return_value=Mock())
def test_class_instance(mock_authorize):
      """_summary_
            - Test data validation
            - Mock test client connection 
      """
      # test input data instantiation
      workbook_test = Workbook("test_wb", "test_sh", 'bestnyah7@gmail.com', "2023", "2")
      assert workbook_test.email == "bestnyah7@gmail.com"
      assert workbook_test.year == "2023"

      assert workbook_test.client is not None

