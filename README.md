# Lang
v_0.4.0  
Обновлена струкрутра программы. Теперь все грамы считаются в отдельных файлах. Так же в отдельном файле осуществляется обработка исходных тренировочного и тестового файла.  
Вскоре бдует использоваться другой алгоритм поиска слов.  


v_0.3.1  
python 3.4 + sklearn + numpy


#<b>Программа по определению языка.</b>
Идея: 

1. Из файла tr.txt (train.txt) парсим строку на символы и название языка.
2. Символы группируем по 1, 2, 3 и записываем в массив. Считаем количество повторений для каждого. 
3. Проходим так весь файл и получаем массив 1,2,3-грам и частоту встреч каждого грама для каждого языка.
4. Выбираем самые часто встречающиеся в каждом языке.
5. Заново пробегаем файл tr.txt теперь, чтобы на основе самых "частых" н-грам создать вектор, содержащий числа- количества встреч каждого грама.
6. Открываем файл ts.txt (test.txt) парсим по строкам.
7. Создаем вектор, в котором записана частота встреч каждого грама.
8. Тренируем наивный Байесовский классификатор.
9. Пытаемся "предсказать" языки, которые забиты в файл ts.txt (test.txt)

Реализация:

Программа оказалась очень требовательной и моих ресурсов не хватало. Пришлось разбить программу на две части

b.py:

Удаляем из тренировочного и тестовго файла ненужные пробелы, цифры и т.п.  
Парсим полученный файл на грамы (очень долгий процесс, пока не смог его оптимизировать; у меня уходило несколько часов на исполнение этого кода) и записываем их в файл.  

d.py:

Достаем языки из файла tr.txt.  
Достаем грамы из файла all_grams.txt.  
Выбираем нужное нам количество грам (сколько элементов каждого из них будет участвовать в оценке; в файле они отсортированы, так что просто берем n первых).  
Создаем тренировочный вектор с ответами из файла tr.txt.  
Создаем вектор, который нужно определить.  
Используем sklearn  

p.s. Есть идея реализации другого алгоритма классификации. Но это уже как нибудь потом.
