from functools import lru_cache

def moves(h):
    a, b = h
    return (a + 3, b), (a, b + 3), (a * 2, b), (a, b * 2)

@lru_cache(None)
def game(h):
    if sum(h) >= 62:
        return "W"
    elif any(game(m) == "W" for m in moves(h)):
          return "P1"
    elif all(game(m) == "P1" for m in moves(h)):
        return "B1"
    elif any(game(m) == "B1" for m in moves(h)):
        return "P2"
    elif all(game(m) == "P1" or game(m) == "P2" for m in moves(h)):
        return "B2"

# fewrhreg
for s in range(1, 55):
      h = (7, s)
      if game(h) is not None:
          print(game(h), s)