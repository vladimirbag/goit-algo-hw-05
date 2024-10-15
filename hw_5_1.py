def caching_fibonacci():
    cache = {} # Використовуємо словник для кешування

    def fibonacci(n):
        if n <= 0: 
            return 0
        elif n == 1: 
            return 1
        elif n in cache: 
            return cache[n]
        
        # ця строка робить оптимізацію обчислення чисел Фібоначчі 
        # за допомогою мемоізації, зберігаючи вже обчислені результати в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) 
        return cache[n]

    return fibonacci
print(caching_fibonacci)

# Створюємо екземпляр функції
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610