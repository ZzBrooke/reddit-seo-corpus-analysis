import pandas as pd
import matplotlib.pyplot as plt

def tokenize(text):
    return text.split()


def ttr(tokens):
    if not tokens:
        return 0.0

    return len(set(tokens)) / len(tokens)


def sttr(tokens, window_size=100):
    scores = []

    for i in range(0, len(tokens) - window_size + 1, window_size):
        window = tokens[i:i + window_size]
        scores.append(ttr(window))

    if not scores:
        return 0.0, []

    return sum(scores) / len(scores), scores


def analyze_corpus(df):
    tokens = []

    for text in df['text']:
        tokens.extend(tokenize(text))

    sttr_score, window_scores = sttr(tokens)
    
    return {
        'Tokens': len(tokens),
        'Types': len(set(tokens)),
        'TTR': ttr(tokens),
        'STTR': sttr_score
    }, window_scores


def main():
    reddit = pd.read_csv('../data/reddit_comments_clean.csv')
    seo = pd.read_csv('../data/blog_sentences_clean.csv')

    reddit_result, reddit_windows = analyze_corpus(reddit)
    seo_result, seo_windows = analyze_corpus(seo)

    results = pd.DataFrame(
        [reddit_result, seo_result],
        index=['Reddit', 'SEO']
    )

    print(results)
    
    results[['TTR', 'STTR']].plot(
        kind='bar',
        figsize=(7, 5)
    )

    plt.ylabel('Score')
    plt.title('Lexical Diversity: Reddit vs SEO')
    plt.xticks(rotation=0)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    plt.figure(figsize=(8, 5))

    plt.plot(
        range(1, len(reddit_windows) + 1),
        reddit_windows,
        label='Reddit'
    )

    plt.plot(
        range(1, len(seo_windows) + 1),
        seo_windows,
        label='SEO'
    )

    plt.xlabel('100-token window')
    plt.ylabel('TTR')
    plt.title('TTR across 100-token windows')
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
