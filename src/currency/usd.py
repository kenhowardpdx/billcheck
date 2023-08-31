import locale

locale.setlocale(locale.LC_ALL, "")

def usd(n):
    return locale.currency(n, grouping=True)
