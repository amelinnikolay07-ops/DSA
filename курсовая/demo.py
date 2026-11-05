"""Пример запуска Trie без графического интерфейса."""

from trie import Trie


def print_tree(node, indent="", char="корень"):
    """Вывести дерево в консоль (удобно для небольшого словаря)."""
    label = char
    if node.is_end:
        label += f"  [конец слова, частота {node.frequency}]"
    print(indent + label)

    for next_char in sorted(node.children):
        print_tree(node.children[next_char], indent + "    ", next_char)


def main():
    trie = Trie()
    trie.insert("кот", 2)
    trie.insert("котик", 5)
    trie.insert("кошка", 3)
    trie.insert("дом", 1)

    print("СТРУКТУРА TRIE")
    print_tree(trie.root)

    print("\nПРОВЕРКА ОПЕРАЦИЙ")
    print("Есть слово 'кот':", trie.search("кот"))
    print("Есть слово 'ко':", trie.search("ко"))
    print("Есть префикс 'ко':", trie.starts_with("ко"))
    print("Частота 'котик':", trie.get_frequency("котик"))
    print("Подсказки для 'ко':", trie.autocomplete("ко"))

    visited, found = trie.search_path("котик")
    print("Путь поиска 'котик':", visited)
    print("Слово найдено:", found)


if __name__ == "__main__":
    main()
