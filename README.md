<p align="center">
  <a href="https://imgur.com/Wr2BsNb"><img src="https://i.imgur.com/Wr2BsNbm.png" title="source: imgur.com" /></a>
</p>
<p align="center">
  <a href="https://anaconda.org/ASALIcode/beerpy"><img alt="Conda" src="https://img.shields.io/conda/pn/asalicode/beerpy?color=orange&style=popout-square"></a>
  <a href="https://anaconda.org/ASALIcode/beerpy"><img alt="Conda (channel only)" src="https://img.shields.io/conda/vn/asalicode/beerpy?color=blue&style=popout-square"></a>
  <a href="https://anaconda.org/ASALIcode/beerpy"><img alt="Conda - License" src="https://img.shields.io/conda/l/asalicode/beerpy?style=popout-square"></a>
  <a href="https://anaconda.org/ASALIcode/beerpy"><img alt="Conda" src="https://img.shields.io/conda/dn/asalicode/beerpy?style=popout-square"></a>
  <a href="https://www.codefactor.io/repository/github/srebughini/beerpy"><img src="https://www.codefactor.io/repository/github/srebughini/beerpy/badge" alt="CodeFactor" /></a>
</p>

## 1. Installation
**beerpy** is part of the [ASALI](https://srebughini.github.io/ASALI/) project and it is a **Python** library to get **beer related quotes** in different languages. You can check some of them [here](https://srebughini.github.io/BEERQ/).  
Its [conda package](https://www.anaconda.com/) can be installed as follow:

```bash
conda install asalicode::beerpy
```  

## 2. Examples
The use of **beerpy** is pretty straightforward, but here you can find an example that might help:  

```python
import beerpy as bp

# Extract list of authors
author_list = bp.get_author_list()

# Extract a random quote
random_quote = bp.get_random_quote(language="eng")

# Extract quotes of a specific author
author_quotes = bp.get_quotes_from_author("Benjamin Franklin")

# Extract a random quote of a specific author
random_author_quote = bp.get_random_quote_from_author("W. C. Fields")
```

## 3. Contacts
If you want to contribute, ask questions, report bugs or just *drink a beer* with us feel free to open an [issue](https://github.com/srebughini/BEERPY/issues).
