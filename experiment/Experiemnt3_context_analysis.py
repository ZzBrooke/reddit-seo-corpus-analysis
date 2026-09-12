import pandas as pd
import matplotlib.pyplot as plt


def tokenize(text):
    return text.split()


keywords = [
    'best',
    'strong',
    'broken',
    'op'
]


stopwords = {
    'the', 'a', 'an', 'and', 'or', 'but', 'of', 'to', 'in', 'on',
    'for', 'with', 'at', 'by', 'from', 'is', 'are', 'was', 'were',
    'be', 'been', 'this', 'that', 'it', 'as', 'i', 'you', 'he',
    'she', 'they', 'we', 'my', 'your', 'their', 'our', 'his', 'her',
    'me', 'them', 'so', 'if', 'then', 'than', 'just', 'very'
}


def get_context(tokens, keyword, window_size=5):
    contexts = []

    for i, token in enumerate(tokens):        
        if token == keyword:
            start = max(0, i - window_size)
            end = min(len(tokens), i + window_size + 1)
            context = tokens[start:end]

            context = [
                word for word in context
                if word != keyword
            ]

            # Remove stopwords
            context = [
                word for word in context
                if word not in stopwords
            ]

            contexts.extend(context)

    return contexts


def top_context_words(context_words, top_n=10):

    if not context_words:
        return pd.Series(dtype=int)

    frequencies = pd.Series(context_words).value_counts()

    return frequencies.head(top_n)


def analyze_corpus(df):

    keyword_contexts = {}

    for keyword in keywords:
        all_context_words = []

        for text in df['text']:
            tokens = tokenize(text)          
            context_words = get_context(
                tokens,
                keyword
            )
            
            all_context_words.extend(context_words)

        keyword_contexts[keyword] = top_context_words(
            all_context_words
        )

    return keyword_contexts


def create_comparison(reddit_words, seo_words, top_n=10):

    # Combine both corpora
    all_words = list(
        set(reddit_words.index) | set(seo_words.index)
    )

    comparison = pd.DataFrame(
        index=all_words
    )

    comparison['Reddit'] = reddit_words
    comparison['SEO'] = seo_words

    comparison = comparison.fillna(0)

    # Total frequency
    comparison['Total'] = (
        comparison['Reddit'] +
        comparison['SEO']
    )

    # Top words overall
    comparison = comparison.sort_values(
        'Total',
        ascending=False
    ).head(top_n)

    comparison = comparison.drop(
        columns='Total'
    )

    return comparison


def main():

    reddit = pd.read_csv(
        '../data/reddit_comments_clean.csv'
    )
    seo = pd.read_csv(
        '../data/blog_sentences_clean.csv'
    )

    reddit_results = analyze_corpus(reddit)
    seo_results = analyze_corpus(seo)


    for keyword in keywords:
        print()
        print('Keyword:', keyword)
        print()

        print('Reddit:')
        print(reddit_results[keyword])

        print()

        print('SEO:')
        print(seo_results[keyword])

        print()
        print('-' * 40)


        comparison = create_comparison(
            reddit_results[keyword],
            seo_results[keyword],
            top_n=10
        )
        
        
        print('Top 10 context words:')
        print(comparison)


        comparison.plot(
            kind='bar',
            figsize=(8, 5)
        )

        plt.ylabel('Frequency')

        plt.title(
            f'Top Context Words around "{keyword}": '
            'Reddit vs SEO'
        )

        plt.xticks(
            rotation=45
        )

        plt.legend()

        plt.tight_layout()

        plt.show()


if __name__ == '__main__':
    main()
