from wine_color_predictor.train import load_winequality_data
from test_fixtures import winequality_test_data_dir

def test_load_winequality_data(winequality_test_data_dir):
    # Load the wine quality data
    df = load_winequality_data(data_dir=winequality_test_data_dir)

    # Assert the dataframe contains data from both red and white wines
    assert len(df) == 2, "The dataframe should contain 2 rows (1 red, 1 white wine)"
    assert "is_red" in df.columns, "The dataframe should contain the 'is red' column"

    # Assert the 'is_red' column is correctly populated
    assert set(df["is_red"].unique()) == {0, 1}, "The 'is red' column should only contain the values 0 and 1"
