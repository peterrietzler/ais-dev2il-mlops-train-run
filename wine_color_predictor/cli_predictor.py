import click 
import pandas
import sys
import train

@click.command()
@click.argument('input_file', type=click.Path(exists=True, dir_okay=False))
def predict(input_file):
    data = train.load_winequality_data()
    model = train.train_model(data)
    input_data = pandas.read_csv(input_file, delimiter=";")
    predictions = model.predict(input_data)
    input_data['is_red'] = predictions
    input_data.to_csv(sys.stdout, index=False, sep=";")
    pass


if(__name__ == '__main__'):
    predict()