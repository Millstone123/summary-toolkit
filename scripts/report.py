#!/usr/bin/env python3
"""Generate a project summary report."""
import argparse, json, sys

try:
    from summary_formatter.formatter import format_row
    USE_PKG = True
except ImportError:
    USE_PKG = False

def main():
    parser = argparse.ArgumentParser(description="Generate project summary")
    parser.add_argument("--input", required=True, help="Input JSON stats")
    parser.add_argument("--output", required=True, help="Output file")
    args = parser.parse_args()

    with open(args.input) as fh:
        data = json.load(fh)

    lines = ["# Project Summary", ""]
    for k, v in data.items():
        if USE_PKG:
            lines.append(format_row([k, str(v)], [20, 30]))
        else:
            lines.append(f"- {k}: {v}")

    with open(args.output, "w") as out:
        out.write("\n".join(lines) + "\n")
    print("Summary written to", args.output)

if __name__ == "__main__":
    main()
