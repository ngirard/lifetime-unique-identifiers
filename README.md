# Lifetime unique identifiers

A program that helps evaluating different strategies for forming compact, human-friendly systems of unique identifiers for the various items that an individual will encounter during their lifetime.

## Purpose

The purpose of this program is to provide a tool for evaluating different strategies for forming compact, human-friendly systems of unique identifiers for the various items that an individual will encounter during their lifetime. The program calculates and displays, for each unit of time, the maximum number of units during the person's lifetime in both base 10 and base 58 encoding. This can help to inform decisions about the best approach for creating unique identifiers for different types of items, based on the criteria of compactness, human-friendliness, and efficiency, among others.

### Why Base58?

Base58 encoding is a good choice in this context because it provides a compact and human-friendly representation of data. Unlike base 10 or hexadecimal encoding, base 58 encoding uses a reduced set of characters that are easy to distinguish and less likely to be confused with each other. This makes it easier for humans to read and type the encoded data, and reduces the risk of typos and errors.

In addition, base 58 encoding is efficient to compute and store, making it well-suited for use in systems where performance is a concern. It is also flexible, allowing for easy updates or modifications to the encoded data if needed.

The combination of compactness, human-friendliness, efficiency, and flexibility make base 58 encoding a good choice for this its use in generating compact, human-friendly unique identifiers.

## Example

```sh
python3 lifetime_unique_identifiers.py 1990-01-01 100
```
```
Unit         | Lifetime                | Since 1970-01-01      |
             | Base 10      | Base 58  | Base 10    | Base 58  |
second       | 3153600000   | 5og2Qo   | 3784752000 | 6mSquq   |
10 seconds   | 315360000    | UsJYP    | 378475200  | aSnVV    |
...
1 hour       | 876000       | 5VQT     | 1051320    | 6PXD     |
...
```

This reads as follows:

- *For the kinds of items that can arise once every 10 seconds during a person's lifetime, a system that uses base 58 encoding to generate unique identifiers for these items based on the date and time of their creation, expressed as the number of 10-second units since the Unix epoch (or since that person's date of birth), needs only __5 characters__ to uniquely identify each item.*

- *For the kinds of items that can arise once every hour during a person's lifetime, only __4 characters__ suffice to uniquely identify each item.*


## Usage

The program takes two arguments as input:

- the date of birth of a person in any ISO 8601 form, and
- their life expectancy in years.

It then calculates and displays, for each unit of time (e.g. seconds, minutes, hours, days, etc.), the maximum number of units during the person's lifetime in both base 10 and base 58 encoding.


## Requirements

- Python 3.x
- `base58` module from PyPI


## Contribute

Feel free to contribute to this project by submitting bug reports, feature requests, or by creating pull requests with new features and improvements.

