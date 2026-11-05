"""Базовая реализация префиксного дерева (Trie) для курсовой работы."""


class TrieNode:
    """Узел дерева: переходы по символам и информация о конце слова."""

    def __init__(self):
        self.children = {}   # Символ -> следующий узел TrieNode
        self.is_end = False  # True, если здесь заканчивается слово
        self.frequency = 0  # Сколько раз было добавлено это слово


class Trie:
    """Префиксное дерево с поиском и частотным автодополнением."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, count=1):
        """Добавить слово или увеличить его частоту на count."""
        if not isinstance(word, str) or not word:
            raise ValueError("Слово должно быть непустой строкой")
        if isinstance(count, bool) or not isinstance(count, int) or count <= 0:
            raise ValueError("Количество должно быть положительным целым числом")

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True
        node.frequency += count

    def _find_node(self, prefix):
        """Найти узел префикса или вернуть None, если пути нет."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def search(self, word):
        """Проверить, есть ли в дереве именно такое слово."""
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        """Проверить, существует ли путь для указанного префикса."""
        return self._find_node(prefix) is not None

    def get_frequency(self, word):
        """Получить частоту слова (0, если слова нет)."""
        node = self._find_node(word)
        if node is None or not node.is_end:
            return 0
        return node.frequency

    def autocomplete(self, prefix, limit=5):
        """Найти слова по префиксу, отсортировав по частоте и алфавиту."""
        if not isinstance(limit, int) or isinstance(limit, bool) or limit < 0:
            raise ValueError("Лимит должен быть неотрицательным целым числом")
        if limit == 0:
            return []

        start_node = self._find_node(prefix)
        if start_node is None:
            return []

        results = []
        stack = [(start_node, prefix)]

        # Обходим поддерево в глубину без рекурсии.
        while stack:
            node, current_word = stack.pop()
            if node.is_end:
                results.append((current_word, node.frequency))

            for char, child in node.children.items():
                stack.append((child, current_word + char))

        # Сначала самые частые слова, при равенстве — по алфавиту.
        results.sort(key=lambda item: (-item[1], item[0]))
        return results[:limit]

    def search_path(self, word):
        """Вернуть пройденные префиксы и результат точного поиска.

        Пройденные префиксы позже можно подсвечивать в интерфейсе.
        """
        node = self.root
        visited = []
        current_prefix = ""

        for char in word:
            if char not in node.children:
                return visited, False
            node = node.children[char]
            current_prefix += char
            visited.append(current_prefix)

        return visited, node.is_end
