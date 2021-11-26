# Python Gift Exchange Picker

[![The Rest by taleas.com](https://www.taleascomic.com/static/images/comics/the-rest-of-my-presents.jpg "The Rest by taleas.com")](https://www.taleascomic.com/comics/the-rest-of-the-christmas-presents.html)

My wife is in charge of our families' annual Secret Santa Gift Exchange. Because she, unfortunately, knows about my background in math and computer science her requirements have become more extreme. A hat containing folded pieces of paper with hand-written names is no longer sufficient. Python Gift Exchange Picker (pyge) is my third and best implementation of my wife's requirements:

- It must match each person to a different person.
- The match should not be in the same household.
- The match should not be the same gender.
- The match should not be in the same age group.
- The match must not happen again for at least three years.

To accomplish this, pyge imports a list of participants along with their feature sets and transforms each participant's feature set into numerical values. Each value is then vectorized and a pairwise euclidean distance between each participant is computed; this can be represented as either a graph or a matrix - I chose a matrix. The distances are then multiplied by a per-participant "qualifier" coefficient and the results are used to build a weighted distribution. The pairs of participants are then randomly matched using the weighted distribution until either all participants have been matched or no matches can be made. If no matches can be made and there are still participants pyge will backtrack until all participants can be successfully matched or it is discovered that it is impossible to match the given set of participants.

If you're interested, you can read a more detailed description [here](https://www.sethserver.com/python/secret-santa-gift-exchange.html).

## Installation

```sh
pip install pyge
```

## Basic Usage

Pyge has only one required argument: the path to a csv file containing the people who are participating in the gift exchange. An example csv file, [jazz.csv](https://github.com/sethblack/py-gift-exchange/blob/master/jazz.csv) has been provided.


```sh
$ pyge /path/to/jazz.csv
Herbie Hancock, Billie Holiday
Ella Fitzgerald, Herbie Hancock
Charlie Parker, Nina Simone
Nina Simone, Bill Evans
Miles Davis, Duke Ellington
John Coltrane, Sarah Vaughan
Sarah Vaughan, Louis Armstrong
Louis Armstrong, Ella Fitzgerald
Billie Holiday, Charlie Parker
Duke Ellington, John Coltrane
Dizzy Gillespie, Miles Davis
Bill Evans, Dizzy Gillespie
```

### Input CSV File Format

```
name, date of birth, sex, "city, state or province or territory"
```

Any column containing a comma should be quoted with double-quotes, for example, `"Austin, TX"`.

The `Date of Birth` field is in `MM/DD/YYYY` format.

`Sex` can be `M`, `F` or `N`.

`City` by default only includes cities in the United States. See [Using Other Country Databases](https://github.com/sethblack/py-gift-exchange#using-other-country-databases) for more information on changing the country.

## Saving History

Pyge saves a historical list of pairings which is used to ensure participants will not be paired for at a minimum of three exchanges. Saving history can be toggled with the `--save-history` and `--no-history` flags. The minimum number of exchanges can be modified with the `--history-length` argument.

## Using Other Country Databases

You can pass a different city weight database file by using the `--citydb` argument. The city weight database is a csv file in the following format:

```
city, state or province or territory, normalized latitude, normalized longitude
```

Where normalized latitude and longitude are the values normalized between -1 and +1 (divided by 180).

## Full Usage

```
usage: pyge [-h] [-s] [-n] [-c citydb] [-l historylength] file

Generates a list of people pairings for a holiday gift exchange.

positional arguments:
  file                  path to the csv containing a list of people who want
                        to be part of the celebration

optional arguments:
  -h, --help            show this help message and exit
  -s, --save-history    save a history file of matches
  -n, --no-history      do not save a history file of matches
  -c citydb, --citydb citydb
                        path to city csv for distance calculations
  -l historylength, --history-length historylength
                        number of cycles before people can be paired again
```

---

Cities database provided by [https://simplemaps.com/data/us-cities](https://simplemaps.com/data/us-cities).