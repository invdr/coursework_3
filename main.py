from config.utils import *
from config.config import *

original_list = load_file(PATH)
sorted_list = get_sorted_list(original_list)

for line in sorted_list[0:5]:
    transaction_description = line["description"]
    transaction_date = line["date"]

    print(transaction_date, transaction_description)
    if transaction_description == "Открытие вклада":
        print(encoding_to(line))
    else:
        print(encoding_to(line), '->', encoding_from(line))
    print(get_amount(line))
    print()
