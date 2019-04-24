import os
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    your_series = pd.DataFrame(pd.Series([1,2,3,4]))
    df = pd.DataFrame({
        "Integers": [1, 23, 456, 7890],
        "Strings": ['hello', 'pandas', 'world', '!'],
        "Floats": [1.23, 23.5, 45.6, 7.890],
        "Booleans": [True, False, True, False]
    })
    integers = pd.DataFrame(df["Integers"])
    two_columns = df[["Integers","Strings"]]
    desc=df.describe(include='all')
    your_list = [4, 'softdev', 12.5, False]
    list_df = pd.DataFrame([your_list], columns=['Integers', 'Strings', 'Floats', 'Booleans'])
    new_df = pd.DataFrame({
        "Integers": [1, 23, 456, 7890],
        "Strings": ['hello', 'pandas', 'world', '!'],
        "Floats": [1.23, 23.5, 45.6, 7.890],
        "Booleans": [True, False, True, False]
    })
    new_df = new_df.append(list_df, ignore_index=True)
    csv_path = os.path.join('uscities.csv')
    csv_df = pd.read_csv(csv_path, delimiter=",")
    head = csv_df.head(10)
    shape = csv_df.shape
    tail = csv_df.tail()
    max = pd.DataFrame(csv_df.max())
    min = pd.DataFrame(csv_df.min())
    median = pd.DataFrame(csv_df.median())
    sample = csv_df.sample(3)
    asc = csv_df.head(10).sort_values('density')
    dec = csv_df.head(10).sort_values('density',ascending=False)
    new_csv_df = csv_df.dropna()
    new_shape = new_csv_df.shape
    lat = new_csv_df[new_csv_df['lat'] > 45].head(10)
    ny = new_csv_df[['city','state_id']].query('state_id == "NY"').head(20)
    return render_template('index.html', series=your_series.to_html(), data=df.to_html(), integers=integers.to_html(), two_columns=two_columns.to_html(), stat=desc.to_html(), list_df=list_df.to_html(), new_df=new_df.to_html(), head=head.to_html(), shape=shape, tail=tail.to_html(), max=max.to_html(), min=min.to_html(), median=median.to_html(), sample=sample.to_html(), asc=asc.to_html(), dec=dec.to_html(), new_shape=new_shape, lat=lat.to_html(), ny=ny.to_html())

if __name__ == "__main__":
    app.debug = True
    app.run()
