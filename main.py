import find as find
import filter as filter
import sets as sets
import numpy as np
import pandas as pd
import sys
import json

def main():
    if len(sys.argv) != 3:
        print('Usage: python3 main.py <STEP: find|sets|all> [PARAMS FILEPATH]')
        quit()
    else:
        in_json = sys.argv[2]
        step = sys.argv[1]

        with open(in_json, 'r') as f:
            data = json.load(f)
        
        if data['data_dir'][-1] == "/":
            data['data_dir'] = data['data_dir'][:-1]

        for i, pref in enumerate(data["fg_prefixes"]):
            if pref[-1] == "/":
                data["fg_prefixes"][i] = data["fg_prefixes"][i][:-1]

        for i, pref in enumerate(data["bg_prefixes"]):
            if pref[-1] == "/":
                data["bg_prefixes"][i] = data["bg_prefixes"][i][:-1]

        if step == "find":
            find.main(data)
        elif step == "sets":
            df, primers_with_positions, rev_pos = filter.main(data)
            sets.main(df, primers_with_positions, data)
        elif step == "all":
            find.main(data)
            df, primers_with_positions, rev_pos = filter.main(data)
            sets.main(df, primers_with_positions, rev_pos, data)
        else:
            print("Invalid step. Input is 'find', 'sets', or 'all'.")

if __name__ == "__main__":
    # step = "sets"
    # in_json = '/Users/kaleb/Desktop/Bailey_Lab/code/newswga/params/new_params.json'
    # with open(in_json, 'r') as f:
    #     data = json.load(f)
    # find.main(data)
    # df, primers_with_positions, rev_pos = filter.main(data)
    # sets.main(df, primers_with_positions, rev_pos, data)
    main()
    