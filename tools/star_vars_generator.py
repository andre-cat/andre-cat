import random
from typing import Tuple;

def get_random(start : int, end : int):
    return random.randint(start, end);

def write_file(file_name : str, text: str) -> None:
    file = open(file_name, "w");
    file.write(text);
    file.close();

def generate_dots(quantity : int, range_x: Tuple[int, int], range_y: Tuple[int, int], colors: list[str]) -> str:

    dots = "";

    for i in range(quantity):
        x : int = get_random(range_x[0], range_x[1]);
        y : int = get_random(range_y[0], range_y[1]);

        color = colors[get_random(0, len(colors) - 1)];

        dot = f"{x}px {y}px {color}, ";

        dots += dot;

    dots = dots[:-2] + ";";

    return dots;

little_stars : str = generate_dots(150, (0, 2000), (0, 1000), ['red','crimson']);
medium_stars : str = generate_dots(100, (0, 2000), (0, 1000), ['orange','darkOrange']);
big_stars: str = generate_dots(50, (0, 2000), (0, 1000), ['yellow','gold']);

stars = f"--little-stars: {little_stars}\n--medium-stars: {medium_stars}\n--big-stars: {big_stars}"

write_file("star-vars.txt", stars);