
# search_key_word_count = int(input("검색어 갯수를 입력해주세요 : "))
# search_key_word = input("검색을 원하는 브랜드를 입력해주세요")
# brands = [search_key_word for brand_name in range(search_key_word_count)]
# print(brands)

search_key_word_count = int(input("검색어 갯수를 입력해주세요: "))
brands = [input("검색을 원하는 브랜드를 입력해주세요: ") for _ in range(search_key_word_count)]
print(brands)
print(brands[0])