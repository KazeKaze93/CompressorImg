# Image Compressor

**Image Compressor** — это простое приложение для сжатия изображений, написанное на Python с использованием библиотеки PyQt5 для графического интерфейса и Pillow для обработки изображений. Приложение позволяет уменьшать размер и качество изображений, сохраняя их в различных форматах (JPEG, PNG, WebP).

---

## Основные функции

- **Сжатие изображений**: Уменьшение размера файла изображения за счет снижения качества и/или разрешения.
- **Поддержка форматов**: JPEG, PNG, WebP.
- **Графический интерфейс**: Удобный и интуитивно понятный интерфейс для выбора изображений и настройки параметров сжатия.
- **Гибкие настройки**:
  - Управление качеством сжатия (от 1 до 100%).
  - Уменьшение разрешения изображения (от 10 до 100% от исходного размера).

---

## Установка

### Требования

- Python 3.7 или выше.
- Установленные зависимости: PyQt5, Pillow.

### Инструкция по установке

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/KazeKaze93/CompressorImg.git
   cd image-compressor
2. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt

3. Запустите приложение:
   ```bash
   python main.py

---
### Сборка исполняемого файла (.exe)

Чтобы создать исполняемый файл (.exe), выполните следующие шаги:

1. Установите PyInstaller:
   ```bash
   pip install pyinstaller
2. Перейдите в корневую директорию проекта (где находится main.py).
3. Выполните команду для сборки:
   ```bash
   pyinstaller --onefile --windowed main.py
* --onefile: Собирает все в один исполняемый файл.
* --windowed: Запускает приложение без консоли (для GUI-приложений).
4. После завершения сборки:
* Исполняемый файл будет находиться в папке dist.
---

## Использование

1. **Выберите изображение для сжатия**:
   - Нажмите кнопку "Обзор..." рядом с полем "Выберите изображение для сжатия" и выберите файл.

2. **Укажите выходной файл**:
   - Нажмите кнопку "Обзор..." рядом с полем "Сохранить как" и выберите место сохранения и формат файла (JPEG, PNG, WebP).

3. **Настройте параметры сжатия**:
   - **Качество сжатия**: Введите значение от 1 до 100 (чем меньше значение, тем сильнее сжатие).
   - **Уменьшение разрешения**: Введите значение от 10 до 100 (процент от исходного разрешения).

4. **Запустите сжатие**:
   - Нажмите кнопку "Сжать изображение".
   - После завершения сжатия вы увидите сообщение с результатами (размер до и после сжатия,