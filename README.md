# py-gift-exchange

Holiday Gift Exchange Picker

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

Pyge has only one required argument and that is the path to a csv file with the people who are participating in the gift exchange. An example csv file has been provided: [jazz.csv](https://github.com/sethblack/py-gift-exchange/blob/master/jazz.csv).

```sh
$ pyge /path/to/people.csv
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
The `Date of Birth` field is in MM/DD/YYYY format.
`Sex` can be `M`, `F` or `N`.
`City, State` by default only include cities in the United States. See Using Other Country Databases for more information on changing the country.

---

Cities database provided by [https://simplemaps.com/data/us-cities](https://simplemaps.com/data/us-cities)