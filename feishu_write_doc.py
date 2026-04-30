#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直接以数据对象形式定义，绕过字符串引号冲突
"""
import requests
import json
import sys
import time
from datetime import datetime, timedelta

APP_ID = "cli_a93d483f6ff81bca"
APP_SECRET = "CU3EPesfCzNayK4bqsnh6droaJsf4HV8"
TENANT_DOMAIN = "wcn5jx0ifkx3.feishu.cn"

yesterday_cn = (datetime.now()).strftime('%Y\u5e74%m\u6708%d\u65e5')
today_date = (datetime.now()).strftime('%Y-%m-%d')
SECTIONS = [
    {'title': '\u4e00\u3001\u6d77\u6d0b\u4eba\u5de5\u667a\u80fd', 'en': 'Ocean AI / Marine Artificial Intelligence', 'items': [
        {'title': '1. NOAA NCEI\uff082026-04-13\uff09\uff1aAI\u8d4b\u80fdNOAA\u5168\u7403\u6e29\u5ea6\u6570\u636e\u96c6\u2014\u2014NOAAGlobalTemp v6.1.0\u5168\u9762\u8f6c\u578b\u4eba\u5de5\u795e\u7ecf\u7f51\u7edc', 'badge': '\u8fd17\u5929', 'abstract': 'NOAA\u56fd\u5bb6\u73af\u5883\u4fe1\u606f\u4e2d\u5fc3\uff08NCEI\uff09\u53d1\u5e03NOAAGlobalTemp v6.1.0\uff0c\u8be5\u7248\u672c\u5b8c\u5168\u57fa\u4e8e\u4eba\u5de5\u795e\u7ecf\u7f51\u7edc\uff08ANN\uff09\u65b9\u6cd5\uff0c\u6574\u5408\u65b0\u53d1\u5e03\u7684ERSST v6\uff0c\u4ece\u9646\u5730\u6c14\u6e29\u5230\u6d77\u8868\u6e29\u5ea6\u5168\u9762\u91c7\u7528AI\u91cd\u5efa\uff0c\u8986\u76d61850\u5e74\u81f3\u4eca\u5168\u5386\u53f2\u8bb0\u5f55\u3002\u8be5\u6570\u636e\u96c6\u88abWMO\u548cBAMS\u5e7f\u6cdb\u7528\u4e8e\u6c14\u5019\u76d1\u6d4b\u4e0e\u8bc4\u4f30\u3002', 'source': 'NOAA NCEI', 'url': 'https://www.ncei.noaa.gov/news/ai-supercharges-key-noaa-dataset-ensuring-peak-accuracy', 'date': '2026-04-13'},
        {'title': '2. Nature Communications Earth\uff082026-04-06\uff09\uff1aBGC-Argo\u6d6e\u6807\u63ed\u793a\u7f3a\u6c27\u5e26\u6c2e\u78b3\u5faa\u73af\u7684\u5236\u5f0f\u8f6c\u53d8', 'badge': '', 'abstract': '\u53d1\u8868\u4e8eCommunications Earth & Environment\uff0c\u5229\u7528\u90e8\u7f72\u4e8e\u4e1c\u70ed\u5e26\u5317\u592a\u5e73\u6d0b\u7684BGC-Argo\u6d6e\u6807\u8fd1\u4e09\u5e74\u9ad8\u5206\u8fa8\u7387\u8bb0\u5f55\uff0c\u6355\u6349\u5230\u4e9a\u785d\u9178\u76d0\u6d53\u5ea6\u7684\u964d\u4f4e\uff0c\u53cd\u6620\u6c2e\u6c27\u5316\u8fd8\u539f\u5e73\u8861\u7684\u8f6c\u53d8\u3002\u7814\u7a76\u91c7\u7528\u5316\u5b66\u8ba1\u91cf\u8d28\u91cf\u5e73\u8861\u6a21\u578b\u91cf\u5316\u4e86\u53cd\u785d\u5316\u3001\u538c\u6c27\u6c28\u6c27\u5316\u7b49\u6c2e\u8f6c\u5316\u8fc7\u7a0b\u53ca\u5176\u4e0e\u78b3\u9178\u76d0\u5316\u5b66\u7684\u8026\u5408\u3002', 'source': 'Nature Communications Earth & Environment', 'url': 'https://www.nature.com/articles/s43247-026-03410-5', 'date': '2026-04-06'},
        {'title': '3. Nature Geoscience\uff082026-04-13\uff09\uff1aGOFLOW\u6df1\u5ea6\u5b66\u4e60\u6846\u67b6\u5229\u7528\u9759\u6b62\u536b\u661f\u70ed\u7ea2\u5916\u56fe\u50cf\u89e3\u6790\u6d77\u6d0b\u8868\u5c42\u6d41\u573a', 'badge': '', 'abstract': '\u53d1\u8868\u4e8eNature Geoscience\uff0c\u63d0\u51fa\u5730\u7403\u9759\u6b62\u536b\u661f\u6d77\u6d0b\u6d41\u52a8\uff08GOFLOW\uff09\u6df1\u5ea6\u5b66\u4e60\u6846\u67b6\uff0c\u5229\u7528GOES\u536b\u661f\u8fde\u7eed\u70ed\u7ea2\u5916\u5f71\u50cf\u5e8f\u5217\uff0c\u9996\u6b21\u5b9e\u73b0\u5bf9\u6d77\u6d0b\u8868\u5c42\u6d41\u573a\u7684\u5168\u7403\u9ad8\u5206\u8fa8\u7387\u63a2\u6d4b\uff0c\u63ed\u793a\u4e86\u4ee5\u5f80\u96be\u4ee5\u89c2\u6d4b\u7684\u6d77\u6d0b\u6d0b\u6d41\u7ed3\u6784\u3002', 'source': 'Nature Geoscience', 'url': 'https://www.nature.com/articles/s41561-026-01943-0', 'date': '2026-04-13'},
    ]},
    {'title': '\u4e8c\u3001\u6d77\u6d0b\u6570\u5b57\u5b6a\u751f', 'en': 'Ocean Digital Twin', 'items': [
        {'title': '1. OceanPredict\uff082026-04-13/14\uff09\uff1aAI-TT Workshop\u2014\u2014\u673a\u5668\u5b66\u4e60\u6d77\u6d0b\u9884\u62a5\u56fd\u9645\u7814\u8ba8\u4f1a\u8499\u7279\u5229\u5c14\u53ec\u5f00', 'badge': '', 'abstract': 'OceanPredict\u4e8e\u52a0\u62ff\u5927\u8499\u7279\u5229\u5c14\u53ec\u5f00\u201cMachine Learning for Ocean Prediction: Methods, Applications & Challenges\u201d\u56fd\u9645\u7814\u8ba8\u4f1a\uff0c\u6c47\u805a\u516830\u7bc7\u6458\u8981\u7684ML\u6d77\u6d0b\u9884\u62a5\u7814\u7a76\u6210\u679c\u3002\u516d\u5927\u8bae\u9898\u6db5\u76d6ML\u6a21\u62df\u5668\u3001\u6df7\u5408\u65b9\u6cd5\u3001\u6df1\u5ea6\u5b66\u4e60\u8d44\u6599\u540c\u5316\u3001\u8bc4\u4f30\u6311\u6218\u3001\u6280\u672f\u96be\u9898\u548c\u964d\u5c3a\u5ea6\u5e94\u7528\u7b49\u3002', 'source': 'OceanPredict / NOAA / ECMWF', 'url': 'https://oceanpredict.org/events/ai-tt-workshop/', 'date': '2026-04-13'},
        {'title': '2. Frontiers\uff082026-04-24\uff09\uff1a\u6d77\u6d0bAI\u524d\u6cbf\u2014\u2014\u4eba\u5de5\u667a\u80fd\u8d4b\u80fd\u53ef\u6301\u7eed\u6d77\u6d0b\u7814\u7a76\u7efc\u8ff0\u4e13\u9898', 'badge': '\u8fd17\u5929', 'abstract': 'Frontiers\u53d1\u5e03\u300aArtificial Intelligence for Sustainable Oceans\u300b\u7814\u7a76\u4e13\u9898\u7efc\u8ff0\uff0c\u6c47\u96c6\u536b\u661f\u3001\u81ea\u4e3b\u822a\u884c\u5668\u3001\u6cbf\u6d77\u4f20\u611f\u5668\u7f51\u7edc\u4ea7\u751f\u7684\u6d77\u91cf\u6d77\u6d0b\u89c2\u6d4b\u6570\u636e\u7684AI\u89e3\u6790\u65b9\u6cd5\uff0c\u6db5\u76d6\u6d77\u6d0b\u9884\u62a5\u3001\u751f\u7269\u591a\u6837\u6027\u8c03\u67e5\u548c\u6df1\u6d77\u4f5c\u4e1a\u7b49\u524d\u6cbf\u5e94\u7528\u3002', 'source': 'Frontiers in Marine Science', 'url': 'https://www.frontiersin.org/research-topics/80289/artificial-intelligence-for-sustainable-oceans', 'date': '2026-04-24'},
    ]},
    {'title': '\u4e09\u3001\u6d77\u6d0b\u53ef\u89c6\u5316', 'en': 'Ocean Visualization', 'items': [
        {'title': '1. NOAA NCEI\uff082026-04-22\uff09\uff1a\u6d77\u5e95\u5730\u5f62\u6570\u636e\u67e5\u770b\u5668\u91cd\u5927\u5347\u7ea7\u2014\u2014\u54cd\u5e94\u5f0f\u8bbe\u8ba1\u4e0e\u79fb\u52a8\u7aef\u4f18\u5316', 'badge': '\u8fd17\u5929', 'abstract': 'NOAA NCEI\u4e8e2026\u5e742\u6708\u5b8c\u6210Bathymetric Data Map Viewer\u91cd\u5927\u5347\u7ea7\uff0c\u65b0\u7248\u67e5\u770b\u5668\u63d0\u4f9b\u66f4\u7075\u654f\u7684\u54cd\u5e94\u5f0f\u8bbe\u8ba1\u3001\u589e\u5f3a\u7684\u79fb\u52a8\u7aef\u4f53\u9a8c\u3001\u66f4\u5f3a\u5927\u7684\u641c\u7d22\u7b5b\u9009\u529f\u80fd\u548c\u6539\u5584\u7684\u65e0\u969c\u788d\u8bbf\u95ee\u3002\u95e8\u6237\u6574\u5408\u591a\u6ce2\u675f\u3001\u5355\u6ce2\u675f\u3001NOS\u6c34\u6587\u6d4b\u91cf\u3001\u4f17\u5305\u6d77\u5e95\u5730\u5f62\u7b49\u6570\u636e\u3002', 'source': 'NOAA NCEI', 'url': 'https://www.ncei.noaa.gov/news/explore-sea-floor-ncei-modernized-portal', 'date': '2026-04-22'},
        {'title': '2. OBIS\uff082026-04-29\uff09\uff1aNode Spotlight\u2014\u2014\u5370\u5ea6\u6d0b\u751f\u7269\u591a\u6837\u6027\u4fe1\u606f\u7cfb\u7edf\uff08IndOBIS\uff09\u63a8\u8fdb\u6570\u636e\u534f\u8c03', 'badge': '\u8fd17\u5929', 'abstract': 'OBIS\u53d1\u5e03Node Spotlight\u7cfb\u5217\uff0c\u805a\u7126\u5370\u5ea6\u6d0b\u751f\u7269\u591a\u6837\u6027\u4fe1\u606f\u7cfb\u7edf\uff08IndOBIS\uff09\u8282\u70b9\uff0c\u4ecb\u7ecd\u5176\u5728\u5370\u5ea6\u6d0b\u533a\u57df\u6d77\u6d0b\u751f\u7269\u591a\u6837\u6027\u6570\u636e\u534f\u8c03\u65b9\u9762\u7684\u8fdb\u5c55\u3002OBIS\u76ee\u524d\u5df2\u6c47\u805a1.77\u4ebf\u6761\u7269\u79cd\u89c2\u6d4b\u8bb0\u5f55\u3001\u8986\u76d620.4\u4e07\u79cd\u6d77\u6d0b\u7269\u79cd\u3001\u62e5\u670937\u4e2a\u5168\u7403\u8282\u70b9\u3002', 'source': 'OBIS', 'url': 'https://portal.obis.org/2026/04/29/node-spotlight-indobis/', 'date': '2026-04-29'},
    ]},
    {'title': '\u56db\u3001\u6d77\u6d0b\u6570\u636e\u8d28\u91cf', 'en': 'Ocean Data Quality / QA/QC', 'items': [
        {'title': '1. Journal of Oceanography\uff082026-04-29\uff09\uff1a\u57fa\u4e8e\u8def\u5f84\u7b7e\u540d\u7684Argo\u5256\u9762\u81ea\u52a8\u5316\u8d28\u91cf\u63a7\u5236\u6539\u8fdb\u65b9\u6cd5', 'badge': '\u8fd17\u5929', 'abstract': '\u53d1\u8868\u4e8eJournal of Oceanography\uff08Springer\uff09\uff0c\u4ecb\u7ecd\u7528\u4e8eArgo\u5256\u9762\u81ea\u52a8\u5316\u9519\u8bef\u68c0\u6d4b\u7684\u65b0\u6d41\u7a0b\uff0c\u878d\u5165\u65b0\u7684\u673a\u5668\u5b66\u4e60\u6280\u672f\u3002\u7814\u7a76\u8868\u660e\uff0c\u4f7f\u75282016\u5e74\u6570\u636e\u8bad\u7ec3\u7684\u6a21\u578b\u4e0e2022\u5e74\u6570\u636e\u8bad\u7ec3\u7684\u6a21\u578b\u6027\u80fd\u76f8\u5f53\uff0c\u80fd\u4ee5\u63a5\u8fd1Argo\u6570\u636e\u4e2d\u5fc3\u7684\u6c34\u5e73\u8bc6\u522b\u9519\u8bef\u5256\u9762\u3002', 'source': 'Journal of Oceanography / Springer', 'url': 'https://link.springer.com/article/10.1007/s10872-026-00791-1', 'date': '2026-04-29'},
        {'title': '2. OBIS\uff082026-04-15\uff09\uff1a\u6807\u51c6\u5316\u4e0eFAIR\u2014\u2014\u91ca\u653e\u8fd175\u5e74\u7684\u9c7c\u7c7b\u5e7c\u4f53\u548c\u9c7c\u5375\u8bb0\u5f55', 'badge': '', 'abstract': 'OBIS\u62a5\u9053CalCOFI Fish Larvae & Egg Tows\u6570\u636e\u96c6\u6210\u529f\u6574\u5408\u5165\u5168\u7403\u6d77\u6d0b\u751f\u7269\u591a\u6837\u6027\u6570\u636e\u94fe\uff0c\u8fd175\u5e74\u7684\u9c7d\u9c7c\u5e7c\u4f53\u548c\u9c7c\u5375\u8bb0\u5f55\u7ecf\u6807\u51c6\u5316\u5904\u7406\u540e\u7b26\u5408FAIR\u539f\u5219\uff0c\u73b0\u53ef\u901a\u8fc7GBIF\u548cOBIS\u5168\u7403\u83b7\u53d6\u3002\u8be5\u6570\u636e\u96c6\u6db5\u76d6\u52a0\u5dde\u6cbf\u6d77\u8d85\u8fc775\u5e74\u7684\u7cfb\u7edf\u91c7\u6837\u8bb0\u5f55\uff0c\u662f\u76ee\u524d\u6700\u5e7f\u6cdb\u7684\u9c7d\u5f62\u6d6e\u6e38\u751f\u7269\u65f6\u95f4\u5e8f\u5217\u4e4b\u4e00\u3002', 'source': 'OBIS / CalCOFI', 'url': 'https://portal.obis.org/2026/04/15/fish-egg-larvae-dataset-calcofi/', 'date': '2026-04-15'},
    ]},
    {'title': '\u4e94\u3001\u6d77\u6d0b\u6570\u636e\u5904\u7406', 'en': 'Ocean Data Processing', 'items': [
        {'title': '1. Copernicus Marine\uff082026-04-21\uff09\uff1aCopernicus Marine Toolbox v2.4.0\u53d1\u5e03\u2014\u2014\u652f\u6301\u7a00\u758f\u6570\u636e\u96c6\u4e0eCSV\u5bfc\u51fa', 'badge': '\u8fd17\u5929', 'abstract': 'Copernicus Marine Toolbox v2.4.0\u4e8e2026\u5e744\u670821\u65e5\u53d1\u5e03\uff0c\u4e3b\u8981\u66f4\u65b0\u5305\u62ec\uff1a\u6700\u4f4e\u652f\u6301Python 3.10\u3001\u65b0\u589e\u7a00\u758f\u6570\u636e\u96c6NetCDF\u683c\u5f0f\u5b50\u96c6\u63d0\u53d6\u3001\u5bc6\u96c6\u6570\u636e\u96c6CSV\u683c\u5f0f\u5bfc\u51fa\u3001\u5146\u8bc1\u590d\u7528\u4f18\u5316\u767b\u5f55\u6d41\u7a0b\u3001\u517c\u5bb9pandas>=3.0.0\u3002\u4fee\u590d\u4e86\u7a00\u758f\u6570\u636e\u96c6\u4e0b\u8f7d\u5931\u8d25\u548c\u7a7a\u6587\u4ef6\u751f\u6210\u95ee\u9898\u3002', 'source': 'Copernicus Marine Service', 'url': 'https://help.marine.copernicus.eu/en/articles/8218641-next-milestones-and-roadmap', 'date': '2026-04-21'},
        {'title': '2. CMEMS\uff082026-04-08\uff09\uff1a\u5fb7\u56fd\u6d77\u5e73\u9762\u65f6\u95f4\u5e8f\u5217\u56de\u6eaf\u81f31990\u5e74\u4ee3\u5e76\u7edf\u4e00\u57fa\u51c6', 'badge': '', 'abstract': 'Copernicus Marine Service\u53d1\u5e03INS-788\u66f4\u65b0\uff0c\u5c06\u5fb7\u56fd\u6d77\u5e73\u9762\u65f6\u95f4\u5e8f\u5217\u56de\u6eaf\u81f31990\u5e74\u4ee3\uff0c\u7edf\u4e00\u57fa\u51c6\u81f3DHHN2016\uff08\u6ce2\u7f57\u7684\u6d77\u533a\u57df\u4e3aBSCD2000\uff09\uff0c\u4fee\u590d\u4e862019\u5e74\u524d\u540e\u57fa\u51c6\u4e0d\u4e00\u81f4\u95ee\u9898\uff0c\u5f71\u54cd\u591a\u4e2a\u539f\u4f4d\u4ea7\u54c1\u3002', 'source': 'Copernicus Marine Service', 'url': 'https://marine.copernicus.eu/user-corner/user-notification-service?field_category=27', 'date': '2026-04-08'},
        {'title': '3. NMFS HackDays\uff082026-04-17\uff09\uff1aERDDAP with xarray\u6559\u7a0b\u2014\u2014\u6d77\u8868\u6e29\u5ea6\u4e0e\u53f6\u7eff\u7d20\u8f68\u8ff9\u5339\u914d\u5206\u6790', 'badge': '', 'abstract': 'NOAA NMFS HackDays 2026\u7b2c\u56db\u671fxarray\u7cfb\u5217\u6559\u7a0b\uff082026-04-17\uff09\uff0c\u6db5\u76d6ERDDAP\u5165\u95e8\u3001\u7528xarray\u521b\u5efa\u6570\u636e\u7acb\u65b9\u4f53\u5e76\u8fdb\u884c\u7a7a\u95f4\u65f6\u95f4\u5e73\u5747\u8ba1\u7b97\u3001\u4ee5\u53ca\u4f7f\u7528ERDDAP\u6570\u636e\u83b7\u53d6\u6d77\u9f9f\u8f68\u8ff9\u6cbf\u7ebf\u7684\u6d77\u8868\u6e29\u5ea6\u548c\u53f6\u7eff\u7d20\u6570\u636e\u3002', 'source': 'NMFS Open Science', 'url': 'https://nmfs-opensci.github.io/NMFSHackDays-2026/topics/2026-04-17/', 'date': '2026-04-17'},
    ]},
    {'title': '\u516d\u3001\u6d77\u6d0b\u6570\u636e\u7ba1\u7406\u4e0e\u5171\u4eab\u670d\u52a1', 'en': 'Ocean Data Management & Sharing', 'items': [
        {'title': '1. UNESCO/IOC\uff082026-04-13\uff09\uff1a\u6d77\u6d0b\u5341\u5e74\u516c\u6c11\u79d1\u5b66\u6570\u636e\u5171\u4eab\u6307\u5357\u53d1\u5e03', 'badge': '', 'abstract': 'UNESCO/IOC\u53d1\u5e03Ocean Decade Citizen Science Data Sharing Guidelines\uff0c\u4e3a\u516c\u6c11\u79d1\u5b66\u6570\u636e\u5171\u4eab\u63d0\u4f9b\u5173\u952e\u539f\u5219\u3001\u73b0\u6709\u6807\u51c6\u3001\u6846\u67b6\u548c\u63a8\u8350\u5b9e\u8df5\uff0c\u65e8\u5728\u6700\u5927\u5316\u516c\u6c11\u79d1\u5b66\u6570\u636e\u4ef7\u503c\u5e76\u89e3\u51b3\u5173\u4e8e\u6570\u636e\u4fe1\u4efb\u3001\u6570\u636e\u7ba1\u7406\u548c\u8d1f\u8d23\u4efb\u5171\u4eab\u7684\u62c5\u5fe7\u3002', 'source': 'UNESCO/IOC Ocean Decade', 'url': 'https://unesdoc.unesco.org/ark:/48223/pf0000397182', 'date': '2026-04-13'},
        {'title': '2. PANGAEA\uff082026-04-28\uff09\uff1aPANGAEA\u6570\u636e\u5e93Event-Campaign Merge\u67b6\u6784\u91cd\u5927\u73b0\u4ee3\u5316\u5347\u7ea7', 'badge': '\u8fd17\u5929', 'abstract': 'PANGAEA\u4e8e2026\u5e744\u670828\u65e5\u542f\u52a8\u6570\u636e\u5e93\u67b6\u6784\u91cd\u5927\u5347\u7ea7\uff0c\u6838\u5fc3\u53d8\u66f4\u4e3aEvent-Campaign Merge\uff0c\u5c06\u6570\u636e\u6536\u96c6\u4e8b\u4ef6\u7684\u5143\u6570\u636e\u67b6\u6784\u4ece\u50f5\u5316\u7684\u5c42\u7ea7\u7ed3\u6784\u8fc1\u79fb\u4e3a\u7075\u6d3b\u7684\u6811\u72b6\u5c42\u7ea7\u7ed3\u6784\uff0c\u652f\u6301\u591a\u7ea7\u5d4c\u5957\u4e8b\u4ef6\u3001\u65b0\u589eLocation 2\u5b57\u6bb5\u652f\u6301\u8f68\u8ff9\u4e8b\u4ef6\u7684\u8d77\u6b62\u70b9\u7cbe\u786e\u5b9a\u4f4d\u3001\u4ee5\u53ca\u4e8b\u4ef6\u7ea7\u522b\u7684\u8d1f\u8d23\u4eba/\u9996\u5e2d\u79d1\u5b66\u5bb6\u4fe1\u606f\u3002\u8fc1\u79fb\u671f\u95f4\u6570\u636e\u641c\u7d22\u548c\u83b7\u53d6\u670d\u52a1\u6b63\u5e38\u8fd0\u884c\u3002', 'source': 'PANGAEA', 'url': 'https://wiki.pangaea.de/wiki/Event-Campaign-Merge', 'date': '2026-04-28'},
    ]},
    {'title': '\u4e03\u3001\u5f00\u653e\u822a\u6b21 / \u8239\u65f6\u5171\u4eab', 'en': 'Open Cruises / Ship Time Sharing', 'items': [
        {'title': '1. Schmidt Ocean Institute\uff082026-04-15/30\uff09\uff1aDeSIGNING THE FUTURE 3\u2014\u2014\u5357\u5927\u897f\u6d0b\u4e2d\u5c42\u6c34\u57df\u751f\u7269\u591a\u6837\u6027\u63a2\u6d4b\u822a\u6b21', 'badge': '\u8fd17\u5929', 'abstract': 'Schmidt Ocean Institute\u4e8e2026\u5e744\u670815\u65e5\u81f330\u65e5\u6267\u884cDeSIGNING THE FUTURE 3\u822a\u6b21\uff0c\u7531\u53f2\u5bc6\u68ee\u5c3c\u56fd\u5bb6\u81ea\u7136\u5386\u53f2\u535a\u7269\u9986\u9996\u5e2d\u79d1\u5b66\u5bb6Karen Osborn\u7387\u961f\uff0c\u8fd0\u7528DeepPIV\u3001EyeRIS\u6210\u50cf\u7cfb\u7edf\u548cRAD\u91c7\u6837\u5668\u63a2\u6d4b\u5357\u5927\u897f\u6d0b\u4e2d\u5c42\u6c34\u57df\u751f\u7269\u591a\u6837\u6027\uff0c\u5e76\u521b\u5efa\u900f\u660e\u751f\u7269\u76844D\u8ba1\u7b97\u673a\u6e32\u67d3\u56fe\u3002', 'source': 'Schmidt Ocean Institute', 'url': 'https://schmidtocean.org/cruises/schmidt-ocean-institute-2026-expeditions/', 'date': '2026-04-15'},
        {'title': '2. Ocean Exploration Trust\uff082026-04-18\uff09\uff1aNautilus 2026\u5e74\u79d1\u5b66\u4e0e\u5de5\u7a0b\u5b9e\u4e60\u751f\u540d\u5355\u516c\u5e03', 'badge': '', 'abstract': 'Ocean Exploration Trust\u5ba3\u5e032026\u5e74\u79d1\u5b66\u4e0e\u5de5\u7a0b\u5b9e\u4e60\u751f\u540d\u5355\uff0c\u516919\u540d\u53c2\u4e0e\u8005\u5165\u9009Nautilus\u63a2\u6d4b\u5b63\u5b9e\u4e60\u8ba1\u5212\uff0c\u5206\u5e03\u5728\u6d77\u6d0b\u79d1\u5b66\u3001ROV\u5de5\u7a0b\u3001\u89c6\u9891\u7cfb\u7edf\u5de5\u7a0b\u3001\u6d77\u5e95\u6d4b\u7ed8\u4e0e\u6c34\u6587\u6d4b\u91cf\u3001\u5bfc\u822a\u4e94\u4e2a\u65b9\u5411\u3002\u52c8\u63a2\u8239Nautilus\u5c06\u5728\u5927\u897f\u6d0b\u6df1\u6d77\u5730\u8d28\u3001\u751f\u7269\u5b66\u548c\u8003\u53e4\u5b66\u63a2\u6d4b\u4e2d\u63d0\u4f9b\u5b9e\u65f6\u76f4\u64ad\u6c34\u4e0b\u63a2\u6d4b\uff0c\u8be5\u9879\u76ee\u7531\u7f8e\u56fd\u6d77\u519b\u7814\u7a76\u529e\u516c\u5ba4STEM\u8ba1\u5212\u8d44\u52a9\u3002', 'source': 'Ocean Exploration Trust / Nautilus Live', 'url': 'https://nautiluslive.org/blog/2026/04/18/congratulations-2026-science-and-engineering-interns', 'date': '2026-04-18'},
    ]},
    {'title': '\u516b\u3001\u6d77\u6d0b\u6570\u636e\u4e2d\u5fc3', 'en': 'Ocean Data Centers', 'items': [
        {'title': '1. GEBCO\uff082026-04-23\uff09\uff1aGEBCO_2026 Grid\u5168\u7403\u6d77\u5e95\u5730\u5f62\u7f51\u683c\u6b63\u5f0f\u53d1\u5e03', 'badge': '\u8fd17\u5929', 'abstract': 'GEBCO\u4e8e2026\u5e744\u670823\u65e5\u53d1\u5e03GEBCO_2026 Grid\uff0c\u662f\u76ee\u524d\u6700\u65b0\u7684\u5168\u7403\u5730\u5f62\u6a21\u578b\uff0c\u63d0\u4f9b15\u5f27\u79d2\u5206\u8fa8\u7387\u7684\u6d77\u6d0b\u4e0e\u9646\u5730\u9ad8\u7a0b\u6570\u636e\uff0c\u5305\u542b\u683c\u9675\u5170\u548c\u5357\u6781\u51b0\u4e0b\u5730\u5f62\u7248\u672c\u3002\u652f\u6301netCDF\u3001GeoTiff\u3001ASCII\u683c\u5f0f\u4e0b\u8f7d\u53caOPeNDAP\u5728\u7ebf\u8bbf\u95ee\uff0c\u5c5e\u4e8e\u516c\u5171\u9886\u57df\u514d\u8d39\u4f7f\u7528\u3002', 'source': 'GEBCO / IHO', 'url': 'https://www.gebco.net/data-products/gridded-bathymetry-data', 'date': '2026-04-23'},
        {'title': '2. EMODnet\uff082026-03-31\uff09\uff1aEMODnet\u53c2\u4e0e\u6b27\u6d32\u6d77\u6d0b\u65e5\u6d3b\u52a8\u2014\u2014OceanEye\u6b27\u6d32\u6d77\u6d0b\u76d1\u6d4b\u5021\u8bae\u53d1\u5e03', 'badge': '', 'abstract': '\u57282026\u5e74\u6b27\u6d32\u6d77\u6d0b\u65e5\u6d3b\u52a8\u671f\u95f4\uff0c\u6b27\u76df\u59d4\u5458\u4f1a\u4e3b\u5e2d\u53d1\u5e03OceanEye\u6b27\u6d32\u6d77\u6d0b\u76d1\u6d4b\u4e0e\u89c2\u6d4b\u5021\u8bae\u3002EMODnet\u4f5c\u4e3a\u6b27\u76df\u6d77\u6d0b\u6570\u636e\u670d\u52a1\u4e2d\u5fc3\u67a2\u7ebd\uff0c\u5c06\u4e3aOceanEye\u63d0\u4f9b\u6570\u636e\u670d\u52a1\u652f\u6491\uff0c\u5df2\u652f\u6301\u6570\u5343\u9879\u539f\u4f4d\u6570\u636e\u6536\u96c6\u5de5\u4f5c\uff0c\u5c06\u539f\u59cb\u6570\u636e\u8f6c\u5316\u4e3aFAIR\u6570\u636e\u548c\u6570\u636e\u4ea7\u54c1\u3002', 'source': 'EMODnet / European Commission', 'url': 'https://emodnet.ec.europa.eu/en/emodnet-european-ocean-days-2026', 'date': '2026-03-31'},
    ]},
    {'title': '\u4e5d\u3001\u5de5\u5177\u4e0e\u4ee3\u7801\u8d44\u6e90', 'en': 'Tools & Code Resources', 'items': [
        {'title': '1. xarray v2026.04.0\uff082026-04-13\uff09\uff1aPython\u591a\u7ef4\u6570\u7ec4\u5904\u7406\u5e93\u53d1\u5e03\u2014\u2014zarr 3.0\u652f\u6301\u4e0e\u6027\u80fd\u4f18\u5316', 'badge': '', 'abstract': 'PyData xarray\u53d1\u5e03v2026.04.0\uff0c\u4e3b\u8981\u53d8\u66f4\u5305\u62ec\uff1azarr\u6700\u4f4e\u652f\u6301\u7248\u672c\u5347\u7ea7\u81f33.0\u3001timedelta\u5f03\u7528\u6e05\u7406\u3001\u65b0\u589ecol_wrap=auto\u7ed8\u56fe\u9009\u9879\u3001DataTree.to_dataset\u65b0\u589einherit\u53c2\u6570\u3001StringDType\u53d8\u91cf\u5199\u5165netCDF\u652f\u6301\u3001dataset\u7d22\u5f15\u6027\u80fd\u6539\u8fdb\u53ca\u591a\u9879bug\u4fee\u590d\u3002', 'source': 'PyData / xarray GitHub', 'url': 'https://github.com/pydata/xarray/releases', 'date': '2026-04-13'}
    ]}
]

def tr(text, bold=False, link=None):
    element = {"text_run": {"content": text}}
    if bold:
        element["text_run"]["style"] = {"bold": True}
    if link:
        element["text_run"]["link"] = {"url": link}
    return element


def paragraph(elements):
    return {"block_type": 2, "text": {"elements": elements, "style": {}}}


def heading(text, level=1):
    prefix = {1: "\u3010", 2: "  >> "}.get(level, "    ")
    suffix = {1: "\u3011", 2: ""}.get(level, "")
    return paragraph([tr(prefix + text + suffix, bold=True)])


def divider():
    return paragraph([tr("\u2500" * 50)])


def item_block(num, title, badge, abstract, source, date, url):
    blocks = []
    badge_text = badge if badge else ""
    title_text = f"{badge_text} {title}" if badge_text else title
    blocks.append(paragraph([tr(f"  {num}. ", bold=True), tr(title_text, bold=True, link=url)]))
    blocks.append(paragraph([tr(abstract)]))
    meta_parts = []
    if source:
        meta_parts.append(f"来源：{source}")
    if date:
        meta_parts.append(f"日期：{date}")
    if url:
        meta_parts.append(f"链接：{url}")
    blocks.append(paragraph([tr(" | ".join(meta_parts), bold=False)]))
    blocks.append(divider())
    return blocks


def section_block(title, en_title, items):
    blocks = []
    blocks.append(heading(title, 1))
    blocks.append(paragraph([tr(en_title, bold=False)]))
    blocks.append(divider())
    for i, item in enumerate(items, 1):
        blocks.extend(item_block(
            i,
            item.get('title', ''),
            item.get('badge', ''),
            item.get('abstract', ''),
            item.get('source', ''),
            item.get('date', ''),
            item.get('url', '')
        ))
    return blocks


def build_blocks():
    blocks = []
    blocks.append(heading(f"海洋AI技术日报 · {datetime.now().strftime('%Y年%m月%d日')}", 1))
    blocks.append(divider())
    for section in SECTIONS:
        blocks.extend(section_block(
            section['title'],
            section.get('en', ''),
            section.get('items', [])
        ))
    return blocks


def create_document_and_write(tenant_access_token):
    url = "https://open.feishu.cn/open-apis/docx/v1/documents"
    payload = {"title": f"海洋AI技术日报 {datetime.now().strftime('%Y-%m-%d')}"}
    headers = {
        "Authorization": f"Bearer {tenant_access_token}",
        "Content-Type": "application/json"
    }
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    doc_id = resp.json()["data"]["document"]["document_id"]
    print(f"文档创建成功: {doc_id}")
    return doc_id


def write_blocks_to_doc(token, doc_id, blocks, max_retries=3):
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {"children": blocks, "index": 0}
    for attempt in range(max_retries):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=60)
            if resp.status_code == 200:
                print(f"成功写入 {len(blocks)} 个内容块")
                return
            elif resp.status_code == 429:
                print(f"遇到限流，等待 60 秒...")
                time.sleep(60)
            else:
                print(f"写入失败 (状态码: {resp.status_code}): {resp.text}")
                if attempt < max_retries - 1:
                    time.sleep(5)
        except Exception as e:
            print(f"写入异常: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)
    print("文档写入失败")


def get_tenant_access_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = {"app_id": APP_ID, "app_secret": APP_SECRET}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()["tenant_access_token"]


def main():
    print("开始推送飞书文档...")
    token = get_tenant_access_token()
    doc_id = create_document_and_write(token)
    blocks = build_blocks()
    write_blocks_to_doc(token, doc_id, blocks)
    with open("feishu_doc_url.txt", "w") as f:
        f.write(f"https://wcn5jx0ifkx3.feishu.cn/docx/{doc_id}\n")
    print(f"文档地址已保存: feishu_doc_url.txt")


if __name__ == "__main__":
    main()
