from utils.CSVLoader import load_csv, output_csv
from utils.HTTPRequestParser import async_parse

# Argument Parser
import argparse

argparser = argparse.ArgumentParser(allow_abbrev=True)
argparser.add_argument(
    "filepath",
    action="store",
    type=str,
    # required=True,
)
argparser.add_argument(
    "-o",
    "--output",
    action="store",
    type=str,
    default="output.csv"
    # required=True
)
argparser.add_argument(
    "--async-size",
    action="store",
    default=50,
    type=int
)

args = argparser.parse_args()


def main():
    _, urls = load_csv(args.filepath)
    total_num = len(urls)
    print(f"total {total_num} urls were loaded for http request parsing.\n")

    for i in range(0, total_num, args.async_size):
        j = min(i+args.async_size, total_num)
        print(f"batch parsing: {i+1}/{total_num} url to {j}/{total_num} url")
        batch = urls[i:j]
        data = async_parse(batch)
        output_csv(data)
    print(args)
    print(data)

if __name__ == "__main__":
    main()