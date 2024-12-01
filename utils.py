import os
import urllib.request


aoc_session = os.environ.get('AOC_SESSION') 
assert aoc_session, "session cookie is missing"


def download_input(day, year=2024):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cached_path = f"/tmp/aoc-{year}/{day}"
    cached = f"{cached_path}/input.txt"
    if os.path.isfile(cached):
        with open(cached) as file:
            return file.readlines()
    else:
        request = urllib.request.Request(url)
        request.add_header('Cookie', aoc_session)
        with urllib.request.urlopen(request) as response:
            content = response.read().decode('utf-8')
            os.makedirs(cached_path, exist_ok=True)
            with open(cached, 'w') as file:
                file.write(content)
            return content.split("\n")[:-1]
 