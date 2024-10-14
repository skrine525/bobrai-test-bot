import aiohttp
from app import config
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums.parse_mode import ParseMode


router = Router()   # Роутер


# Callback Data
class WeatherCallbackData(CallbackData, prefix="quote"):
    lat: float
    lon: float


async def get_weather(lat: float, lon: float):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': config.OPEN_WEATHER_MAP_TOKEN,
        'units': 'metric',
        'lang': 'ru'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            response.raise_for_status()
            return await response.json()


async def get_cities(q: str):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q': q,
        'appid': config.OPEN_WEATHER_MAP_TOKEN,
        'limit': 6
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            response.raise_for_status()
            return await response.json()
        
        

async def send_weather(message: Message, lat: float, lon: float):
    weather = await get_weather(lat, lon)
    
    temp = weather["main"]["temp"]
    temp_feels_like = weather["main"]["feels_like"]
    humidity = weather["main"]["humidity"]
    desc = weather["weather"][0]["description"].capitalize()
    city_name = weather["name"]
    
    text = f"🏙 Погода в городе <u>{city_name}</u>:\n\n⛅️ Описание: {desc}\n🌡 Температура: {temp}C\n↪️ Ощущается как: {temp_feels_like}C\n💧 Влажность: {humidity}%"
    
    await message.reply(text=text, parse_mode=ParseMode.HTML)


# Обработчики

# Обработка всех сообщений от пользователя
@router.message()
async def message(message: Message):
    if message.content_type != "text":
        await message.reply(text=f"🏙 {message.from_user.first_name}, отправь, пожалуйста, название города.")
        return
    
    try:
        cities = await get_cities(message.text)
    except:
        await message.reply(text=f"⛔️ Во время запроса произошла ошибка!")
        return
    
    try:
        if cities:
            if len(cities) == 1:
                lat = cities[0]["lat"]
                lon = cities[0]["lon"]
                
                await send_weather(message, lat, lon)
            else:
                keyboard = InlineKeyboardBuilder()
                keyboard.max_width = 2
                for city in cities:
                    lat = city["lat"]
                    lon = city["lon"]
                    city_name = city.get("local_names", {}).get("ru", cities[0]["name"])
                    country = city["country"]
                    
                    callback_data = WeatherCallbackData(lat=lat, lon=lon)
                    keyboard.button(text=f"{city_name}, {country}", callback_data=callback_data)
                    
                await message.reply(text="Выберите город.", reply_markup=keyboard.as_markup())
        else:
            await message.reply(text=f"⚠️ По вашему запрос не найдено городов!")
            return
    except:
        await message.reply(text=f"⛔️ Во время запроса произошла ошибка!")
        
        
@router.callback_query(WeatherCallbackData.filter())
async def weather_button(query: CallbackQuery, callback_data: WeatherCallbackData):
    try:
        await send_weather(query.message, callback_data.lat, callback_data.lon)
        await query.answer()
    except:
        await query.answer(text="⛔️ Во время запроса произошла ошибка!", show_alert=True)