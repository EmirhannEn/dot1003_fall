def factorial(n):
    if n < 0:
        raise ValueError("No negative value")
        k = 1
    for i in range(2,n+1):
        k *= i
    return k

try:
    print(factorial(5))   # Bu çalışır ve 120 yazar [cite: 491, 493]
    print(factorial(-1))  # Buraya gelince fonksiyon 'raise' ile hata fırlatır [cite: 492, 494]
except ValueError as e:
    # Fonksiyonun fırlattığı "No negative value" mesajını burada yakalarız
    print(f"Hata yakalandi: {e}")
  


            
