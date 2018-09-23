# import a dictionary of phrases
# which will 'spice up' user input
# to make it more 'SEO-like'


def import_spice(file_path):
    '''get dict of lines from .txt fime'''

    # make a list of SEO buzzwords from \n-delimited text file  
    with open(file_path, 'r') as file:
        spice = [line.strip() for line in file]
    
    return spice

# add 'spice' phrases to raw text to make it 'SEOfied'
def seofy_text(raw_text, spice):
    '''takes some lines of text, spices them up with SEO stuff and returns as a list'''
    seofied_text = []

    for line in raw_text.split('\n'):
        line = line.strip()
        for spice_phrase in spice:
            seofied_text.append(f"{line} {spice_phrase}")
        seofied_text.append(line)
    
    return seofied_text
