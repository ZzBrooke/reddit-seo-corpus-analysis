# reddit-seo-corpus-analysis
A corpus-based comparison of Reddit comments and SEO game-guide texts using Python.

## Research Motivation
In online gaming communities, players often use informal and expressive language shaped by community culture. SEO game guides, on the other hand, are written to meet users’ search needs and to work well with search engines. As a result, they tend to use more standardized and straightforward language. Because these two types of content serve different purposes, similar gaming topics may be expressed in different ways.

This project compares how similar gaming content is expressed in community discussions and SEO-oriented game guides. For example, players in community discussions may use informal evaluative expressions such as *broken*, *insane*, or *trash*. In game guides, similar evaluations may instead be expressed using more standardized, guide-oriented words such as *strong*, *best*, or *effective*.

To examine this difference, I use Python and corpus-linguistic methods to compare Reddit user comments with SEO-oriented game guide texts. The project looks at three main areas:
* Lexical diversity
* Evaluative vocabulary
* Local contexts of evaluative keywords

## Corpus & Data
The dataset compares language use across two sources, both focused on the game characters Wendy and Nori:
* **Reddit Comments (n = 164):** User discussions from Reddit threads about **Wendy** and **Nori**.
* **SEO Game Guides (n = 141):** Sentences extracted from SEO-oriented build guides for the same characters.

### Objective
This dataset provides a basis for analyzing how vocabulary and language use differ between community discussions and SEO-oriented game guides.

## Preprocessing
The raw text was cleaned using Python before analysis. The preprocessing steps included:
* Converting all text to lowercase
* Removing punctuation, underscores, and digits
* Normalizing whitespace
* Saving the cleaned texts as CSV files

The resulting datasets were used as the input for all three experiments.

The preprocessing scripts are provided in `clean_reddit_comments.py` and `clean_blog_sentences.py`.

## Experiment
### Experiment 1 — Lexical Diversity
This experiment compares lexical diversity between the Reddit and SEO corpora using **Type-Token Ratio (TTR)** and **Standardized Type-Token Ratio (STTR)**.

### Methodology
The cleaned texts were split into word tokens. TTR was calculated as the ratio of unique word types to total tokens. STTR was calculated by dividing each corpus into non-overlapping windows of 100 tokens and averaging the TTR scores across the windows.

TTR across the 100-token windows was also visualized to examine how lexical diversity varies throughout each corpus.

### Results
| Corpus     | Tokens | Types |    TTR |   STTR |
| ---------- | -----: | ----: | -----: | -----: |
| **Reddit** |  2,954 |   919 | 0.3111 | 0.7697 |
| **SEO**    |  1,894 |   624 | 0.3295 | 0.7733 |

The SEO corpus shows slightly higher overall TTR and STTR scores than the Reddit corpus, indicating slightly greater lexical diversity in this dataset.
