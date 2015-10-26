#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db import engine, Base
from tables import Nodes,Edges_0910,Edges_2011,Edges_2012,Edges_2013,Edges_2014,Edges_2015,BlkTime


Base.metadata.create_all(engine) #create all of Class which belonged to Base Class