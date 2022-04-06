import csv, os

def load_csv(filename, header=True):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        if header:
            columns = [x.strip() for x in next(reader)]
        else:
            columns = [""]
        data = [x[0].strip() for x in reader if x[0].strip()]

        return columns, data

def output_csv(data, filename="output.csv", header=None):
    if os.path.exists(filename):
        mode = "a"
    else:
        mode = "w"
        if header:
            data_cols_num = max(map(len, data))
            assert data_cols_num == len(header)
        else:
            header = [
                "url", 
                "datetime", 
                "status", 
                "redirected_codes",
                "redirected_urls",
                "final_code",
                "final_url",
                ]
    
    with open(filename, mode, newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        if mode == "w":
            writer.writerow(header)
        writer.writerows(data)
        


if __name__ == '__main__':
    cols, data = load_csv("./data.csv")
    print(cols, data)
    data = [[x] for x in range(10,31)]
    output_csv(data, filename="./data.csv")