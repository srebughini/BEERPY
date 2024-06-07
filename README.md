<p align="center">
  <a href="https://imgur.com/Wr2BsNb"><img src="https://i.imgur.com/Wr2BsNbm.png" title="source: imgur.com" /></a>
</p>
<p align="center">
  <a href="https://anaconda.org/ASALIcode/beerpy"><img alt="Conda" src="https://img.shields.io/conda/pn/asalicode/beerpy?color=orange&style=popout-square"></a>
  <a href="https://anaconda.org/ASALIcode/beerpy"><img alt="Conda (channel only)" src="https://img.shields.io/conda/vn/asalicode/beerpy?color=blue&style=popout-square"></a>
  <a href="https://anaconda.org/ASALIcode/beerpy"><img alt="Conda - License" src="https://img.shields.io/conda/l/asalicode/beerpy?style=popout-square"></a>
  <a href="https://anaconda.org/ASALIcode/beerpy"><img alt="Conda" src="https://img.shields.io/conda/dn/asalicode/beerpy?style=popout-square"></a>
  <img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/srebughini/BEERPY?style=flat-square">
  <a href="https://github.com/srebughini/BEERPY/stargazers"><img src="https://img.shields.io/github/stars/srebughini/BEERPY.svg?style=popout-square"></a>
</p>

## 1. Installation
**beerpy** is part of the [ASALI](https://srebughini.github.io/ASALI/) project and it is a **Python** library to get **beer related quotes** in different languages. You can check some of them [here](https://srebughini.github.io/BEERQ/).  
Its [conda package](https://www.anaconda.com/) can be installed as follow:

```bash
conda install -c conda-forge asalicode::beerpy
```  

## 2. Examples
The use of **beerpy** is pretty straightforward, but here you can find an example that might help:  

```javascript
import beerpy as bp

// Generate beer quotes object with the language of your website
let beerQuote = BeerQuote("eng");

// Extract list of authors
let authorList = beerQuote.getAuthorList();

// Extract a random quote
let randomQuote = beerQuote.getRandomQuote();

// Extract quotes of a specific author
let authorQuotes = beerQuote.getQuotesFromAuthor("Benjamin Franklin");

// Extract a random quote of a specific author
let randomAuthorQuote = beerQuote.getRandomQuoteFromAuthor("W. C. Fields");
```

## 3. Contacts
If you want to contribute, ask questions, report bugs or just *drink a beer* with us feel free to open an [issue](https://github.com/srebughini/BEERPY/issues).
