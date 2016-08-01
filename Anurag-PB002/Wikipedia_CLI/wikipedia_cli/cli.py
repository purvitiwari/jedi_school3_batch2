import click
import wikipedia
import codecs
import os


@click.command()
@click.option('--query', '-q', prompt='Search',
              help='Wikipedia article to search')
@click.option('--log-filename', default='wikipedia_cli.log',
              help='Path to log file to log queries')
def main(query, log_filename):
    """Search wikipedia articles on your terminal"""
    results =  wikipedia.search(query, results=10)

    if not results:
        print 'No results found'
        return

    for idx, val in enumerate(results):
        print "%d. %s" % (idx + 1, val)
    print "\n-1 to exit"

    total_results = len(results)
    choice = 0
    while not (1 <= choice <= total_results) and choice != -1:
        try:
            choice = int(raw_input("Choose from the above results: "))
        except ValueError:
            continue

    if choice == -1:
        return

    page = wikipedia.page(results[choice - 1])
    pipe = os.popen('less', 'w')
    pipe.write(codecs.encode(page.content, 'utf-8'))
    pipe.close()
    with open(log_filename, "a") as log_file:
        log_file.write(page.url)
