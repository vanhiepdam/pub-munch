import argparse

from . import pubCrawlLib


def download_pmid(pmid, config={}, return_info=False):
    print(pmid, "Downloading meta")
    meta = pubCrawlLib.downloadPubmedMeta(str(pmid))
    print(pmid, "Downloading oneDoc")
    if return_info:
        print(pmid, "Getting info as well")
        pdf_file, crawl_info = pubCrawlLib.crawlOneDoc(meta, doc_type='pdf', config=config, return_info=return_info)
        return pdf_file, crawl_info
    else:
        pdf_file = pubCrawlLib.crawlOneDoc(meta, doc_type='pdf', config=config, return_info=return_info)
        return pdf_file


def download_pmid_program():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('pmid', type=int, help='The pubmed id to download')

    parser.add_argument('--elsevier_key', type=str, help='The pubmed id to download')

    parser.add_argument('--sfx_server', type=str, help='The pubmed id to download')

    args = parser.parse_args()

    print(args)

    config = {}

    if args.elsevier_key is not None:
        config['elsevierApiKey'] = args.elsevier_key

    if args.sfx_server is not None:
        config['crawlSfxServer'] = args.sfx_server

    pdf_file = download_pmid(args.pmid, config=config)

    with open('{}.pdf'.format(args.pmid), 'wb') as file:
        file.write(pdf_file)
