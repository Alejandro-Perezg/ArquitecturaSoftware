import pytest, os
from patterns.csv_utils import parse_file
from patterns.web_report import create_file


@pytest.fixture
def csv_file_path(tmpdir):
    csv_content = "error,TaxiID,pick_up_time,drop_of_time,passenger_count,trip_distance,tolls_amount\n1,23,2023-05-14,2023-05-14,4,2.3,12.3"
    csv_file = tmpdir.join("test.csv")
    csv_file.write(csv_content)
    return str(csv_file)

def test_load_csv(csv_file_path):
    rides = parse_file(csv_file_path)
    assert len(rides) == 2
    assert rides[0] == {"error": "1", "TaxiID": "23", "pick_up_time": "2023-05-14","drop_of_time":"2023-05-14","passenger_count":"4","trip_distance":"2.3","tolls_amount":"12.3"}
    #assert rides[1] == {"error": "1", "taxi_id": "23", "pick_up_time": "2023-05-14","drop_of_time":"2023-05-14","passenger_count":"4","trip_distance":"2.3","tolls_amount":"12.3"}


@pytest.fixture
def output_file_path(tmpdir):
    output_file = tmpdir.join("financial-report.html")
    return str(output_file)

def test_file_creation(output_file_path):
    create_file(output_file_path)
    assert os.path.isfile(output_file_path)