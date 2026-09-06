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
### Experiment 1: Lexical Diversity
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

### Experiment 2: Evaluative Vocabulary
This experiment compares the use of **community-oriented** and **guide-oriented** evaluative vocabulary in the Reddit and SEO corpora.

### Methodology
Two word lists were used to identify evaluative language:
* **Community-oriented words:** *broken*, *insane*, *trash*, *fun*, *overpowered*, and others
* **Guide-oriented words:** *best*, *strong*, *effective*, *powerful*, *safe*, and others

The frequency of words from each category was counted for each corpus. Frequencies were also normalized per 1,000 tokens to make the two corpora more comparable. The proportion of each category among all identified evaluative words was also calculated.

### Results
| Corpus     | Community Frequency | Guide Frequency | Community / 1,000 tokens | Guide / 1,000 tokens |
| ---------- | ------------------: | --------------: | -----------------------: | -------------------: |
| **Reddit** |                  31 |              10 |                    10.49 |                 3.39 |
| **SEO**    |                   0 |              43 |                     0.00 |                22.70 |

The Reddit corpus contains more community-oriented evaluative words, while the SEO corpus contains more guide-oriented evaluative words. After normalization, the difference remains clear: community-oriented words occur more frequently in Reddit, whereas guide-oriented words are much more frequent in SEO.

Among the evaluative words identified, **75.61%** of Reddit examples are community-oriented, compared with **24.39%** that are guide-oriented. In the SEO corpus, **100%** of the identified evaluative words are guide-oriented.

