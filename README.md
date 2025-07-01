# JSintoPDF
python based js embedding into pdf tool


## USAGE
```bash
python embed_js.py yourpdf.py yourjs.js yournewpdf.pdf
```

## !!
add app. before every line of js example:
```js
alert('youralert');
```
should be:
```js
app.alert('youralert');
```
