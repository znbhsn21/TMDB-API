import os
import json
import argparse
import requests
from rich.console import Console
from rich.table import Table
from rich import print
from requests.exceptions import RequestException, Timeout

def playing_movies():
    my_api_key = "9c0453add6bbc1eb37c373588d2e459d"
    url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={my_api_key}"
    headers = {"accept": "application/json"}
    console = Console()

    try:
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            console.print(f"[red]Error {response.status_code}:[/red] {response.reason}")
            try:
                err_json = response.json()
                console.print(f"[yellow]{err_json.get('status_message', 'Unknown error')}[/yellow]")
            except ValueError:
                pass
            return

        try:
            data = response.json()
        except ValueError:
            console.print("[red]Failed to parse JSON response.[/red]")
            return

        results = data.get("results", [])
        if not results:
            console.print("[yellow]No movies found.[/yellow]")
            return

        movies = sorted(
            [(m.get("title", "N/A"), m.get("release_date", "Unknown"), m.get("overview", "No description")) for m in results],
            key=lambda x: x[0].lower()
        )

        table = Table(title="Movie Summary")
        table.add_column("Name", justify="right", style="cyan", no_wrap=True)
        table.add_column("Date", style="magenta")
        table.add_column("Description", style="green")

        for title, date, overview in movies:
            table.add_row(title, date, overview)

        console.print(table)

    except Timeout:
        console.print("[red]Request timed out. Please try again later.[/red]")
    except RequestException as e:
        console.print(f"[red]Network error:[/red] {e}")
    except Exception as e:
        console.print(f"[red]Unexpected error:[/red] {e}")

def popular_movies():
    my_api_key = "9c0453add6bbc1eb37c373588d2e459d"
    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page=1&api_key={my_api_key}"
    headers = {"accept": "application/json"}
    console = Console()

    try:
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            console.print(f"[red]Error {response.status_code}:[/red] {response.reason}")
            try:
                err_json = response.json()
                console.print(f"[yellow]{err_json.get('status_message', 'Unknown error')}[/yellow]")
            except ValueError:
                pass
            return

        try:
            data = response.json()
        except ValueError:
            console.print("[red]Failed to parse JSON response.[/red]")
            return

        results = data.get("results", [])
        if not results:
            console.print("[yellow]No movies found.[/yellow]")
            return

        movies = sorted(
            [(m.get("title", "N/A"), m.get("release_date", "Unknown"), m.get("overview", "No description")) for m in results],
            key=lambda x: x[0].lower()
        )

        table = Table(title="Movie Summary")
        table.add_column("Name", justify="right", style="cyan", no_wrap=True)
        table.add_column("Date", style="magenta")
        table.add_column("Description", style="green")

        for title, date, overview in movies:
            table.add_row(title, date, overview)

        console.print(table)

    except Timeout:
        console.print("[red]Request timed out. Please try again later.[/red]")
    except RequestException as e:
        console.print(f"[red]Network error:[/red] {e}")
    except Exception as e:
        console.print(f"[red]Unexpected error:[/red] {e}")

def top_movies():
    my_api_key = "9c0453add6bbc1eb37c373588d2e459d"
    url = f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1&api_key={my_api_key}"
    headers = {"accept": "application/json"}
    console = Console()

    try:
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            console.print(f"[red]Error {response.status_code}:[/red] {response.reason}")
            try:
                err_json = response.json()
                console.print(f"[yellow]{err_json.get('status_message', 'Unknown error')}[/yellow]")
            except ValueError:
                pass
            return

        try:
            data = response.json()
        except ValueError:
            console.print("[red]Failed to parse JSON response.[/red]")
            return

        results = data.get("results", [])
        if not results:
            console.print("[yellow]No movies found.[/yellow]")
            return

        movies = sorted(
            [(m.get("title", "N/A"), m.get("release_date", "Unknown"), m.get("overview", "No description")) for m in results],
            key=lambda x: x[0].lower()
        )

        table = Table(title="Movie Summary")
        table.add_column("Name", justify="right", style="cyan", no_wrap=True)
        table.add_column("Date", style="magenta")
        table.add_column("Description", style="green")

        for title, date, overview in movies:
            table.add_row(title, date, overview)

        console.print(table)

    except Timeout:
        console.print("[red]Request timed out. Please try again later.[/red]")
    except RequestException as e:
        console.print(f"[red]Network error:[/red] {e}")
    except Exception as e:
        console.print(f"[red]Unexpected error:[/red] {e}")

def upcoming_movies():
    my_api_key = "9c0453add6bbc1eb37c373588d2e459d"
    url = f"https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1&api_key={my_api_key}"
    headers = {"accept": "application/json"}
    console = Console()

    try:
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            console.print(f"[red]Error {response.status_code}:[/red] {response.reason}")
            try:
                err_json = response.json()
                console.print(f"[yellow]{err_json.get('status_message', 'Unknown error')}[/yellow]")
            except ValueError:
                pass
            return

        try:
            data = response.json()
        except ValueError:
            console.print("[red]Failed to parse JSON response.[/red]")
            return

        results = data.get("results", [])
        if not results:
            console.print("[yellow]No movies found.[/yellow]")
            return

        movies = sorted(
            [(m.get("title", "N/A"), m.get("release_date", "Unknown"), m.get("overview", "No description")) for m in results],
            key=lambda x: x[0].lower()
        )

        table = Table(title="Movie Summary")
        table.add_column("Name", justify="right", style="cyan", no_wrap=True)
        table.add_column("Date", style="magenta")
        table.add_column("Description", style="green")

        for title, date, overview in movies:
            table.add_row(title, date, overview)

        console.print(table)

    except Timeout:
        console.print("[red]Request timed out. Please try again later.[/red]")
    except RequestException as e:
        console.print(f"[red]Network error:[/red] {e}")
    except Exception as e:
        console.print(f"[red]Unexpected error:[/red] {e}")

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
