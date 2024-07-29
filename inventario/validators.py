from django.core.exceptions import ValidationError


def validar_par(value):
    if value % 2 != 0:
        raise ValidationError("%(valor)s no es un numero par", params={'valor': value})

def validar_email(value):
    """Valida que el correo electrónico tenga un dominio específico."""
    if not value.endswith('@diplomadofullstack.com'):
        raise ValidationError('El correo electrónico debe ser de dominio @diplomadofullstack.com')

def validar_precio(value):
    """Valida que el precio sea mayor que 0."""
    if value <= 0:
        raise ValidationError('El precio debe ser mayor que 0')

def validar_rating(value):
    """Valida que la calificación esté en el rango de 1 a 5."""
    if value < 1 or value > 5:
        raise ValidationError('La calificación debe estar entre 1 y 5')

def validar_url(value):
    """Valida que la URL tenga un formato específico (solo por ejemplo)."""
    if not re.match(r'^https?:\/\/', value):
        raise ValidationError('La URL debe comenzar con http:// o https://')

def validar_nombre_no_comida(value):
    """Valida que el nombre no sea 'Comida'."""
    if value.lower() == 'comida':
        raise ValidationError('El nombre no puede ser "Comida"')