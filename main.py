import time
import random
from generator import load_words, generate_random_words_sequence

def typing_test():
    words = load_words("english_1k.txt")
    text = generate_random_words_sequence(words, 5)

    print("Typing Test")
    print("Type the following text as fast as you can: \n")
    print(text+"\n")
    
    input("Press Enter when you're ready to start...")
    
    start_time = time.time()
    typed_text = input("Start typing here:\n\n")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words = typed_text.split()
    word_count = len(words)
    
    print(f"elapsed time: {elapsed_time}")
    print(f"time/60: {elapsed_time/60}")
    speed = word_count / (elapsed_time / 60)
    
    typed_text_words = typed_text.split()
    sample_text_words = text.split()
    correct_words_count = sum(typed == sample for typed, sample in zip(typed_text_words, sample_text_words))
    accuracy = (correct_words_count / len(sample_text_words)) * 100
    
    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Your typing speed: {speed:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

typing_test()
