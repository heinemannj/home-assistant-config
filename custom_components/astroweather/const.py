"""Constants in AstroWeather component."""
DOMAIN = "astroweather"

CONF_FORECAST_TYPE = "forecast_type"
CONF_FORECAST_INTERVAL = "forecast_interval"
CONF_LATITUDE = "latitude"
CONF_LONGITUDE = "longitude"
CONF_ELEVATION = "elevation"
CONF_TIMEZONE_INFO = "timezone_info"
CONF_CONDITION_CLOUDCOVER_WEIGHT = "cloudcover_weight"
CONF_CONDITION_SEEING_WEIGHT = "seeing_weight"
CONF_CONDITION_TRANSPARENCY_WEIGHT = "transparency_weight"
CONF_METNO_ENABLED = "metno_enabled"

ASTROWEATHER_PLATFORMS = ["binary_sensor", "sensor", "weather"]
DEVICE_TYPE_WEATHER = "weather"

DEFAULT_ATTRIBUTION = "Powered by 7Timer and Met.no"
DEFAULT_FORECAST_INTERVAL = 60
FORECAST_INTERVAL_MIN = 30
FORECAST_INTERVAL_MAX = 240
DEFAULT_ELEVATION = 0
DEFAULT_TIMEZONE_INFO = "Etc/UTC"
DEFAULT_METNO_ENABLED = True

# In progress, make condition calculation customizable
DEFAULT_CONDITION_CLOUDCOVER_WEIGHT = 3
DEFAULT_CONDITION_SEEING_WEIGHT = 2
DEFAULT_CONDITION_TRANSPARENCY_WEIGHT = 1

ATTR_WEATHER_CLOUDCOVER = "cloudcover_percentage"
ATTR_WEATHER_CLOUDLESS = "cloudless_percentage"
ATTR_WEATHER_SEEING = "seeing_percentage"
ATTR_WEATHER_TRANSPARENCY = "transparency_percentage"
ATTR_WEATHER_LIFTED_INDEX = "lifted_index"
ATTR_WEATHER_CONDITION = "condition_percentage"
ATTR_WEATHER_CONDITION_PLAIN = "condition_plain"
ATTR_WEATHER_PREC_TYPE = "prec_type"
ATTR_WEATHER_DEEPSKY_TODAY_DAYNAME = "deepsky_forecast_today_dayname"
ATTR_WEATHER_DEEPSKY_TODAY_PLAIN = "deepsky_forecast_today_plain"
ATTR_WEATHER_DEEPSKY_TODAY_DESC = "deepsky_forecast_today_desc"
ATTR_WEATHER_DEEPSKY_TOMORROW_DAYNAME = "deepsky_forecast_tomorrow_dayname"
ATTR_WEATHER_DEEPSKY_TOMORROW_PLAIN = "deepsky_forecast_tomorrow_plain"
ATTR_WEATHER_DEEPSKY_TOMORROW_DESC = "deepsky_forecast_tomorrow_desc"
ATTR_WEATHER_SUN_NEXT_RISING = "sun_next_rising"
ATTR_WEATHER_SUN_NEXT_SETTING = "sun_next_setting"
ATTR_WEATHER_SUN_NEXT_RISING_NAUTICAL = "sun_next_rising_nautical"
ATTR_WEATHER_SUN_NEXT_SETTING_NAUTICAL = "sun_next_setting_nautical"
ATTR_WEATHER_SUN_NEXT_RISING_ASTRO = "sun_next_rising_astro"
ATTR_WEATHER_SUN_NEXT_SETTING_ASTRO = "sun_next_setting_astro"
ATTR_WEATHER_MOON_NEXT_RISING = "moon_next_rising"
ATTR_WEATHER_MOON_NEXT_SETTING = "moon_next_setting"
ATTR_WEATHER_MOON_PHASE = "moon_phase"
ATTR_WEATHER_WIND_SPEED_PLAIN = "wind_speed_plain"
ATTR_FORECAST_CLOUDCOVER = "cloudcover_percentage"
ATTR_FORECAST_CLOUDLESS = "cloudless_percentage"
ATTR_FORECAST_SEEING = "seeing_percentage"
ATTR_FORECAST_TRANSPARENCY = "transparency_percentage"
ATTR_FORECAST_LIFTED_INDEX = "lifted_index"
ATTR_FORECAST_HUMIDITY = "humidity"
ATTR_FORECAST_PREC_TYPE = "prec_type"

CONDITION_CLASSES = ["excellent", "good", "fair", "poor", "bad"]
