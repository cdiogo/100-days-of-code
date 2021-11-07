import argparse

parser = argparse.ArgumentParser("Barbecue Skewers")
parser.add_argument("-s", "--skewers", help="Insert the barbecue skewers", required=False)
args = parser.parse_args()


def skewers_identificator(barbecure_skewers):
  veggie, non_veggie = 0, 0
  for skewer in barbecure_skewers.split(" "):
    if "-x" in skewer:
      non_veggie+=1
    else:
      veggie+=1
  return [veggie, non_veggie]

if __name__ == "__main__":
  print(skewers_identificator(args.skewers))
