import sys
import shutil
import os

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python init.py <year>")

    year = sys.argv[1]

    if not year.isdigit() or not (2015 <= int(year) <= 2100):
        sys.exit("Invalid year.")

    os.mkdir(year)

    for i in range(25):
        new_dir_path = f"{year}/day{i + 1}"
        shutil.copytree("template", new_dir_path)

    print(f"Directory {year} created.")
