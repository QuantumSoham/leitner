from quests import cards
from random import randint

def main():
  slots = (list(cards.items()), [], [])
  box_chance_mul = [4, 2, 1]
  card_stats = {q: {"displayed": 0, "incorrect": 0} for q, _ in cards.items()}

  while True:
    wts = [len(i) * box_chance_mul[idx] for idx, i in enumerate(slots)]
    f = randint(1, sum(wts)) - 1
    box_idx = 0
    a = 0
    n = 0
    for idx, i in enumerate(wts):
      a += i
      if f < a:
        box_idx = idx
        n = f - a + i
        break
    box = slots[box_idx]
    q, a = box.pop(n // box_chance_mul[box_idx])
    print(chr(27) + "[2J")
    print(q)
    print("-" * 4)
    user_answer = input("Answer: ")
    print("=" * 5)

    card_stats[q]["displayed"] += 1
    if user_answer.lower() != a.lower():
      card_stats[q]["incorrect"] += 1

    o = input(f"The answer was: {a}\nWere you correct? (Y/n/exit): ")
    print("=" * 5)
    if not o or o[0].lower() == "y":
      box_idx = min(box_idx + 1, len(slots) - 1)
    elif o[0].lower() == "n":
      box_idx = max(box_idx - 1, 0)
    else:
      break
    slots[box_idx].append((q, a))
    if len(cards) == len(slots[-1]):
      print(f"You have memorised all {len(cards)} cards")
      incorrect_percentages = {q: (incorrect / displayed) * 100 for q, (displayed, incorrect) in card_stats.items()}
      top_five_wrong = sorted(incorrect_percentages.items(), key=lambda x: x[1], reverse=True)[:5]

      print("\nCards with Highest Wrong Answer Percentage:")
      for q, percentage in top_five_wrong:
        print(f"- {q}: {percentage:.2f}%")

      k = input("Exit? (N/y): ")
      if k and k[0].lower() == "y":
        break

if __name__ == "__main__":
  main()
