# PyCharmTask-MikhalevNikita

### 1. Создал репозиторий и добавил файлы.


![1](https://user-images.githubusercontent.com/78908105/142763184-25e1afb1-4531-45c7-aef6-1de27fbc7db8.png)

### 2. Создал проект и подключил репозиторий, загрузил файлы.


![2](https://user-images.githubusercontent.com/78908105/142763216-0143b605-1d88-4c10-a582-58815016b86d.png)

### 3. Добавил тестовое изображение.


![3](https://user-images.githubusercontent.com/78908105/142763238-6cb3862c-555c-47b4-bd6b-45a5f375ed3f.png)


### 4. Загрузил изображение в репозиторий.


![4 1](https://user-images.githubusercontent.com/78908105/142763269-d62edf54-7bb9-443c-8ab9-09fa2b936122.png)
![4 2](https://user-images.githubusercontent.com/78908105/142763270-51a74a72-d1ed-4d3a-9d4a-8f24afee37c2.png)

### 5. Сделал профилизацию filter.py.


![5](https://user-images.githubusercontent.com/78908105/142763309-95e51369-1851-4755-afbf-0396c48f7911.png)

### 6. Сделал профилизацию old-filter.py.


По сравнению с old-filter переписанный filter работает быстрее, потому что происходит более оптимизированная работа с матрицей изображения благодаря модулю numpy. В моем случае скорость увеличилась более, чем в 4 раза.
![6](https://user-images.githubusercontent.com/78908105/142763354-42749721-4233-4ab4-bf20-df4454a11b39.png)

### 7. Создал отдельный filter без ввода с размером блока 10 и кол-вом градаций 50. Сделал профилизацию этого файла.


В профилизаторе резултат выполнения всей прогрммы кажется быстрее, тк отсутсвует ввод пользователя. На самом деле время работы одинаковое.
![7](https://user-images.githubusercontent.com/78908105/142763417-8d43b371-e18b-4435-ab44-5be723d799d7.png)

### 8. Фото до обработки и после.


![test-img](https://user-images.githubusercontent.com/78908105/142763740-39e9cbc7-a453-4033-8dc4-1e60e3352dd8.jpg)
![res](https://user-images.githubusercontent.com/78908105/142763745-cd408c68-d624-4b0b-95eb-44914b4a2d86.jpg)

### 9-10. Добавил doctests и документацию.


![9-10](https://user-images.githubusercontent.com/78908105/142763803-90584fb7-0e10-4bda-a517-2ed0f590f722.png)

### 11. Через отладчик вывел формат изображения и его размеры, ширину блока и кол-во градаций.


![13](https://user-images.githubusercontent.com/78908105/142763854-e86aec1a-8101-4854-bacf-f0ab32b6f362.png)


### Готовый результат исправлений по pep8 можно посмотреть в файле **filter_with_filename.py**.


