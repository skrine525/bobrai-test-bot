

# Telegram Weather Bot

Этот Telegram-бот позволяет получать информацию о погоде в городах по всему миру.

## Начало работы

Следуйте этим шагам, чтобы клонировать репозиторий, настроить окружение и запустить бота с использованием Docker.

### Предварительные требования

Убедитесь, что у вас установлены следующие инструменты:
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)

### Установка

1. **Клонируйте репозиторий**

   Клонируйте репозиторий бота на ваш локальный компьютер:
   ```bash
   git clone https://github.com/skrine525/bobrai-test-bot
   cd bobrai-test-bot
   ```

2. **Настройка переменных окружения**

   Создайте копию файла с примером переменных окружения и отредактируйте его:
   ```bash
   cp example.env app.env
   ```

   Откройте файл `.env` в любом текстовом редакторе и укажите следующие значения:
   - `BOT_TOKEN`: Токен вашего Telegram-бота, полученный у [BotFather](https://t.me/botfather).
   - `OPEN_WEATHER_MAP_TOKEN`: API-ключ [OpenWeatherMap](https://home.openweathermap.org/api_keys).

3. **Запуск бота с Docker**

   Используйте Docker для сборки и запуска бота:
   ```bash
   docker compose up --build -d
   ```

   Эта команда соберет Docker-образ и запустит бота в контейнере.

### Использование

После запуска бота вы можете взаимодействовать с ним через Telegram. Достаточно прислать сообщение с названием города и бот пришлет погоду.

### Остановка бота

Для остановки бота используйте команду:
```bash
docker compose down
```
