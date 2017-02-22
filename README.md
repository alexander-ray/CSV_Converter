# CSV_Converter
### About
Converts `kerbals.csv` file to JSON or XML using python. No libraries are used outside `sys` and `math`. Could theoretically be extended to other csv files if the `getRealValue()` function was removed.

### Usage
1. Download or clone `csv_converter.py` to your local unix-based system--I ran the program using Python 2.7.10
2. Download or clone `kerbals.csv` into the same directory as `csv_converter.py`
3. Run `python csv_converter.py kerbals.csv` to output unformatted JSON
  * To output formatted JSON run `python csv_converter.py kerbals.csv | jsonlint` (must have jsonlint installed on your system)
  * To output formatted XML run `python csv_converter.py kerbals.csv xml`

### Transformation
My solution implemented the "Apply a transform to the 'Courage' and 'Stupidity' columns after they've been read, and before they've been displayed" part of the given problem.

I read the transformation as saying the csv file given contains the "transformed" values for "Courage" and "Stupidity". To transform these values back to the true values I used the equation `true_val = (((arctan(given_val) + (PI/2)) * 100.0) / PI`. 
