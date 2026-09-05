"""
Clean Reddit comments for corpus analysis.

Input: a CSV file containing a 'text' column.
Output: a CSV file containing 'source' and 'text' columns.
"""

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
    input_file = 'reddit_comments_raw.csv'
    output_file = 'reddit_comments_clean.csv'

    df = pd.read_csv(input_file)

    if 'text' not in df.columns:
        raise ValueError('Input file must contain a 'text' column.')

    df['text'] = df['text'].apply(clean_text)
    df = df[df['text'] != ''].copy()

    result = pd.DataFrame({
        'source': 'reddit',
        'text': df['text']
    })

    result.to_csv(output_file, index=False)
    print(f'Saved {len(result)} comments to {output_file}')


if __name__ == '__main__':
    main()
