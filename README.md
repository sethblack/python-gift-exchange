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

Pyge has only one required argument and that is the path to a csv file with the people who are participating in the gift exchange. An example csv file has been provided: jazz.csv.

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

Cities database provided by [https://simplemaps.com/data/us-cities](https://simplemaps.com/data/us-cities)