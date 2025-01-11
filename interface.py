from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt
from algorithms import compress_image


class ImageCompressorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сжатие изображений")
        self.setFixedSize(500, 150)  # Фиксированный размер окна

        # Основной виджет и макет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Создаем и настраиваем поля ввода
        self.setup_input_fields()
        self.setup_output_fields()
        self.setup_quality_resize_fields()
        self.setup_compress_button()

    def setup_input_fields(self):
        """Настройка поля для выбора входного файла."""
        input_layout = QHBoxLayout()
        input_label = QLabel("Выберите изображение для сжатия:")
        self.input_entry = QLineEdit()
        self.input_entry.setFixedWidth(200)  # Фиксированная ширина поля ввода
        input_button = QPushButton("Обзор...")
        input_button.setFixedWidth(80)  # Фиксированная ширина кнопки
        input_button.clicked.connect(self.select_input_file)

        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_entry)
        input_layout.addWidget(input_button)
        self.layout.addLayout(input_layout)

    def setup_output_fields(self):
        """Настройка поля для выбора выходного файла."""
        output_layout = QHBoxLayout()
        output_label = QLabel("Сохранить как:")
        self.output_entry = QLineEdit()
        self.output_entry.setFixedWidth(200)  # Фиксированная ширина поля ввода
        output_button = QPushButton("Обзор...")
        output_button.setFixedWidth(80)  # Фиксированная ширина кнопки
        output_button.clicked.connect(self.select_output_file)

        output_layout.addWidget(output_label)
        output_layout.addWidget(self.output_entry)
        output_layout.addWidget(output_button)
        self.layout.addLayout(output_layout)

    def setup_quality_resize_fields(self):
        """Настройка полей для ввода качества и уменьшения разрешения."""
        quality_resize_layout = QHBoxLayout()

        # Поле для ввода качества
        quality_label = QLabel("Качество сжатия (%):")
        quality_label.setFixedWidth(150)  # Фиксированная ширина метки
        self.quality_entry = QLineEdit()
        self.quality_entry.setFixedWidth(50)  # Фиксированная ширина поля ввода
        self.quality_entry.setText("100")  # Значение по умолчанию

        # Поле для ввода уменьшения разрешения
        resize_label = QLabel("Уменьшение разрешения (%):")
        resize_label.setFixedWidth(150)  # Фиксированная ширина метки
        self.resize_entry = QLineEdit()
        self.resize_entry.setFixedWidth(50)  # Фиксированная ширина поля ввода
        self.resize_entry.setText("100")  # Значение по умолчанию

        # Добавляем элементы в макет
        quality_resize_layout.addWidget(quality_label)
        quality_resize_layout.addWidget(self.quality_entry)
        quality_resize_layout.addSpacing(20)  # Отступ между полями
        quality_resize_layout.addWidget(resize_label)
        quality_resize_layout.addWidget(self.resize_entry)

        # Выравниваем содержимое влево
        quality_resize_layout.setAlignment(Qt.AlignLeft)
        self.layout.addLayout(quality_resize_layout)

    def setup_compress_button(self):
        """Настройка кнопки для запуска сжатия."""
        self.compress_button = QPushButton("Сжать изображение")
        self.compress_button.setFixedWidth(150)  # Фиксированная ширина кнопки
        self.compress_button.clicked.connect(self.start_compression)
        self.layout.addWidget(self.compress_button, alignment=Qt.AlignCenter)  # Выравниваем по центру

    def select_input_file(self):
        """Открывает диалог выбора входного файла."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "",
                                                   "Изображения (*.jpg *.jpeg *.png *.webp)")
        if file_path:
            self.input_entry.setText(file_path)

    def select_output_file(self):
        """Открывает диалог выбора выходного файла."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить сжатое изображение", "",
                                                   "JPEG (*.jpg);;PNG (*.png);;WebP (*.webp)")
        if file_path:
            self.output_entry.setText(file_path)

    def start_compression(self):
        """Запускает процесс сжатия изображения."""
        input_path = self.input_entry.text()
        output_path = self.output_entry.text()
        quality = self.quality_entry.text()
        resize_ratio = self.resize_entry.text()

        # Проверка наличия входного и выходного файлов
        if not input_path or not output_path:
            QMessageBox.warning(self, "Внимание", "Пожалуйста, выберите входной и выходной файлы.")
            return

        # Проверка корректности ввода качества
        try:
            quality = int(quality)
            if quality < 1 or quality > 100:
                QMessageBox.warning(self, "Внимание", "Качество должно быть от 1 до 100.")
                return
        except ValueError:
            QMessageBox.warning(self, "Внимание", "Качество должно быть целым числом от 1 до 100.")
            return

        # Проверка корректности ввода уменьшения разрешения
        try:
            resize_ratio = int(resize_ratio)
            if resize_ratio < 10 or resize_ratio > 100:
                QMessageBox.warning(self, "Внимание", "Уменьшение разрешения должно быть от 10 до 100%.")
                return
            resize_ratio = resize_ratio / 100.0  # Преобразуем проценты в дробное число
        except ValueError:
            QMessageBox.warning(self, "Внимание", "Уменьшение разрешения должно быть целым числом от 10 до 100.")
            return

        # Определяем формат выходного файла
        output_format = output_path.split(".")[-1].upper()
        if output_format not in ["JPEG", "JPG", "PNG", "WEBP"]:
            QMessageBox.warning(self, "Внимание", "Неподдерживаемый формат файла. Используйте JPEG, PNG или WebP.")
            return

        # Выполняем сжатие изображения
        success, result = compress_image(input_path, output_path, quality, output_format, resize_ratio)
        if success:
            QMessageBox.information(self, "Успех", f"Изображение успешно сжато!\n"
                                                   f"Исходный размер: {result['original_size_mb']:.2f} МБ\n"
                                                   f"Сжатый размер: {result['compressed_size_mb']:.2f} МБ\n"
                                                   f"Сжатие: {result['compression_ratio']:.2f}%\n"
                                                   f"Исходное разрешение: {result['original_resolution'][0]}x{result['original_resolution'][1]}\n"
                                                   f"Конечное разрешение: {result['final_resolution'][0]}x{result['final_resolution'][1]}")
        else:
            QMessageBox.critical(self, "Ошибка", result)
