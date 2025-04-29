import sys 

def parse_arguments():
    args = type('Args', (str,), {'ticker': sys.argv[1] if len(sys.argv) > 1 else None})()
    if not args.ticker:
        raise ValueError("Stock ticker is required. Usage: python scrapper.py <ticker>")
    return args