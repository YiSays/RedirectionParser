from utils.CSVLoader import load_csv, output_csv
from utils.HTTPRequestParser import async_parse

# Argument Parser
import argparse

argparser = argparse.ArgumentParser(
    description="An async-web-scraper to parse redirection information",
    allow_abbrev=True,
)

argparser.add_argument(
    "filepath",
    action="store",
    type=str,
    help="csv file path, e.g. 'data.csv' or './folder/data.csv'.",
)
argparser.add_argument(
    "-o",
    "--output",
    action="store",
    type=str,
    default="output.csv",
    # required=True,
    help="csv file to save, the default file is 'output.csv' at local folder."
)
argparser.add_argument(
    "-s",
    "--size",
    action="store",
    default=50,
    type=int,
    help="batch size for async requests, default parsing 50 urls per batch."
)

argparser.add_argument(
    "-t",
    "--test-run",
    action="store_true",
    help="run test of async web requests"
)

args = argparser.parse_args()


def main():
    _, urls = load_csv(args.filepath)
    total_num = len(urls)
    print(f"\nTotal {total_num} urls were loaded for http request parsing.\n")

    for i in range(0, total_num, args.size):
        j = min(i+args.size, total_num)
        print("=="*20)
        print(f"BATCH JOB START: {i+1}/{total_num} url to {j}/{total_num} url")
        batch = urls[i:j]
        data = async_parse(batch)
        output_csv(data, filename=args.output)

def test_run():
    urls = [
        "http://github.com",
        "http://google.com",
        "http://python.org",
    ]
    print(async_parse(urls))    

if __name__ == "__main__":
    from time import perf_counter
    print(args)
    start = perf_counter()
    if args.test_run:
        test_run()
    else:
        main()
    print(f"Parsing job finished in {perf_counter()-start:.2f}s.")
    print(f"Please copy the output file at '{args.output}', and delete afterwards.")