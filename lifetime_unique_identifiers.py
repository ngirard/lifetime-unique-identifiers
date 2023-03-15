#!/usr/bin/env python3

from base58 import b58encode_int as enc, b58decode_int as dec
from datetime import datetime, timedelta
import argparse
import sys

time_units = [
    (1, "second"),
    (10, "10 seconds"),
    (15, "15 seconds"),
    (20, "20 seconds"),
    (30, "30 seconds"),
    (60, "1 minute"),
    (600, "10 minutes"),
    (900, "15 minutes"),
    (1200, "20 minutes"),
    (1800, "30 minutes"),
    (3600, "1 hour"),
    (43200, "12 hours"),
    (86400, "1 day"),
    (604800, "1 week"),
    (2629743, "1 month"),
    (7889238, "1 trimester"),
    (15778476, "1 semester"),
    (31536000, "1 year"),
]


def integer_to_base58(n):
    return enc(n).decode()

def calculate_lifetime_in_seconds(date_of_birth, life_expectancy):
    dob = datetime.fromisoformat(date_of_birth)
    end_of_life = dob + timedelta(days=(life_expectancy * 365))
    lifetime_in_seconds = int((end_of_life - dob).total_seconds())
    return lifetime_in_seconds

def calculate_seconds_since_epoch(date):
    return int((datetime.fromisoformat(date) - datetime(1970, 1, 1)).total_seconds())

def gen_data(date_of_birth, life_expectancy):
    lifetime_in_seconds = calculate_lifetime_in_seconds(date_of_birth, life_expectancy)
    end_of_life = datetime.fromisoformat(date_of_birth) + timedelta(days=(life_expectancy * 365))
    seconds_since_epoch = calculate_seconds_since_epoch(end_of_life.isoformat())
    for unit_in_seconds, unit_name in time_units:
        max_units_during_lifetime = lifetime_in_seconds // unit_in_seconds
        max_units_since_epoch = seconds_since_epoch // unit_in_seconds
        yield unit_name, max_units_during_lifetime, integer_to_base58(max_units_during_lifetime),  max_units_since_epoch, integer_to_base58(max_units_since_epoch)

def display_lifetime_in_units(date_of_birth, life_expectancy):
    print("Unit         | Lifetime                | Since 1970-01-01      |")
    print("             | Base 10      | Base 58  | Base 10    | Base 58  |")
    for unit_name, card_lifetime, card_lifetime_base58, card_epoch, card_epoch_base58 in gen_data(date_of_birth, life_expectancy):
        print(f"{unit_name:<12} | {card_lifetime:<12} | {card_lifetime_base58:<8} | {card_epoch:<10} | {card_epoch_base58:<8} |")

def main(date_of_birth, life_expectancy):
    display_lifetime_in_units(date_of_birth, life_expectancy)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate lifetime in different units of time')
    parser.add_argument('date_of_birth', type=str, help='Date of birth (ISO 8601 format)')
    parser.add_argument('life_expectancy', type=int, help='Life expectancy in years')
    args = parser.parse_args()
    display_lifetime_in_units(args.date_of_birth, args.life_expectancy)
