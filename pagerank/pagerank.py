import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    probability_distribution = {}

    # Calculate the probability to choose a link from the current page
    if page in corpus and len(corpus[page]) > 0:
        for linked_page in corpus:
            if linked_page in corpus[page]:
                probability_distribution[linked_page] = damping_factor / \
                    len(corpus[page])
            else:
                probability_distribution[linked_page] = 0
    else:
        # If the current page has no outgoing links, choose any page with equal probability
        for linked_page in corpus:
            probability_distribution[linked_page] = 1 / len(corpus)

    # Add the probability to choose any page at random
    random_prob = (1 - damping_factor) / len(corpus)
    for linked_page in corpus:
        probability_distribution[linked_page] += random_prob

    return probability_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_rank = {page: 0 for page in corpus}
    current_page = random.choice(list(corpus.keys()))

    # assign page ranks
    for _ in range(n):
        page_rank[current_page] += 1
        transition_probabilities = transition_model(
            corpus, current_page, damping_factor)
        next_page = random.choices(
            list(corpus.keys()), weights=transition_probabilities.values())[0]
        current_page = next_page

    total_samples = sum(page_rank.values())
    normalised_page_rank = {}

    for page, rank in page_rank.items():
        normalised_value = rank / total_samples
        normalised_page_rank[page] = normalised_value

    page_rank = normalised_page_rank

    return page_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    num_pages = len(corpus)
    initial_rank = 1 / num_pages
    page_rank = {page: initial_rank for page in corpus}
    threshold = 0.001

    while True:
        new_page_rank = {}
        for page in corpus:
            rank_sum = 0.0

            # Iterate linking pages
            for linking_page in corpus:
                if page in corpus[linking_page]:
                    rank_sum += page_rank[linking_page] / \
                        len(corpus[linking_page])
            new_rank = (1 - damping_factor) / num_pages + \
                damping_factor * rank_sum
            new_page_rank[page] = new_rank

        # Check for convergence
        max_diff = 0.0
        for page in corpus:
            diff = abs(new_page_rank[page] - page_rank[page])
            max_diff = max(max_diff, diff)

        if max_diff < threshold:
            break

        page_rank = new_page_rank

    return page_rank


if __name__ == "__main__":
    main()
