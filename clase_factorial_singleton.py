class Factorial:
    _instance = None  # Almacena la única instancia

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def calculate_factorial(self, n):
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        if n == 0:
            return 1
        else:
            return n * self.calculate_factorial(n - 1)

# Uso de la clase Singleton Factorial
factorial_calculator = Factorial()

# Ejemplo de uso
num = 5
resultado = factorial_calculator.calculate_factorial(num)
print(f"El factorial de {num} es: {resultado}")
