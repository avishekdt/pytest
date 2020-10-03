# pytest

pytest -v -s PytestPackage/test_google.py --html=report.html
pytest -v -s PytestPackage/test_google_fixture.py --html=report.html
pytest -v -s PytestPackage/test_fixture_classes.py --html=report.html
pytest -v -s PytestPackage/test_fixture_params.py --html=report.html
pytest -v -s PytestPackage/test_fixture_params.py -n 2 --html=report.html
pytest -v -s PytestPackage/test_fixture_params.py -n 4 --html=report.html
pytest -v -k total --html=report.html
pytest -v -k total --html=report.html
pytest -v -s PytestPackage/test_fixture_params.py -n 4 --html=report.html
