import argparse

parser = argparse.ArgumentParser("Convert age to days")
parser.add_argument("-a", "--age", help="Age to convert to days", required=False)
args = parser.parse_args()

def convert(age):
  try:
    return int(age) * 365
  except ValueError:
    return "Please inform a valid number"


if __name__ == "__main__":
  print(convert(args.age))
