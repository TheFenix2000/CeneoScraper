# CeneoScraper
A simple web scrapper written in python

## Table of CSS Selectors and Variable Names

| **Składowa** | **Nazwa** | **Selektor** |
| --- | --- | --- |
| **Opinia** | opinion | div.js\_product-review |
| **Identyfikator opinii** | opinion\_id | [data-entry-id] |
| **Autor** | author | span.user-post\_\_author-name |
| **Rekomendacja** | recommendation | span.user-post\_\_author-recomendation \> em |
| **Liczba gwiazdek** | score | span.user-post\_\_score-count |
| **Czy opinia jest potwierdzona zakupem** | purchased | div.review-pz |
| **Data wystawienia opinii** | opinion\_date | span.user-post\_\_published \> time:nth-child(1)[datetime] |
| **Data zakupu produktu** | purchase\_date | span.user-post\_\_published \> time:nth-child(2)[datetime] |
| **Ile osób uznało opinię za przydatną** | likes | button.vote-yes[data-total-vote] |
| **Ile osób uznało opinię za nieprzydatną** | dislikes | button.vote-no[data-total-vote] |
| **Treść opinii** | content | div.user-post\_\_text |
| **Wady** | cons | div.review-feature\_\_title—negatives ~ review-feature\_\_item |
| **Zalety** | pros | div.review-feature\_\_title—positives ~ review-feature\_\_item |

## Required libraries
- Requests
- BeautifulSoup
- Os
- Json
- Pandas
- Matplotlib
- Numpy