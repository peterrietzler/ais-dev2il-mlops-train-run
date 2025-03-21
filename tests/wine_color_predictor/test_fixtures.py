import pytest

@pytest.fixture
def winequality_test_data_dir(tmp_path) -> str:
    # Create mock data directory
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    # Create mock red wine data
    red_wine_data = "fixed acidity;volatile acidity;citric acid;residual sugar;chlorides;free sulfur dioxide;total sulfur dioxide;density;pH;sulphates;alcohol;quality\n7.4;0.7;0;1.9;0.076;11;34;0.9978;3.51;0.56;9.4;5"
    red_wine_file = data_dir / "winequality-red.csv"
    red_wine_file.write_text(red_wine_data)

    # Create mock white wine data
    white_wine_data = "fixed acidity;volatile acidity;citric acid;residual sugar;chlorides;free sulfur dioxide;total sulfur dioxide;density;pH;sulphates;alcohol;quality\n7;0.27;0.36;20.7;0.045;45;170;1.001;3;0.45;8.8;6"
    white_wine_file = data_dir / "winequality-white.csv"
    white_wine_file.write_text(white_wine_data)

    return str(data_dir)