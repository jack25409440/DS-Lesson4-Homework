# DS-Lesson4-Homework
Author: Xiaohui Chen

## Command Line Tasks Answers

1.

The commands are `head chipotle.tsv` and `tail chipotle.tsv`

Each column means the values of the attributes

Column 1 is the value of order_id

Column 2 is the value of quantity

Column 3 is the value of itme_name

Column 4 is the value of choice_description

Each row represents the instances of that type of entity

2.
The command is `cut -f1 chipotle.tsv | sed `1 d`| uniq | wc -l`

The number of orders is 1834

3.
The command is `wc -l chipotle.tsv`

The number of lines is 4623

4.
The commands are:

```
grep "Steak Burrito" chipotle.tsv | wc -l

grep "Chicken Burrito" chipotle.tsv | wc -l

```

The number of Steak Burritos is 368 and the number of Chicken Burritos is 553. Therefore Chicken Burrito is more popular

5.
The commands are:

```
grep "Chicken Burrito" chipotle.tsv | grep "Pinto Beans" | wc -l

grep "Chicken Burrito" chipotle.tsv | grep "Black Beans" | wc -l
```

There are 105 chicken burrito orders with pinto beans and 282 chicken burrito orders with black beans. So the ones with black beans are more popular

6.
The command is `ls -R |grep .[c,t]sv$`

The list of files are:

```
Airline_on_time_west_coast.csv
airlines.csv
bank-additional.csv
bikeshare.csv
chipotle.tsv
citibike_feb2014.csv
drinks.csv
drones.csv
hitters.csv
icecream.csv
imdb_1000.csv
mtcars.csv
NBA_players_2015.csv
ozone.csv
rossmann.csv
rt_critics.csv
sms.tsv
stores.csv
syria.csv
time_series_train.csv
titanic.csv
ufo.csv
vehicles_test.csv
vehicles_train.csv
yelp.csv
2015_station_data.csv
2015_trip_data.csv
2015_weather_data.csv
```

7.
The command should be `grep -r "dictionary" | wc -l`
The total number of the word "dictionary" in the repo is 76

8.
`grep "[c,C]hicken" data/chipotle.tsv | wc -l`

This command counts the number of "chicken" or "Chicken" in the chipotle.tsv file. And the number is 1565
