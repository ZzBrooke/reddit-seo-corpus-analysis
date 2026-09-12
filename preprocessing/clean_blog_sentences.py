import re
import pandas as pd


def clean_text(text):
    text = str(text).lower()
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'_', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def main():
    input_file = '../raw_data/blog_sentences_raw.csv'
    output_file = '../raw_data/blog_sentences_clean.csv'

    df = pd.read_csv(input_file)

    if 'text' not in df.columns:
        raise ValueError('Input file must contain a \'text\' column.')

    df['text'] = df['text'].apply(clean_text)
    df = df[df['text'] != ''].copy()

    # Keep sentences with at least five words and remove duplicates.
    df['word_count'] = df['text'].str.split().str.len()
    df = df[df['word_count'] >= 5].drop_duplicates(subset='text')

    result = pd.DataFrame({
        'source': 'ldplayer',
        'text': df['text']
    })

    result.to_csv(output_file, index=False)
    print(f'Saved {len(result)} sentences to {output_file}')


if __name__ == '__main__':
    main()
