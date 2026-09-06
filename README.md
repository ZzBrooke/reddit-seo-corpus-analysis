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

## Experiment 1: Lexical Diversity
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

## Experiment 2: Evaluative Vocabulary
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

Among the evaluative words identified, **75.61%** of Reddit instances are community-oriented, compared with **24.39%** that are guide-oriented. In the SEO corpus, **100%** of the identified evaluative words are guide-oriented.

## Experiment 3: Local Contexts of Evaluative Keywords
This experiment examines the local contexts of selected evaluative keywords: *best*, *strong*, *broken*, and *op*.

### Methodology
For each keyword, words appearing within a **±5-word context window** were collected. Common stopwords were removed, and the 10 most frequent context words were identified for each corpus.

The context words from Reddit and SEO were then compared to examine whether the same evaluative keywords appear in different local contexts.

### Results
The context patterns differ between the two corpora:
* **`best`:** In the SEO corpus, frequent context words include *build*, *brawl*, *nori*, *stars*, and *modes*. In Reddit, *super* is the most frequent context word, while the other context words occur only once.
* **`strong`:** SEO contexts include *nori*, *shields*, *speed*, and *mobility*, while Reddit contexts include *should*, *super*, *position*, and *atm*.
* **`broken` and `op`:** Both keywords occur only in the Reddit corpus in this dataset. *Broken* appears near words such as *its*, *gonna*, *not*, and *brawl*, while *op* appears near words such as *strong*, *cool*, *legendary*, and *brawler*.

Overall, the results show that the same evaluative keywords can appear in different local contexts across the two corpora. SEO contexts are more closely associated with character names, builds, game modes, and gameplay-related features, while Reddit contexts include more informal and conversational expressions.

## Discussion & Limitations
### Discussion
Overall, the analysis suggests that community discussions and SEO game guides may cover similar gaming topics, but they differ in how evaluative information is expressed and organized. The “compression” observed at the beginning of the project is better understood not as a simple reduction in vocabulary, but as a shift toward more standardized ways of expressing evaluation.

### Limitations
This project has several limitations:
1. **Sample Size & Sampling:** The dataset is relatively small, containing 164 Reddit comments and 141 SEO guide sentences. Both corpora were also collected from specific gaming characters and topics rather than through large-scale, systematic sampling. The results therefore mainly reflect the language patterns found in this dataset, and differences in the game, topic, or data source may have influenced the results.

2. **Evaluative Vocabulary Classification:** The evaluative word lists used in Experiment 2 were developed with reference to a survey of 150 participants, including native speakers of Chinese, English, and Portuguese. However, the analysis still relies on a predefined set of vocabulary. This classification may not capture all forms of evaluative language found in the original texts, and the same word may serve different functions depending on its context.

3. **Contextual Analysis Scope:** Experiment 3 used a fixed **±5-word window** to examine local contexts rather than formal statistical measures of collocation. The results therefore describe observed patterns around the selected keywords, but they do not establish statistically significant collocational relationships.

Overall, this project should be viewed as a small-scale exploratory analysis. It demonstrates how Python and corpus-linguistic methods can be used to investigate content rewriting and language change, while providing a basis for further research using larger datasets, broader evaluative vocabulary, and more formal statistical methods.

## How to Run
1. Clone or download this repository.
2. Install the required Python packages:
   ```bash
   pip install pandas matplotlib
   ```
3. Make sure the cleaned datasets are available in the `data/` folder.
4. Run the three experiment scripts:
   ```bash
   python experiment/Experiment1_lexical_diversity.py
   python experiment/Experiment2_evaluative_language.py
   python experiment/Experiment3_context_analysis.py
   ```
The cleaned datasets are included in the `data/` folder and can be used directly as the input for all three experiments.
The preprocessing scripts are included for reference, but the original raw data are not provided in this repository.

## Project Structure
```text
reddit-seo-corpus-analysis/
├── data/
│   ├── reddit_comments_clean.csv
│   └── blog_sentences_clean.csv
├── preprocessing/
│   ├── clean_reddit_comments.py
│   └── clean_blog_sentences.py
├── experiment/
│   ├── Experiment1_lexical_diversity.py
│   ├── Experiment2_evaluative_language.py
│   └── Experiment3_context_analysis.py
├── results/
│   ├── experiment1/
│   │   ├── Figure_1.png
│   │   └── Figure_2.png
│   ├── experiment2/
│   │   ├── Figure_3.png
│   │   └── Figure_4.png
│   └── experiment3/
│       ├── Figure_5.png
│       ├── Figure_6.png
│       ├── Figure_7.png
│       └── Figure_8.png
├── .gitignore
└── README.md
```
* `data/` — Cleaned Reddit and SEO text used in the analysis
* `preprocessing/` — Scripts used to clean and prepare the text
* `experiment/` — Scripts used for the three corpus analyses
* `results/` — Figures generated from the experiments
* `.gitignore` — Files and folders excluded from version control
* `README.md` — Project description, methodology, results, and limitations
