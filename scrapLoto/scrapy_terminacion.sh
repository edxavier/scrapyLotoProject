#!/bin/bash


cd /root/scrapy/
source env/bin/activate
cd /root/scrapy/scrapyLotoProject/scrapLoto
scrapy crawl terminacion --nolog