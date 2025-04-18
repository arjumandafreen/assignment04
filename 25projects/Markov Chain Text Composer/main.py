import random
from termcolor import colored

def generate_markov_chain(text, n_gram=2):
    markov_chain = {}
    words = text.split()
    for i in range(len(words) - n_gram):
        gram = tuple(words[i:i + n_gram])
        next_word = words[i + n_gram]
        if gram not in markov_chain:
            markov_chain[gram] = []
        markov_chain[gram].append(next_word)
    return markov_chain

def generate_text(markov_chain, length=50, n_gram=2):
    start = random.choice(list(markov_chain.keys()))
    result = list(start)
    for _ in range(length - n_gram):
        state = tuple(result[-n_gram:])
        if state in markov_chain:
            next_word = random.choice(markov_chain[state])
            result.append(next_word)
        else:
            break
    return ' '.join(result)

def main():
    text = '''As the sun rises, painting the sky with hues of gold, we step into the day with renewed energy.
    Every moment holds the potential to lead us down paths of discovery, as we uncover the treasures hidden in the mundane.
    It’s in the silence that we hear the whispers of wisdom, and in the hustle, we find our purpose unfolding.
    Nature’s rhythm teaches us the art of patience, while the stars above remind us of the vastness of time.
    Let us cherish each fleeting moment, for in them lies the magic that shapes our journey.'''
    
    markov_chain = generate_markov_chain(text, n_gram=2)
    generated_text = generate_text(markov_chain, length=50, n_gram=2)
    
    # Display generated text with colors and style
    print(colored("Generated Text:\n", 'magenta', attrs=['bold']))
    print(colored(generated_text, 'cyan', attrs=['underline']))

if __name__ == '__main__':
    main()
