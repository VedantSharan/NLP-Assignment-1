# NLP-Assignment-1
## Kannada Dataset Curation, Cleaning, and Deduplication

This project involves the curation, processing, cleaning, and deduplication of text datasets in the Kannada language. The goal is to build a clean, high-quality dataset.
The dataset was sourced from publicly available websites and then processed to remove offensive language, pornographic content, hate speech, and duplicated articles.
The dataset is available at: https://huggingface.co/datasets/CoolCoder44/NLP_Assignment_1


### Key Steps:

1. **Data Curation**: Kannada text data was collected from publicly accessible and non-copyrighted sources.
2. **Cleaning**: Articles with offensive or inappropriate content were filtered out using a custom bad-word dictionary for Kannada.
3. **Deduplication**: Duplicate articles were identified and removed.

## Dataset Summary

The final dataset comprises curated, cleaned, and deduplicated articles, ensuring high-quality text data in the Kannada language.

### Raw Data
| Sources                           | Number of Articles | Volume (GBs) |
|-----------------------------------|--------------------|--------------|
| www.prajavani.net                 | 51,699             | 0.361        |
| zeenews.india.com/kannada        | 3,046              | 0.023        |
| www.kannadaprabha.com             | 28,515             | 0.154        |
| kannada.oneindia.com              | 555,306            | 3.996        |
| www.justkannada.in                | 82,444             | 0.465        |
| https://vishwavani.news           | 33,489             | 0.274        |
| eesanje.com                       | 11,044             | 0.069        |
| www.sanjevani.com                 | 24,140             | 0.138        |
| kannada.asianetnews.com           | 87,544             | 0.7          |
| Wikipedia                         | 45,134             | 0.5          |
| Panju Magazine                     | 8,502              | 0.17         |
| Kenda Sampige                     | 912                | 0.005        |
| Public TV                        | 1,200,000          | 5.6          |
| Vijayavani                        | 84,352             | 0.67         |
| BK Murli                         | 2,700              | 0.009        |
| Kannada Sahitya                   | 780                | 0.003        |
| Varta Bharati                    | 43,432             | 0.18         |
| Sumanasa                         | 50,434             | 0.49         |
| Udayavani                        | 52,013             | 0.64         |
| **Total Scraped**                | **2,365,486**      | **14.447**   |
| ai4 sangraha                      | 3,297,146          | 18.2         |
| CulturaX                          | 1                  | 9.25         |
| MC4                               | 1                  | 6.96         |
| Samanantar                        | 1                  | 0.57         |
| **Total**                        | **5,662,635**      | **49.427**   |
### Data Cleaning

A custom Kannada bad-word dictionary was used to filter out articles with inappropriate content such as offensive language, hate speech, and abusive material.
The list of bad words used is stored in kannada_bad_words.txt and the script used for cleaning is in data_cleaning.py



| Sources                           | Number of Articles | Volume (GBs) |
|-----------------------------------|--------------------|--------------|
| www.prajavani.net                 | 51,608             | 0.36         |
| zeenews.india.com/kannada        | 3,046              | 0.023        |
| www.kannadaprabha.com             | 28,515             | 0.154        |
| kannada.oneindia.com              | 542,199            | 3.935        |
| www.justkannada.in                | 82,237             | 0.464        |
| https://vishwavani.news           | 33,489             | 0.274        |
| eesanje.com                       | 11,044             | 0.069        |
| www.sanjevani.com                 | 24,140             | 0.138        |
| kannada.asianetnews.com           | 85,691             | 0.69         |
| Wikipedia                         | 45,134             | 0.5          |
| Panju Magazine                     | 8,502              | 0.17         |
| Kenda Sampige                     | 912                | 0.005        |
| Public TV                        | 1,200,000          | 5.6          |
| Vijayavani                        | 84,352             | 0.67         |
| BK Murli                         | 2,700              | 0.009        |
| Kannada Sahitya                   | 780                | 0.003        |
| Varta Bharati                    | 43,432             | 0.18         |
| Sumanasa                         | 50,434             | 0.49         |
| Udayavani                        | 52,013             | 0.64         |
| **Total Scraped**                | **2,350,228**      | **14.374**   |
| ai4 sangraha                      | 3,297,146          | 18.2         |
| CulturaX                         | 1                  | 9.25         |
| MC4                               | 1                  | 6.96         |
| Samanantar                        | 1                  | 0.57         |
| **Total**                         | **5,647,377**      | **49.354**   |


### Deduplication Statistics

After cleaning, we applied deduplication techniques to ensure no duplicate articles remained in the dataset.

| Sources                           | Number of Articles | Volume (GBs) |
|-----------------------------------|--------------------|--------------|
| www.prajavani.net                 | 49,165             | 0.347        |
| zeenews.india.com/kannada        | 3,046              | 0.023        |
| www.kannadaprabha.com             | 26,913             | 0.149        |
| kannada.oneindia.com              | 237,525            | 1.48         |
| www.justkannada.in                | 38,748             | 0.189        |
| https://vishwavani.news           | 32,418             | 0.265        |
| eesanje.com                       | 10,381             | 0.064        |
| www.sanjevani.com                 | 23,603             | 0.135        |
| kannada.asianetnews.com           | 75,662             | 0.6          |
| Wikipedia                         | 42,834             | 0.46         |
| Panju Magazine                     | 8,314              | 0.14         |
| Kenda Sampige                     | 593                | 0.002        |
| Public TV                        | 285,764            | 1.2          |
| Vijayavani                        | 83,000             | 0.6          |
| BK Murli                         | 2,700              | 0.009        |
| Kannada Sahitya                   | 780                | 0.003        |
| Varta Bharati                    | 27,500             | 0.1          |
| Sumanasa                         | 42,834             | 0.45         |
| Udayavani                        | 30,358             | 0.35         |
| **Total Scraped**                | **991,780**        | **6.566**    |
| ai4 sangraha                      | 3,297,146          | 18.2         |
| CulturaX                          | 1                  | 9.25         |
| MC4                               | 1                  | 6.96         |
| Samanantar                        | 1                  | 0.57         |
| **Total**                        | **4,288,929**      | **41.546**   |

