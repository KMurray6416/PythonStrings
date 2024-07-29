    # Task 1

reviews_list = ["This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]

reviews_list = [s.replace('good','GOOD') for s in reviews_list]
reviews_list = [s.replace('excellent','EXCELLENT') for s in reviews_list]
reviews_list = [s.replace('bad','BAD') for s in reviews_list]
reviews_list = [s.replace('poor','POOR') for s in reviews_list]
reviews_list = [s.replace('average','AVERAGE') for s in reviews_list]

for review in reviews_list:
    print(f"\n{review}")

    # Task 2

positive_words = ['good','good.', 'excellent', 'excellent.', 'great', 'awesome', 'fantastic', 'superb', 'amazing']
negative_words = ['bad', 'poor', 'terrible', 'horrible', 'awful', 'disappointing', 'subpar']

def sentiment_tally(reviews, pos_words, neg_words):

    results = []

    for review in reviews:
        positive_count = 0
        negative_count = 0
      
        words = review.lower().split()
        for word in words:
            if word in pos_words:
                positive_count += 1
            elif word in neg_words:
                negative_count += 1
        
        results.append((positive_count, negative_count))

    return results

review_tally = sentiment_tally(reviews_list,positive_words,negative_words)

for review, (positive_count, negative_count) in zip(reviews_list, review_tally):
    print(f"\nReview: \"{review}\" \nPositive words: \"{positive_count}\" \nNegative words: \"{negative_count}\n")

    # Task 3

def summary_of_reviews(reviews):
        if len(review) <= 30:
            return review
        summary_cut = review.rfind(' ', 0, 30)
        if summary_cut == -1:
            summarized = review[:30]
        else:
            summarized = review[:summary_cut]

        return summarized + "..."

for review in reviews_list:
    print(summary_of_reviews(reviews_list))