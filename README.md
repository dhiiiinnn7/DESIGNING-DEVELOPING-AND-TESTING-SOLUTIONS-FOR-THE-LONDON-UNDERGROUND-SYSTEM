# DESIGNING-DEVELOPING-AND-TESTING-SOLUTIONS-FOR-THE-LONDON-UNDERGROUND-SYSTEM

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Navigate to the Project Directory](#navigate-to-the-project-directory)
  - [Install the Required Packages](#install-the-required-packages)
- [Usage](#usage)
- [Data Structures and Algorithms](#data-structures-and-algorithms)
- [Performance Evaluation](#performance-evaluation)
- [Testing](#testing)
- [Limitations](#limitations)
- [License](#license)

## Overview

This project is a London Underground Journey Planner application developed in Python. It uses Dijkstra’s Algorithm to find the shortest path between two stations, considering potential closures of stations or train lines. The project also features live arrival times and visual representations of journey data.

## Features

- **Shortest Path Calculation**: Uses Dijkstra’s Algorithm to determine the quickest route between two stations.
- **Station and Line Closures**: Accounts for closed stations and train lines, providing alternative routes.
- **Live Arrival Time**: Displays the expected arrival time at the destination.
- **Data Visualization**: Generates histograms of journey times using Matplotlib.

## Installation

### Clone the Repository
```sh
git clone https://github.com/dhiiiinnn7/DESIGNING-DEVELOPING-AND-TESTING-SOLUTIONS-FOR-THE-LONDON-UNDERGROUND-SYSTEM.git
```

### Navigate to the Project Directory
```sh
cd London Underground - Algorithm.py
```

### Install the required packages
```sh
pip install pandas matplotlib colorama
```

## Usage
Ensure the data file London Underground Data.xlsx is in the project directory.

### Run the Python script
```sh
python LondonUnderground_Algorithm.py
```

Follow the on-screen prompts to enter the starting point and destination. Optionally, specify closed stations or lines.

## Data Structures and Algorithms

- Dijkstra’s Algorithm: Chosen for its efficiency in finding shortest paths with positive weights, suitable for our dataset of TFL stations.
- Dictionary: Used for fast lookup of stations and their connections.
- Arrays: Store visited nodes to manage the journey's progress.

## Performance Evaluation

The project successfully integrates the Excel data with Dijkstra’s Algorithm to calculate shortest paths and handles station closures effectively. Challenges included linking the data to the algorithm and handling various edge cases, which were overcome through iterative testing and debugging.

## Testing

Several test cases were performed to validate the functionality:

- Shortest route from Stratford to Baker Street.
- Time taken for a journey from Barking to Whitechapel.
- Alternative route when Mile End station is closed.
- Route using the Jubilee line when the Central line is closed.
- Live arrival time for various journeys.

## Limitations

- Single Line Stations: Stations served by only one line cause errors if that line is closed.
- Output Direction: The journey path is printed backwards due to the algorithm's implementation.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
