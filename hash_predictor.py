
import hashlib

def predict_input_from_hash(hash_value):
    first_128_bits = hash_value[:32]
    decimal_value = int(first_128_bits, 16)
    mapped_value = decimal_value % 26000
    if mapped_value < 1000:
        return 'a'
    elif mapped_value < 2000:
        return 'b'
    elif mapped_value < 3000:
        return 'c'
    elif mapped_value < 4000:
        return 'd'
    elif mapped_value < 5000:
        return 'e'
    elif mapped_value < 6000:
        return 'f'
    elif mapped_value < 7000:
        return 'g'
    elif mapped_value < 8000:
        return 'h'
    elif mapped_value < 9000:
        return 'i'
    elif mapped_value < 10000:
        return 'j'
    elif mapped_value < 11000:
        return 'k'
    elif mapped_value < 12000:
        return 'l'
    elif mapped_value < 13000:
        return 'm'
    elif mapped_value < 14000:
        return 'n'
    elif mapped_value < 15000:
        return 'o'
    elif mapped_value < 16000:
        return 'p'
    elif mapped_value < 17000:
        return 'q'
    elif mapped_value < 18000:
        return 'r'
    elif mapped_value < 19000:
        return 's'
    elif mapped_value < 20000:
        return 't'
    elif mapped_value < 21000:
        return 'u'
    elif mapped_value < 22000:
        return 'v'
    elif mapped_value < 23000:
        return 'w'
    elif mapped_value < 24000:
        return 'x'
    elif mapped_value < 25000:
        return 'y'
    else:
        return 'z'

if __name__ == "__main__":
    text = 'a'
    hash_full = hashlib.sha256(text.encode()).hexdigest()
    predicted = predict_input_from_hash(hash_full)
    print(f"Input: {text} | Full Hash: {hash_full} | Prediction: {predicted}")
