import pandas as pd

'''
# Complex examples of pandas Series to challenge your understanding and expand your skillset:

1. Filtering & Grouping:
'''
# Filter a series based on multiple conditions:
fruits = pd.Series(['apple', 'banana', 'orange', 'grapefruit', 'kiwi'],
                  index=[1999, 2000, 2001, 2002, 2003])
filtered_fruits = fruits[(fruits.index > 2000) & (fruits.str.len() > 6)]
print(filtered_fruits)

# Group a series by categorical values and apply functions:
temperatures = pd.Series([25, 28, 30, 22, 27], index=['London', 'Paris', 'Rome', 'London', 'Paris'])
grouped_temps = temperatures.groupby(temperatures.index.str.capitalize()).agg(['mean', 'max', 'min'])
print(grouped_temps)

'''
2. String manipulation:
'''
# Extract parts of strings:
website_urls = pd.Series(['https://www.example.com/blog/post1',
                          'http://www.anothersite.net/page',
                          'https://example.org/news/article'])
domains = website_urls.str.extract('https?://(www\.)?([^/]+)\.')
print(domains)

# Clean and normalize text data:
reviews = pd.Series(['Great movie! #mustwatch', 'Not bad, could be better.', 'Terrible acting, avoid!'])
cleaned_reviews = reviews.str.lower().str.replace('[^\w\s]', '').str.strip()
print(cleaned_reviews)

'''
3. Combining Series:
'''
# Concatenate Series with different indices:
fruits_1 = pd.Series(['apple', 'banana'], index=['a', 'b'])
fruits_2 = pd.Series(['orange', 'grapefruit'], index=[1, 2])
combined_fruits = pd.concat([fruits_1, fruits_2], ignore_index=True)
print(combined_fruits)

'''
Advanced Indexing:
'''
# boolean indexing for complex filtering:
data = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
filtered_data = data[(data % 2 == 0) & (data.index.str.isalpha())]
print(filtered_data)

# Index Series with another Series:
names = pd.Series(['Alice', 'Bob', 'Charlie'])
ages = pd.Series([25, 30, 28], index=['Bob', 'Alice', 'Charlie'])
  # reindexing the 'names' series according to the index of the 'ages'
  # There's actually no point in doing that :) . It is just to show that what `.reindex()` does
indexed_names = names.reindex(ages.index)
print(indexed_names, end='\n\n')
  # filling any missing values with 'Charlie'
indexed_names = names.reindex(index=ages.index, fill_value='Charlie')
print(indexed_names)
  # performing an operation similar to set_index of DataFrame
  # more precisely, I'm just copying the values from `names` to a new Series with the index from `ages`
indexed_names = pd.Series(names.values, index=ages.index)
print(indexed_names)
