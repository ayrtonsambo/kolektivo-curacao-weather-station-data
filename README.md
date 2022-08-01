# kolektivo-curacao-geonft-weatherstations
This repository contains building blocks for the off-chain to on-chain weather station data feed. The 'Virtual Environment' file consists of code that creates a virtual environment which is very much needed to request from API. 

The 'PWS API Current observations' file retrieves the daily observations from Wunderground, writes that data to CSV and uploads it daily to IPFS. A lot of steps were derived from the IPFS shipyard gitHub: https://github.com/ipfs-shipyard/py-ipfs-http-client.
Code is written in Python

For most of the code here, it's best advised to create a virtual environment. The seteps below show how to create one with Jupyter Notebook.
- Open Anaconda prompt
- Run:
 
<sub> py -m venv <environment_name>

 .\<environment_name>\Scripts\activate </sub>
- Open Jupyter Notebook
 
  
