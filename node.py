class Node:
    """Класс для узла связного списка."""
    def __init__(self, data):
        self.data = data  # Данные узла
        self.next = None  # Указатель на следующий узел

class LinkedList:
    """Класс для связного списка."""
    def __init__(self):
        self.head = None  # Голова списка

    def insert(self, data):
        """Вставка нового узла в конец списка."""
        new_node = Node(data)  # Создаем новый узел
        if not self.head:  # Если список пустой
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # Находим последний узел
            last_node = last_node.next
        last_node.next = new_node  # Добавляем новый узел в конец

    def delete(self, key):
        """Удаление узла по значению."""
        current = self.head
        if current and current.data == key:  # Проверяем, если нужно удалить голову
            self.head = current.next  # Перемещаем голову
            current = None
            return
        prev = None
        while current and current.data != key:  # Ищем узел для удаления
            prev = current
            current = current.next
        if current is None:  # Если узел не найден
            return
        prev.next = current.next  # Удаляем узел из списка
        current = None  # Освобождение памяти