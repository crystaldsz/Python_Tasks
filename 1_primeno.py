# Prime Number Generator 
# Generate all prime numbers between two given numbers using a function. 
def is_prime(num):  
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False 
    return True

def find_primes_in_range(start, end):
    primes = [] 
    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)
    return primes

if __name__ == "__main__":
    
    start_num, end_num = 11, 20
    found_primes = find_primes_in_range(start_num, end_num)
    print(" ".join(map(str, found_primes)))
    