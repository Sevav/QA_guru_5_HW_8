Вам нужно реализовать и протестировать классы интернет-магазина. 
Все места, которые нужно дописать как в тестах, так и классах, отмечены # TODO.
При реализации обращайте внимание на типизацию аргументов методов и возвращаемых значений. 
Так же обратите внимание на организацию тестов в файле с тестами:


• Тесты сгруппированы по классу, который они тестируют.

• Каждый тест называется именем соответствующего ему метода.

Вы можете начать как с реализации классов, так и с тестов.

Дополнительные вопросы:

1) С чего проще начать выполнение домашнего задания: с тестов или с реализации классов?

Рекомендуется начать выполнение домашнего задания с реализации классов, 
так как это позволит лучше понять требования к классам и их взаимодействие. 
Затем можно перейти к написанию тестов для проверки правильности работы классов.

2) Почему для хранения товаров в корзине используется словарь, а не список?

Лучше использовать словарь, потому что он позволяет быстро находить элементы по ключу, 
который может быть уникальным идентификатором товара.

3) Зачем нужен hash в классе Product? Изучите этот метод и объясните, почему он нужен.

Hash в классе Product нужен для того, чтобы каждый экземпляр класса имел уникальный идентификатор. 
Это позволяет использовать объекты класса Product в качестве ключей в словаре, 
так как словарь использует хеш-функцию для быстрого поиска элементов по ключу. 
Кроме того, хеш может использоваться для сравнения объектов класса Product, 
что может быть полезно при сортировке или удалении дубликатов.
