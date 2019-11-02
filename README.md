# py-gift-exchange

Python Gift Exchange Picker

```sh
       ((\./))
 ,------//^\\------,
 |     //| |\\     |
 |_______| |_______|
 |_______| |_______|
 |       | |       |
 |       | |       |
 '-------===-------'
```

## Installation

```sh
pip install pyge
```

## Basic Usage

Pyge has only one required argument: the path to a csv file with the people who are participating in the gift exchange. An example csv file has been provided: [jazz.csv](https://github.com/sethblack/py-gift-exchange/blob/master/jazz.csv).

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
name, date of birth, sex, "city, state"
```

Any column containing a comma should be quoted with double-quotes for example, `"Austin, TX"`.

The `Date of Birth` field is in `MM/DD/YYYY` format.

`Sex` can be `M`, `F` or `N`.

`City, State` by default only include cities in the United States. See Using Other Country Databases for more information on changing the country.

## Saving History

Pyge saves a historical list of pairings which is used to ensure participants will not be paired for at a minimum of three exchanges. Saving history can be toggled with the `--save-history` and `--no-history` flags. The minimum number of exchanges can be modified with the `--history-length` argument.

## Full Usage

```sh
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

Cities database provided by [https://simplemaps.com/data/us-cities](https://simplemaps.com/data/us-cities)