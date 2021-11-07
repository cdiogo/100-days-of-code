import argparse

parser = argparse.ArgumentParser("Find sock pairs")
parser.add_argument("-d", "--drawer", help="Drawer to look for sock pairs")
args = parser.parse_args()

def find_sock_pairs(drawer):
  socks = list(drawer)
  pair_count = 0

  for key in range(0, len(socks)):
    sock = socks[key]

    for drawer in socks[key+1:len(socks)]:
      if sock == drawer:
        pair_count+=1
        break
  return pair_count

if __name__ == "__main__":
  print(find_sock_pairs(args.drawer))
