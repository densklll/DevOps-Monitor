# Указываем нашу кастомную модель пользователя
AUTH_USER_MODEL = 'users.User'

# Настройки для djangorestframework и JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
} 
# 2022-01-24: Tighten Compose dependency boot order (staging)

# 2022-02-10: Describe CI layout verify step scope (prod checklist)

# 2022-03-01: Describe notification channel fallback (prod checklist)

# 2022-03-17: Mark K8s CPU requests for backend (demo box)
