from config.utils import *
from config.config import *

listt = load_file(PATH)
normal_list = get_normal_list(listt)

for line in normal_list:
    transaction_description = line["description"]
    print(get_date(line), transaction_description)
    if transaction_description == "Открытие вклада":
        print(encoding_to(line))
    else:
        print(encoding_from(line), '->', encoding_from(line))
    print(get_ammount(line))
    print()