import argparse
import importlib


def run(day):
    # Run the code for the specified day
    module = importlib.import_module(f"{day:02d}")
    part_a = module.part_a()

    print(f"Part A: {part_a}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int, help="Specify the day")
    args = parser.parse_args()

    run(args.day)
