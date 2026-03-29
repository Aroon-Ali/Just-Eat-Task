# Just Eat Restaurant Finder

## Overview
This is a Python console application that retrieves restaurant data from the Just Eat API using any UK postcode.

The application filters the returned data to include only restaurants and displays the first 10 results including the name, cuisines, rating, address.
---

## How to Build, Run and Use

### Prerequisites
- Python 3 

### Installation
Install the required dependency/package:

```bash
pip install requests
```

## Running the Application

Run the script:

```bash
python main.py
```

You will then be asked to enter a UK postcode. The program will return the first 10 restaurants for the inputted postcode.

## Assumptions / Unclear Areas

- The API returns a valid response for any postcode input, even if no restaurants are found.
- It was assumed that at least 10 restaurant results would be available, based on the brief stating to display the first 10.
- The API does not provide an explicit "type" field to distinguish restaurants from other establishments.
- Grocery stores were identified and excluded using the `"Groceries"` value within the `cuisines` field.
- Some entries in the `cuisines` field, such as `"Deals"`, `"Collect stamps"` and `"Freebies"`, appear to be metadata rather than actual cuisines, so these were excluded.
- Takeaways and food vendors were treated as restaurants.

## Improvements

- Implement a graphical user interface (GUI) or web interface for a better user experience.
- Add more robust error handling, such as repeated invalid input handling and API failure handling.
- Refactor the code into smaller functions to improve structure and readability.
- Improve handling of API requests so the solution does not rely on manually setting headers.
