import argparse

parser = argparse.ArgumentParser("Progress Day")
parser.add_argument("-p", "--progress", help="Insert the progress", required=False)
args = parser.parse_args()


def progress_days(progress):
  progress_days = 0
  progress_string = progress.split(" ")
  progress_integer = list(map(int, progress_string))

  while len(progress_integer) > 1:
    compare = []
    compare = progress_integer[:2]

    if compare[1] > compare[0]:
      progress_days+=1
      del(progress_integer[0])
    else:
      del(progress_integer[0])

  return progress_days


if __name__ == "__main__":
  print(progress_days(args.progress))
