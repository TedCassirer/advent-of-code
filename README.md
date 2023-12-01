# Advent of code
Solutions for advent of code

You can run this project with: [Advent of code Data](https://github.com/wimglenn/advent-of-code-data)


## Setup

```sh
poetry install
````





## Run tests
```sh
poetry run pytest
```





## Run
```sh
poetry run aoccas solve -y 2023 -d 1 --submit
```

## Initialize new challenge file
```shell
poetry run aoccas init-challenge -y 2023 -d 1
```

To submit the results you can add the `-s` flag

Set the environment variable `AOC_SESSION` to use your personal input.

Instructions: [How to find the session id](https://github.com/wimglenn/advent-of-code-wim/issues/1)


To run it using the aocd plugin you can run:

```sh
poetry run aoc -y 2023 -d 1
```
