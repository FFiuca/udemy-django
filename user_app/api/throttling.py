from rest_framework.throttling import AnonRateThrottle

class LoginThrottle(AnonRateThrottle):
    scope = 'login-attempt'

class RegisterThrottle(AnonRateThrottle):
    scope = 'register-attempt'
