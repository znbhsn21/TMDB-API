import os
import json
import argparse
import requests
from rich.console import Console
from rich.table import Table
from rich import print

file_path = "movies.json"

def playing_movies():
    my_api_key = "9c0453add6bbc1eb37c373588d2e459d"
    url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={my_api_key}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()

    movies = sorted([(movie["title"], movie["release_date"], movie["overview"]) for movie in data.get("results", [])],
             key=lambda x: x[0].lower())

    table = Table(title="Movie Summary")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Date", style="magenta")
    table.add_column("Description", style="green")

    for title, date, overview in movies:
        table.add_row(
            title, 
            date, 
            overview)

    console = Console()
    console.print(table)

def popular_movies():
    my_api_key = "9c0453add6bbc1eb37c373588d2e459d"
    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page=1&api_key={my_api_key}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()

    movies = sorted([(movie["title"], movie["release_date"], movie["overview"]) for movie in data.get("results", [])],
             key=lambda x: x[0].lower())

    table = Table(title="Movie Summary")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Date", style="magenta")
    table.add_column("Description", style="green")

    for title, date, overview in movies:
        table.add_row(
            title, 
            date, 
            overview)

    console = Console()
    console.print(table)

def top_movies():
    my_api_key = "9c0453add6bbc1eb37c373588d2e459d"
    url = f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1&api_key={my_api_key}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()

    movies = sorted([(movie["title"], movie["release_date"], movie["overview"]) for movie in data.get("results", [])],
             key=lambda x: x[0].lower())

    table = Table(title="Movie Summary")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Date", style="magenta")
    table.add_column("Description", style="green")

    for title, date, overview in movies:
        table.add_row(
            title, 
            date, 
            overview)

    console = Console()
    console.print(table)

def upcoming_movies():
    my_api_key = "9c0453add6bbc1eb37c373588d2e459d"
    url = f"https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1&api_key={my_api_key}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()

    movies = sorted([(movie["title"], movie["release_date"], movie["overview"]) for movie in data.get("results", [])],
             key=lambda x: x[0].lower())

    table = Table(title="Movie Summary")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Date", style="magenta")
    table.add_column("Description", style="green")

    for title, date, overview in movies:
        table.add_row(
            title, 
            date, 
            overview)

    console = Console()
    console.print(table)

parser = argparse.ArgumentParser(description="TMDB CLI")
parser.add_argument(
    "--type",
    choices=["playing", "upcoming", "popular", "top"],
    help="Type of movies to display")

args = parser.parse_args()

if args.type == "playing":
    playing_movies()
elif args.type == "popular":
    popular_movies()
elif args.type == "top":
    top_movies()
elif args.type == "upcoming":
    upcoming_movies()
