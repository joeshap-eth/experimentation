## To start the locally running light node run:
```console
geth.exe --syncmode light --http
```
from the location where geth.exe lives. For example C:\Program Files\Geth

## To run the python once the node is running:
run testing_get_nft_info.py in visual studio code with the play button.
can alternatively run other files or run in console with
```console
python testing_get_nft_info.py
```

note* Not python3. Not sure why. I seem to have set things up such that python is the correct python3 to use.

## Future enhancements and ideas
- Connect this with openAI GPT api to generate a fight based on two token ids.
- Give users more freedom on which attributes are referenced. 
    - Perhaps allow users to choose up to 4 attributes.
- Perhaps create a web page view where this all renders. Or somehow expose this, even if it's only available when I'm running it.
- Maybe there is something I can do with this related to mutant hounds or apecoin.
- Run the node in AWS so it's always up