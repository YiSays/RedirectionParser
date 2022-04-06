from utils.CSVLoader import load_csv, output_csv
from utils.HTTPRequestParser import async_parse
import argparse


def main():
    header, urls = load_csv()
    total_num = len(urls)
    print(f"total {total_num} urls were loaded for http request parsing.")

    
    data = async_parse(urls)
    output_csv(data)

if __name__ == "__main__":
    main()