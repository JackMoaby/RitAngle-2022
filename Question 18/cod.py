def main(m):
    total_cards = 1024
    number_of_piles = total_cards / (2**m)
    cards_per_pile = total_cards / number_of_piles

    # Division time
    division_time = 1000

    # Sort time
    sort_time = 0
    for a in range(int(cards_per_pile)):
        sort_time += (a + 1)
    sort_time = sort_time * number_of_piles

    # Collate time
    collate_time = 0
    current_total_piles = int(number_of_piles)

    while current_total_piles != 1:
        collate_time += total_cards + 1
        current_total_piles = current_total_piles / 2

    # CS to S converter
    total_time = division_time + sort_time + collate_time
    print(total_time, "cs")
    print(" -> ", total_time * 0.01, "s")


for x in range(10):
    main(x + 1)
