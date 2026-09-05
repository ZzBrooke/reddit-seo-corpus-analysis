import pandas as pd
import matplotlib.pyplot as plt


def tokenize(text):
    return text.split()


community_words = {
    'broken',
    'insane',
    'trash',
    'ridiculous',
    'annoying',
    'op',
    'fun',
    'cool',
    'great',
    'stupid',
    'overpowered'
}

guide_words = {
    'best',
    'strong',
    'excellent',
    'useful',
    'reliable',
    'consistent',
    'effective',
    'worth',
    'weak',
    'powerful',
    'safe'
}


def find_evaluative_words(tokens, word_set):
    words = []

    for token in tokens:
        if token in word_set:
            words.append(token)

    return words


def normalized_frequency(word_count, total_tokens):
    if total_tokens == 0:
        return 0.0

    return (word_count / total_tokens) * 1000


def evaluative_ttr(evaluative_tokens):
    if not evaluative_tokens:
        return 0.0

    return len(set(evaluative_tokens)) / len(evaluative_tokens)


def category_share(category_count, total_evaluative):
    if total_evaluative == 0:
        return 0.0

    return category_count / total_evaluative

def analyze_corpus(df):
    tokens = []

    for text in df['text']:
        tokens.extend(tokenize(text))

    community_tokens = find_evaluative_words(
        tokens,
        community_words
    )

    guide_tokens = find_evaluative_words(
        tokens,
        guide_words
    )

    evaluative_tokens = community_tokens + guide_tokens

    total_tokens = len(tokens)

    community_frequency = len(community_tokens)
    guide_frequency = len(guide_tokens)
    evaluative_frequency = len(evaluative_tokens)

    return {
        'Tokens': total_tokens,
        'Community Frequency': community_frequency,
        'Guide Frequency': guide_frequency,
        'Evaluative Frequency': evaluative_frequency,
        'Community / 1000 tokens':
            normalized_frequency(
                community_frequency,
                total_tokens
            ),
        'Guide / 1000 tokens':
            normalized_frequency(
                guide_frequency,
                total_tokens
            ),
         'Community Share':
            category_share(
                community_frequency,
                evaluative_frequency
            ),
        'Guide Share':
            category_share(
                guide_frequency,
                evaluative_frequency
            ),
        'Evaluative TTR':
            evaluative_ttr(
                evaluative_tokens
            )
    }


def main():
    pd.set_option('display.max_columns', None)
        
    reddit = pd.read_csv('reddit_comments_clean.csv')
    seo = pd.read_csv('blog_sentences_clean.csv')

    reddit_result = analyze_corpus(reddit)
    seo_result = analyze_corpus(seo)

    results = pd.DataFrame(
        [reddit_result, seo_result],
        index=['Reddit', 'SEO']
    )

    print(results)

    
    results[
        [
            'Community / 1000 tokens',
            'Guide / 1000 tokens'
        ]
    ].plot(
        kind='bar',
        figsize=(8, 5)
    )

    plt.ylabel('Frequency per 1,000 tokens')
    plt.title('Evaluative Language: Reddit vs SEO')
    plt.xticks(rotation=0)
    plt.legend()
    plt.tight_layout()
    plt.show()


    results[
        [
            'Community Share',

            'Guide Share'
        ]
    ].plot(
        kind='bar',
        figsize=(8, 5)
    )

    plt.ylabel('Proportion')
    plt.title('Evaluative Language Orientation: Reddit vs SEO')
    plt.xticks(rotation=0)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()