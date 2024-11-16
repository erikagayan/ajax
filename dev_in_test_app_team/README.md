## Ajax Systems, Python developer in test for Application team

### Завдання:
Встановити та налаштувати Appium, щоб на Android телефоні запустився автотест-заглушка.
Для цього на телефон необхідно встановити застосунок Ajax Systems (якщо немає реального Android девайсу, можна використати емулятор).


В папці з проєктом є папка Appium Manual, в ній детальний ґайд по налаштуванню на різних операційних системах (ґайд для macOS містить більше скриншотів).


### Реалізовано 2 варіанти запуску тестів:
- Скидання даних застосунку та вхід в систему "з нуля" (параметр --login при запуску pytest) при кожному запуску тестів
- Запуск застосунку без входу в систему
#### Примітка: Сервер може тимчасово заблокувати Вас через надмірну кількість авторизацій.


### Необхідний результат:
1) Розібратись із стуктурою та принципом роботи проекту
2) Розібратись як і для чого використовувати Appium Inspector.
3) Pytest має видати в консоль успішний результат тесту test_something.


### Корисні посилання:
1) Застосунок Ajax Systems - https://play.google.com/store/apps/details?id=com.ajaxsystems
2) Робота з реальним телефоном - https://developer.android.com/tools/adb
3) Налаштування емулятора - https://developer.android.com/studio/run/emulator
4) Драйвер - http://appium.io/docs/en/2.1/quickstart/uiauto2-driver/
5) Appium Inspector - https://github.com/appium/appium-inspector
