import random
import time

def is_even(n):
    return n % 2 == 0

def count_evens_recursive(numbers,index=0):
    if index >= len(numbers):
        return 0
    return (1 if is_even(numbers[index]) else 0) + count_evens_recursive(numbers, index + 1)

def generate_ramdom_numbers(count, min_val=1,max_val=100):
    return [random.randint(min_val, max_val) for _ in range(count)]

def main():
    print("===program pengecekan Angka ganap dengan assertion, Try-except, dan rekursif===")
    while True:
        try:
            count = int(input("masukan jumlah angka ackak yang ingin dibuat (minimal 1): "))
            assert count > 0, "jumlah angka harus lebih dari 0!"

            numbers = generate_ramdom_numbers(count)
            print(f"\nAngka yang dihasilkan: {numbers}")

            print("\nMemeriksa ke genapan setiap angka:")
            for i in range(len(numbers)):
                try:
                    for j in range(1):
                        time.sleep(0.1)
                        print(f"angka {numbers[i]} {'genap' if is_even(numbers[i]) else 'ganjil'}")
                except Exception as e:
                    print(f"Terjadi kesalahan saat memeriksa angka ke {i}: {e}")

                    total_even = count_evens_recursive(numbers)
                    print(f"\nTotal angka genap (dihitung secara rekursif): {total_even}")

        except AssertionError as ae:
                    print(f"kesalahan assertion: {ae}")
        except ValueError:
                    print("input harus berupa angka bulat!")
        except Exception as e:
                    print(f"kesalahan tak terduga: {e}")

                    ulang = input("ingin mencoba lagi? (y/n): ").lower()
                    if ulang != 'y':
                        print("program selesa. terima kasih!")
                        break

if __name__=="__main__":
    main()