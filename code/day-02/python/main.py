import argparse

parser = argparse.ArgumentParser("Calculate Tribonacci")
parser.add_argument("-n", "--numbers", help="Please digit 3 random numbers separate by comma", required=False)
args = parser.parse_args()


def calcTribonacci(numbers):
  tribonacci = numbers.split(",")

  tribonacci_int = convertStrArrayToIntAray(tribonacci)

  tribonacci.append(str(sum(tribonacci_int[-3:])))

  tribonacci_int = convertStrArrayToIntAray(tribonacci)

  tribonacci.append(str(sum(tribonacci_int[-3:])))

  return tribonacci

def convertStrArrayToIntAray(str_array):
  int_array = list(map(int, str_array))
  return int_array

if __name__ == "__main__":
  print(calcTribonacci(args.numbers))
