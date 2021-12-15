{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Emp Names</th>\n",
       "      <th>Location</th>\n",
       "      <th>Floor</th>\n",
       "      <th>DEPARTMENT</th>\n",
       "      <th>CURRENT \n",
       "POSITION TITLES</th>\n",
       "      <th>FUTURE FUNCTION BASED TITLES</th>\n",
       "      <th>PAY GRADE \n",
       "(SENIOR (Gr.0-8)/\n",
       "NON SENIOR(Gr.9-16))</th>\n",
       "      <th>REMOTABILITY INDEX</th>\n",
       "      <th>At Office/Week</th>\n",
       "      <th>Employee preferences(Day of the week)</th>\n",
       "      <th>WFH(0) or At Office(1)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Philip Druckman</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PROCUREMENT &amp; SUPPLY CHAIN</td>\n",
       "      <td>Warehouse Officer</td>\n",
       "      <td>Officer (Warehouse)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Patrick Fixler</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PROCUREMENT &amp; SUPPLY CHAIN</td>\n",
       "      <td>Warehouse Assistant</td>\n",
       "      <td>Administrative Assistant (P&amp;SC)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Sompop Chang</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>FINANCE</td>\n",
       "      <td>Treasury Coordinator</td>\n",
       "      <td>Accountant (Treasury)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Michelle Grusq</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>BUSINESS SUPPORT SERVICE</td>\n",
       "      <td>Transport Coordinator</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Parker</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PIPING</td>\n",
       "      <td>Technician</td>\n",
       "      <td>Technician</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Vincent</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>MACHINE SHOP</td>\n",
       "      <td>Technician</td>\n",
       "      <td>Technician</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Calvin</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>ELECTRICAL &amp; INSTRUMENTATION</td>\n",
       "      <td>Technician</td>\n",
       "      <td>Technician (Electrical)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Timothy</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>SHIPWRIGHT</td>\n",
       "      <td>Technician</td>\n",
       "      <td>Technician</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Jax</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PLANT &amp; MAINTENANCE</td>\n",
       "      <td>Team Leader - Marine Rigging</td>\n",
       "      <td>Rigger (P&amp;M)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Barrett</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PLANT &amp; MAINTENANCE</td>\n",
       "      <td>Team Leader - Machinist</td>\n",
       "      <td>Group Lader (P&amp;M)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Maximus</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PLANT &amp; MAINTENANCE</td>\n",
       "      <td>Team Leader – HVAC &amp; Plumping</td>\n",
       "      <td>Group Leader (P&amp;M)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Tara Cantrock</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>IT &amp; SYSTEMS</td>\n",
       "      <td>Systems Engineer</td>\n",
       "      <td>Engineer (IT Systems)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Aaron</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>STEEL WORKS</td>\n",
       "      <td>Supervisor</td>\n",
       "      <td>Supervisor (Steel) OB,WS,QC, WP</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Jace</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PIPING</td>\n",
       "      <td>Supervisor</td>\n",
       "      <td>Supervisor (Piping) OB,WS,QC,WP</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Luca</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>MACHINE SHOP</td>\n",
       "      <td>Supervisor</td>\n",
       "      <td>Supervisor (Machine Shop)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Brandon</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>MACHINERY</td>\n",
       "      <td>Supervisor</td>\n",
       "      <td>Supervisor (Machinery)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Justin</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>ELECTRICAL &amp; INSTRUMENTATION</td>\n",
       "      <td>Supervisor</td>\n",
       "      <td>Supervisor (Electrical)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Abraham</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>SHIPWRIGHT</td>\n",
       "      <td>Supervisor</td>\n",
       "      <td>Supervisor (Shipwright)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Brantley</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PLANT &amp; MAINTENANCE</td>\n",
       "      <td>Supervisor</td>\n",
       "      <td>Supervisor (Services)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Greyson</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>STEEL WORKS</td>\n",
       "      <td>Structural Welder</td>\n",
       "      <td>Welder (Structure)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Austin</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>STEEL WORKS</td>\n",
       "      <td>Structural Rigger</td>\n",
       "      <td>Rigger (Structural)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Ian</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>STEEL WORKS</td>\n",
       "      <td>Structural Fitter</td>\n",
       "      <td>Fitter (Structure)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>Patino Forsyth</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PROCUREMENT &amp; SUPPLY CHAIN</td>\n",
       "      <td>Store Keeper</td>\n",
       "      <td>Store Keeper</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Jonathan</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>STEEL WORKS</td>\n",
       "      <td>Store Keeper</td>\n",
       "      <td>Store Keeper</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Alex</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>ELECTRICAL &amp; INSTRUMENTATION</td>\n",
       "      <td>Store Keeper</td>\n",
       "      <td>Store Keeper</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>Finn</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>SHIPWRIGHT</td>\n",
       "      <td>Store Keeper</td>\n",
       "      <td>Store Keeper</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>Alejandro</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PLANT &amp; MAINTENANCE</td>\n",
       "      <td>Steel Worker</td>\n",
       "      <td>Fitter (P&amp;M)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>Ryan Cloke</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>COMMERCIAL, MARINE &amp; O&amp;IE</td>\n",
       "      <td>Sr.Proposal&amp;Contracts Engineer (O&amp;IE)</td>\n",
       "      <td>Engineer (Estimating/ Invoicing)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Joshua</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>ENGINEERING</td>\n",
       "      <td>Sr.Design Engineer-Mechanical &amp; Piping</td>\n",
       "      <td>Design Engineer (Mechanical &amp; Piping)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>Ophir Friedman</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>BUSINESS SUPPORT SERVICE</td>\n",
       "      <td>Sr.Bus.Support Services Officer-Workfr.</td>\n",
       "      <td>Officer (Workforce)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>Nicole Gao</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>BUSINESS SUPPORT SERVICE</td>\n",
       "      <td>Sr.Bus.Support Services Officer-Enterp.</td>\n",
       "      <td>Officer (Enterprise)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>Rui Cockle</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>COMMERCIAL, MARINE &amp; O&amp;IE</td>\n",
       "      <td>Sr. Estimating Engineer(O&amp;IE Fabr.)</td>\n",
       "      <td>Engineer (Estimating/ Invoicing)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>Caleb</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>ENGINEERING</td>\n",
       "      <td>Sr. Design Engineer-Structure Offshore</td>\n",
       "      <td>Design Engineer (Naval Arch/Structure)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>Noelle Fu</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>BUSINESS SUPPORT SERVICE</td>\n",
       "      <td>Sr. Bus.Support Services Officer-Client</td>\n",
       "      <td>Officer (Business Support Service)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>Ryan</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>ENGINEERING</td>\n",
       "      <td>Sr.  Design Engineer-Structure Marine</td>\n",
       "      <td>Design Engineer (Naval Arch/Structure)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>Tanzeer Cao</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>IT &amp; SYSTEMS</td>\n",
       "      <td>Site Engineer</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>Ted Brown</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>IT &amp; SYSTEMS</td>\n",
       "      <td>Shipyard IT Projects Lead</td>\n",
       "      <td>Shipyard IT Projects Lead</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37</th>\n",
       "      <td>Massimo Himmelfarb</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>HSSE</td>\n",
       "      <td>Shipyard HSSE Manager</td>\n",
       "      <td>Dept. Manager (QHSSE)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>Tadamitsu Carrow</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>FINANCE</td>\n",
       "      <td>Shipyard Finance Manager</td>\n",
       "      <td>Dept. Manager (Finance)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>Grant</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PLANT &amp; MAINTENANCE</td>\n",
       "      <td>Shipyard Facility &amp; Maintenance Manager</td>\n",
       "      <td>Dept Manager (P&amp;M)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>Jasper</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>SHIPWRIGHT</td>\n",
       "      <td>Shipwright Manager</td>\n",
       "      <td>Dept. Manager (Shipwright)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41</th>\n",
       "      <td>Tae Carrillo</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>IT &amp; SYSTEMS</td>\n",
       "      <td>Service Desk Support</td>\n",
       "      <td>Service Desk Support</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>42</th>\n",
       "      <td>Jacob</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PRODUCTION CONTROL</td>\n",
       "      <td>Senior Yard Manager</td>\n",
       "      <td>Senior Yard Manager</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43</th>\n",
       "      <td>Rikin Davis</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PROCUREMENT &amp; SUPPLY CHAIN</td>\n",
       "      <td>Senior Warehouse Officer</td>\n",
       "      <td>Section Head (Warehouse Inventory &amp; Materials)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44</th>\n",
       "      <td>Thanadtha Brown</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>IT &amp; SYSTEMS</td>\n",
       "      <td>Senior System Analyst (FICO)</td>\n",
       "      <td>System Analyst (FICO)</td>\n",
       "      <td>Senior Staff (SS)</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>Jaxson</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>STEEL WORKS</td>\n",
       "      <td>Senior Structural Welder</td>\n",
       "      <td>Welder (Structure)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>46</th>\n",
       "      <td>Adam</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>STEEL WORKS</td>\n",
       "      <td>Senior Structural Fitter</td>\n",
       "      <td>Fitter (Structure)</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>47</th>\n",
       "      <td>Patrick Flegal</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PROCUREMENT &amp; SUPPLY CHAIN</td>\n",
       "      <td>Senior Store Keeper</td>\n",
       "      <td>Store Keeper</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>Adrian</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>STEEL WORKS</td>\n",
       "      <td>Senior Store Keeper</td>\n",
       "      <td>Store Keeper</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49</th>\n",
       "      <td>Everett</td>\n",
       "      <td>Building WTC</td>\n",
       "      <td>Floor 12</td>\n",
       "      <td>PIPING</td>\n",
       "      <td>Senior Store Keeper</td>\n",
       "      <td>Store Keeper</td>\n",
       "      <td>Non Senior Staff (NSS)</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Emp Names      Location     Floor                    DEPARTMENT  \\\n",
       "0      Philip Druckman  Building WTC  Floor 12    PROCUREMENT & SUPPLY CHAIN   \n",
       "1       Patrick Fixler  Building WTC  Floor 12    PROCUREMENT & SUPPLY CHAIN   \n",
       "2         Sompop Chang  Building WTC  Floor 12                       FINANCE   \n",
       "3       Michelle Grusq  Building WTC  Floor 12      BUSINESS SUPPORT SERVICE   \n",
       "4              Parker   Building WTC  Floor 12                        PIPING   \n",
       "5             Vincent   Building WTC  Floor 12                  MACHINE SHOP   \n",
       "6              Calvin   Building WTC  Floor 12  ELECTRICAL & INSTRUMENTATION   \n",
       "7             Timothy   Building WTC  Floor 12                    SHIPWRIGHT   \n",
       "8                 Jax   Building WTC  Floor 12           PLANT & MAINTENANCE   \n",
       "9             Barrett   Building WTC  Floor 12           PLANT & MAINTENANCE   \n",
       "10            Maximus   Building WTC  Floor 12           PLANT & MAINTENANCE   \n",
       "11       Tara Cantrock  Building WTC  Floor 12                  IT & SYSTEMS   \n",
       "12              Aaron   Building WTC  Floor 12                   STEEL WORKS   \n",
       "13               Jace   Building WTC  Floor 12                        PIPING   \n",
       "14               Luca   Building WTC  Floor 12                  MACHINE SHOP   \n",
       "15            Brandon   Building WTC  Floor 12                     MACHINERY   \n",
       "16             Justin   Building WTC  Floor 12  ELECTRICAL & INSTRUMENTATION   \n",
       "17            Abraham   Building WTC  Floor 12                    SHIPWRIGHT   \n",
       "18           Brantley   Building WTC  Floor 12           PLANT & MAINTENANCE   \n",
       "19            Greyson   Building WTC  Floor 12                   STEEL WORKS   \n",
       "20             Austin   Building WTC  Floor 12                   STEEL WORKS   \n",
       "21                Ian   Building WTC  Floor 12                   STEEL WORKS   \n",
       "22      Patino Forsyth  Building WTC  Floor 12    PROCUREMENT & SUPPLY CHAIN   \n",
       "23           Jonathan   Building WTC  Floor 12                   STEEL WORKS   \n",
       "24               Alex   Building WTC  Floor 12  ELECTRICAL & INSTRUMENTATION   \n",
       "25               Finn   Building WTC  Floor 12                    SHIPWRIGHT   \n",
       "26          Alejandro   Building WTC  Floor 12           PLANT & MAINTENANCE   \n",
       "27          Ryan Cloke  Building WTC  Floor 12     COMMERCIAL, MARINE & O&IE   \n",
       "28             Joshua   Building WTC  Floor 12                   ENGINEERING   \n",
       "29      Ophir Friedman  Building WTC  Floor 12      BUSINESS SUPPORT SERVICE   \n",
       "30          Nicole Gao  Building WTC  Floor 12      BUSINESS SUPPORT SERVICE   \n",
       "31          Rui Cockle  Building WTC  Floor 12     COMMERCIAL, MARINE & O&IE   \n",
       "32              Caleb   Building WTC  Floor 12                   ENGINEERING   \n",
       "33           Noelle Fu  Building WTC  Floor 12      BUSINESS SUPPORT SERVICE   \n",
       "34               Ryan   Building WTC  Floor 12                   ENGINEERING   \n",
       "35         Tanzeer Cao  Building WTC  Floor 12                  IT & SYSTEMS   \n",
       "36           Ted Brown  Building WTC  Floor 12                  IT & SYSTEMS   \n",
       "37  Massimo Himmelfarb  Building WTC  Floor 12                          HSSE   \n",
       "38    Tadamitsu Carrow  Building WTC  Floor 12                       FINANCE   \n",
       "39              Grant   Building WTC  Floor 12           PLANT & MAINTENANCE   \n",
       "40             Jasper   Building WTC  Floor 12                    SHIPWRIGHT   \n",
       "41        Tae Carrillo  Building WTC  Floor 12                  IT & SYSTEMS   \n",
       "42              Jacob   Building WTC  Floor 12            PRODUCTION CONTROL   \n",
       "43         Rikin Davis  Building WTC  Floor 12    PROCUREMENT & SUPPLY CHAIN   \n",
       "44     Thanadtha Brown  Building WTC  Floor 12                  IT & SYSTEMS   \n",
       "45             Jaxson   Building WTC  Floor 12                   STEEL WORKS   \n",
       "46               Adam   Building WTC  Floor 12                   STEEL WORKS   \n",
       "47      Patrick Flegal  Building WTC  Floor 12    PROCUREMENT & SUPPLY CHAIN   \n",
       "48             Adrian   Building WTC  Floor 12                   STEEL WORKS   \n",
       "49            Everett   Building WTC  Floor 12                        PIPING   \n",
       "\n",
       "                  CURRENT \\nPOSITION TITLES  \\\n",
       "0                         Warehouse Officer   \n",
       "1                       Warehouse Assistant   \n",
       "2                      Treasury Coordinator   \n",
       "3                     Transport Coordinator   \n",
       "4                                Technician   \n",
       "5                                Technician   \n",
       "6                                Technician   \n",
       "7                                Technician   \n",
       "8              Team Leader - Marine Rigging   \n",
       "9                   Team Leader - Machinist   \n",
       "10            Team Leader – HVAC & Plumping   \n",
       "11                         Systems Engineer   \n",
       "12                               Supervisor   \n",
       "13                               Supervisor   \n",
       "14                               Supervisor   \n",
       "15                               Supervisor   \n",
       "16                               Supervisor   \n",
       "17                               Supervisor   \n",
       "18                               Supervisor   \n",
       "19                        Structural Welder   \n",
       "20                        Structural Rigger   \n",
       "21                        Structural Fitter   \n",
       "22                             Store Keeper   \n",
       "23                             Store Keeper   \n",
       "24                             Store Keeper   \n",
       "25                             Store Keeper   \n",
       "26                             Steel Worker   \n",
       "27    Sr.Proposal&Contracts Engineer (O&IE)   \n",
       "28   Sr.Design Engineer-Mechanical & Piping   \n",
       "29  Sr.Bus.Support Services Officer-Workfr.   \n",
       "30  Sr.Bus.Support Services Officer-Enterp.   \n",
       "31      Sr. Estimating Engineer(O&IE Fabr.)   \n",
       "32   Sr. Design Engineer-Structure Offshore   \n",
       "33  Sr. Bus.Support Services Officer-Client   \n",
       "34    Sr.  Design Engineer-Structure Marine   \n",
       "35                            Site Engineer   \n",
       "36                Shipyard IT Projects Lead   \n",
       "37                    Shipyard HSSE Manager   \n",
       "38                 Shipyard Finance Manager   \n",
       "39  Shipyard Facility & Maintenance Manager   \n",
       "40                       Shipwright Manager   \n",
       "41                     Service Desk Support   \n",
       "42                      Senior Yard Manager   \n",
       "43                 Senior Warehouse Officer   \n",
       "44             Senior System Analyst (FICO)   \n",
       "45                 Senior Structural Welder   \n",
       "46                 Senior Structural Fitter   \n",
       "47                      Senior Store Keeper   \n",
       "48                      Senior Store Keeper   \n",
       "49                      Senior Store Keeper   \n",
       "\n",
       "                      FUTURE FUNCTION BASED TITLES  \\\n",
       "0                              Officer (Warehouse)   \n",
       "1                  Administrative Assistant (P&SC)   \n",
       "2                            Accountant (Treasury)   \n",
       "3                                              NaN   \n",
       "4                                       Technician   \n",
       "5                                       Technician   \n",
       "6                          Technician (Electrical)   \n",
       "7                                       Technician   \n",
       "8                                     Rigger (P&M)   \n",
       "9                                Group Lader (P&M)   \n",
       "10                              Group Leader (P&M)   \n",
       "11                           Engineer (IT Systems)   \n",
       "12                 Supervisor (Steel) OB,WS,QC, WP   \n",
       "13                 Supervisor (Piping) OB,WS,QC,WP   \n",
       "14                       Supervisor (Machine Shop)   \n",
       "15                          Supervisor (Machinery)   \n",
       "16                         Supervisor (Electrical)   \n",
       "17                         Supervisor (Shipwright)   \n",
       "18                           Supervisor (Services)   \n",
       "19                              Welder (Structure)   \n",
       "20                             Rigger (Structural)   \n",
       "21                              Fitter (Structure)   \n",
       "22                                    Store Keeper   \n",
       "23                                    Store Keeper   \n",
       "24                                    Store Keeper   \n",
       "25                                    Store Keeper   \n",
       "26                                    Fitter (P&M)   \n",
       "27                Engineer (Estimating/ Invoicing)   \n",
       "28           Design Engineer (Mechanical & Piping)   \n",
       "29                             Officer (Workforce)   \n",
       "30                            Officer (Enterprise)   \n",
       "31                Engineer (Estimating/ Invoicing)   \n",
       "32          Design Engineer (Naval Arch/Structure)   \n",
       "33              Officer (Business Support Service)   \n",
       "34          Design Engineer (Naval Arch/Structure)   \n",
       "35                                             NaN   \n",
       "36                       Shipyard IT Projects Lead   \n",
       "37                           Dept. Manager (QHSSE)   \n",
       "38                         Dept. Manager (Finance)   \n",
       "39                              Dept Manager (P&M)   \n",
       "40                      Dept. Manager (Shipwright)   \n",
       "41                            Service Desk Support   \n",
       "42                             Senior Yard Manager   \n",
       "43  Section Head (Warehouse Inventory & Materials)   \n",
       "44                           System Analyst (FICO)   \n",
       "45                              Welder (Structure)   \n",
       "46                              Fitter (Structure)   \n",
       "47                                    Store Keeper   \n",
       "48                                    Store Keeper   \n",
       "49                                    Store Keeper   \n",
       "\n",
       "   PAY GRADE \\n(SENIOR (Gr.0-8)/\\nNON SENIOR(Gr.9-16))  REMOTABILITY INDEX  \\\n",
       "0                              Non Senior Staff (NSS)                    1   \n",
       "1                              Non Senior Staff (NSS)                    5   \n",
       "2                                   Senior Staff (SS)                    5   \n",
       "3                              Non Senior Staff (NSS)                    3   \n",
       "4                              Non Senior Staff (NSS)                    5   \n",
       "5                              Non Senior Staff (NSS)                    0   \n",
       "6                              Non Senior Staff (NSS)                    5   \n",
       "7                              Non Senior Staff (NSS)                    3   \n",
       "8                              Non Senior Staff (NSS)                    4   \n",
       "9                              Non Senior Staff (NSS)                    4   \n",
       "10                             Non Senior Staff (NSS)                    2   \n",
       "11                                  Senior Staff (SS)                    5   \n",
       "12                             Non Senior Staff (NSS)                    0   \n",
       "13                             Non Senior Staff (NSS)                    2   \n",
       "14                             Non Senior Staff (NSS)                    4   \n",
       "15                             Non Senior Staff (NSS)                    2   \n",
       "16                             Non Senior Staff (NSS)                    3   \n",
       "17                             Non Senior Staff (NSS)                    2   \n",
       "18                             Non Senior Staff (NSS)                    3   \n",
       "19                             Non Senior Staff (NSS)                    4   \n",
       "20                             Non Senior Staff (NSS)                    2   \n",
       "21                             Non Senior Staff (NSS)                    5   \n",
       "22                             Non Senior Staff (NSS)                    3   \n",
       "23                             Non Senior Staff (NSS)                    5   \n",
       "24                             Non Senior Staff (NSS)                    2   \n",
       "25                             Non Senior Staff (NSS)                    3   \n",
       "26                             Non Senior Staff (NSS)                    1   \n",
       "27                                  Senior Staff (SS)                    2   \n",
       "28                                  Senior Staff (SS)                    2   \n",
       "29                                  Senior Staff (SS)                    2   \n",
       "30                                  Senior Staff (SS)                    1   \n",
       "31                                  Senior Staff (SS)                    0   \n",
       "32                                  Senior Staff (SS)                    4   \n",
       "33                                  Senior Staff (SS)                    4   \n",
       "34                                  Senior Staff (SS)                    5   \n",
       "35                                  Senior Staff (SS)                    4   \n",
       "36                                  Senior Staff (SS)                    2   \n",
       "37                                  Senior Staff (SS)                    2   \n",
       "38                                  Senior Staff (SS)                    2   \n",
       "39                                  Senior Staff (SS)                    5   \n",
       "40                                  Senior Staff (SS)                    3   \n",
       "41                             Non Senior Staff (NSS)                    1   \n",
       "42                                  Senior Staff (SS)                    1   \n",
       "43                                  Senior Staff (SS)                    5   \n",
       "44                                  Senior Staff (SS)                    5   \n",
       "45                             Non Senior Staff (NSS)                    1   \n",
       "46                             Non Senior Staff (NSS)                    0   \n",
       "47                             Non Senior Staff (NSS)                    1   \n",
       "48                             Non Senior Staff (NSS)                    5   \n",
       "49                             Non Senior Staff (NSS)                    4   \n",
       "\n",
       "    At Office/Week  Employee preferences(Day of the week)  \\\n",
       "0                4                                      3   \n",
       "1                0                                      4   \n",
       "2                0                                      1   \n",
       "3                2                                      3   \n",
       "4                0                                      2   \n",
       "5                5                                      3   \n",
       "6                0                                      5   \n",
       "7                2                                      4   \n",
       "8                1                                      3   \n",
       "9                1                                      5   \n",
       "10               3                                      3   \n",
       "11               0                                      5   \n",
       "12               5                                      4   \n",
       "13               3                                      3   \n",
       "14               1                                      1   \n",
       "15               3                                      3   \n",
       "16               2                                      3   \n",
       "17               3                                      1   \n",
       "18               2                                      1   \n",
       "19               1                                      1   \n",
       "20               3                                      4   \n",
       "21               0                                      1   \n",
       "22               2                                      5   \n",
       "23               0                                      2   \n",
       "24               3                                      2   \n",
       "25               2                                      5   \n",
       "26               4                                      5   \n",
       "27               3                                      1   \n",
       "28               3                                      3   \n",
       "29               3                                      3   \n",
       "30               4                                      5   \n",
       "31               5                                      4   \n",
       "32               1                                      5   \n",
       "33               1                                      4   \n",
       "34               0                                      4   \n",
       "35               1                                      5   \n",
       "36               3                                      4   \n",
       "37               3                                      3   \n",
       "38               3                                      4   \n",
       "39               0                                      2   \n",
       "40               2                                      3   \n",
       "41               4                                      2   \n",
       "42               4                                      5   \n",
       "43               0                                      2   \n",
       "44               0                                      1   \n",
       "45               4                                      4   \n",
       "46               5                                      2   \n",
       "47               4                                      4   \n",
       "48               0                                      3   \n",
       "49               1                                      1   \n",
       "\n",
       "    WFH(0) or At Office(1)  \n",
       "0                        1  \n",
       "1                        0  \n",
       "2                        0  \n",
       "3                        1  \n",
       "4                        0  \n",
       "5                        1  \n",
       "6                        0  \n",
       "7                        0  \n",
       "8                        1  \n",
       "9                        0  \n",
       "10                       0  \n",
       "11                       1  \n",
       "12                       1  \n",
       "13                       0  \n",
       "14                       0  \n",
       "15                       0  \n",
       "16                       0  \n",
       "17                       0  \n",
       "18                       1  \n",
       "19                       1  \n",
       "20                       0  \n",
       "21                       1  \n",
       "22                       0  \n",
       "23                       0  \n",
       "24                       1  \n",
       "25                       1  \n",
       "26                       0  \n",
       "27                       0  \n",
       "28                       0  \n",
       "29                       0  \n",
       "30                       0  \n",
       "31                       1  \n",
       "32                       0  \n",
       "33                       1  \n",
       "34                       1  \n",
       "35                       1  \n",
       "36                       0  \n",
       "37                       1  \n",
       "38                       1  \n",
       "39                       0  \n",
       "40                       0  \n",
       "41                       1  \n",
       "42                       1  \n",
       "43                       0  \n",
       "44                       1  \n",
       "45                       1  \n",
       "46                       1  \n",
       "47                       0  \n",
       "48                       0  \n",
       "49                       1  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xl=pd.read_excel('C:/Users/PC/Downloads/DataSet1.xlsx')\n",
    "df=pd.DataFrame(xl)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "employees=list(df['Emp Names'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_steel=list(df['Emp Names'][df['DEPARTMENT']=='STEEL WORKS'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_plant=list(df['Emp Names'][df['DEPARTMENT']=='PLANT & MAINTENANCE'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def xa0_remover(namelist):\n",
    "    \n",
    "    return [x.replace('\\xa0','') for x in namelist]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Jax', 'Barrett', 'Maximus', 'Brantley', 'Alejandro', 'Grant']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp_plant=xa0_remover(emp_plant)\n",
    "emp_plant"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_steel=xa0_remover(emp_steel)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def name_day_variable_creator(namelist,dayslist=['Mon','Tue','Wed','Thu','Fri']):\n",
    "    nameday_list=[]\n",
    "    for name in namelist:\n",
    "        minilist=[]\n",
    "        for day in dayslist:\n",
    "            minilist.append(name+day)\n",
    "        nameday_list.append(minilist)\n",
    "    return nameday_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['AMon', 'ATue', 'AWed'], ['BMon', 'BTue', 'BWed'], ['CMon', 'CTue', 'CWed']]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name_day_variable_creator(['A','B','C'],['Mon','Tue','Wed'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "workingdays=['Mon','Tue','Wed','Thu','Fri']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "steel_nameday=name_day_variable_creator(emp_steel,workingdays)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "plant_nameday=name_day_variable_creator(emp_plant, workingdays)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "import constraint\n",
    "from constraint import *\n",
    "import time\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**DataFrame Column Additions**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "list_raw=df['Employee preferences(Day of the week)']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "day_dict={1:'Mon',2:'Tue',3:'Wed',4:'Thu',5:'Fri'}\n",
    "list_translated=[]\n",
    "for i in list_raw:\n",
    "    list_translated.append(day_dict[i])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Employee preferences(Day of the week)']=list_translated"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_names=list(df['Emp Names'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "day_preference=list(df['Employee preferences(Day of the week)'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_day_pref=[(x+y) for (x,y) in zip(emp_names,day_preference)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_day_pref=xa0_remover(emp_day_pref)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Emp_day_Preference']=emp_day_pref"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "office_YorN=list(df['WFH(0) or At Office(1)'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_day_pref_dict={key:value for (key, value) in zip(emp_day_pref, office_YorN)} "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "STEEL WORKS                     8\n",
       "PLANT & MAINTENANCE             6\n",
       "IT & SYSTEMS                    5\n",
       "PROCUREMENT & SUPPLY CHAIN      5\n",
       "SHIPWRIGHT                      4\n",
       "BUSINESS SUPPORT SERVICE        4\n",
       "PIPING                          3\n",
       "ELECTRICAL & INSTRUMENTATION    3\n",
       "ENGINEERING                     3\n",
       "COMMERCIAL, MARINE & O&IE       2\n",
       "FINANCE                         2\n",
       "MACHINE SHOP                    2\n",
       "PRODUCTION CONTROL              1\n",
       "MACHINERY                       1\n",
       "HSSE                            1\n",
       "Name: DEPARTMENT, dtype: int64"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.DEPARTMENT.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Variables and Constraints Functions**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "def variable_generator(nameday_LoL, ProblemName, emp_pref='yes'):\n",
    "    c=0\n",
    "    for element in nameday_LoL:\n",
    "        for sub_element in element:\n",
    "            if sub_element in list(df['Emp_day_Preference']):\n",
    "                print ('{0}.addVariable('.format(ProblemName)+'\\''+str(sub_element)+'\\''+',[{0}])'.format(emp_day_pref_dict[sub_element]))\n",
    "            else:\n",
    "                print ('{0}.addVariable('.format(ProblemName)+'\\''+str(sub_element)+'\\''+',[0,1])')\n",
    "            c+=1\n",
    "    print ('Added {0} variables'.format(c))\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "def constraint_generator(namedaylist, ProblemName):\n",
    "    for element in namedaylist:\n",
    "        print ('{0}.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == {1},'.format(ProblemName, name_workday_count_dict[element[0][:-3]]))\n",
    "        print ('(\"{0}\", \"{1}\",\"{2}\",\"{3}\",\"{4}\"))'.format(element[0],element[1],element[2],element[3],element[4]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_time(func): \n",
    "    def inner1(*args, **kwargs): \n",
    "        begin = time.time()           \n",
    "        result=func(*args, **kwargs) \n",
    "        end = time.time() \n",
    "        print(\"Total time taken in : \", func.__name__, end - begin) \n",
    "        return result\n",
    "  \n",
    "    return inner1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "@calculate_time\n",
    "def solution_function(problem):\n",
    "    \n",
    "    return problem.getSolutions()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "def master_list(list_of_days_as_series):\n",
    "    master_list=[]\n",
    "    for i in list_of_days_as_series:\n",
    "        for index, value in i.items():\n",
    "            if value==1:\n",
    "                master_list.append(index)\n",
    "        master_list.append('#')\n",
    "    return master_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "@calculate_time\n",
    "def populator_fn(ml):\n",
    "    EvsE_grid=pd.DataFrame(np.zeros((len(employeelist), len(employeelist))), index=employeelist, columns=employeelist)\n",
    "    for i in range (0,len(ml)):\n",
    "        if ml[i]=='#':\n",
    "            pass\n",
    "        else:\n",
    "            j=i+1\n",
    "            while ml[j]!='#':\n",
    "                EvsE_grid.at[ml[i],ml[j]]=1\n",
    "                EvsE_grid.at[ml[j],ml[i]]=1\n",
    "                j+=1\n",
    "    # EvsE_grid.drop(columns='#',inplace=True)\n",
    "    unique_interactions=(EvsE_grid.values.sum())/2\n",
    "    return EvsE_grid, unique_interactions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "@calculate_time\n",
    "def consolidated_function(solutions):\n",
    "    list_of_employees=[]\n",
    "    for i in solutions[0]:\n",
    "        list_of_employees.append(i[:-3])\n",
    "    employeelist=sorted(list(set(list_of_employees)))\n",
    "    \n",
    "    workingdays=['Mon','Tue','Wed','Thu','Fri']\n",
    "    interaction_score_all=[]\n",
    "    for solution in solutions:\n",
    "        grid1=pd.DataFrame(np.zeros((len(employeelist), len(workingdays))), index=employeelist, columns=workingdays)\n",
    "        for i in solution:\n",
    "            \n",
    "            if (solution[i])==1:\n",
    "                grid1.at[i[:-3],i[-3:]]=1\n",
    "            g = globals()\n",
    "            for i in range(0,5):\n",
    "                g['Day_{0}'.format(i+1)] = pd.Series([x for x in grid1.iloc[:,i]],index=employeelist)\n",
    "            ml=master_list([Day_1,Day_2,Day_3,Day_4,Day_5])\n",
    "            EvsE_grid=pd.DataFrame(np.zeros((len(employeelist), len(employeelist))), index=employeelist, columns=employeelist)\n",
    "            for i in range (0,len(ml)):\n",
    "                if ml[i]=='#':\n",
    "                    pass\n",
    "                else:\n",
    "                    j=i+1\n",
    "                    while ml[j]!='#':\n",
    "                        EvsE_grid.at[ml[i],ml[j]]=1\n",
    "                        EvsE_grid.at[ml[j],ml[i]]=1\n",
    "                        j+=1\n",
    "            # EvsE_grid.drop(columns='#',inplace=True)\n",
    "            unique_interactions=(EvsE_grid.values.sum())/2\n",
    "            interaction_score_all.append(unique_interactions)\n",
    "\n",
    "    return interaction_score_all\n",
    "                \n",
    "                \n",
    "                    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def grid_populator_big(solution,employeelist,workingdays=['Mon','Tue','Wed','Thu','Fri']):\n",
    "    grid1=pd.DataFrame(np.zeros((len(employeelist), len(workingdays))), index=employeelist, columns=workingdays)\n",
    "    \n",
    "    for i in solution:\n",
    "        if (solution[i])==1:\n",
    "            grid1.at[i[:-3],i[-3:]]=1\n",
    "    return grid1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def grid_populator(solution):\n",
    "    grid1=pd.DataFrame(np.zeros((len(['A','B','C','D','E']), len(workingdays))), index=['A','B','C','D','E'], columns=['Mon','Tue','Wed','Thur','Fri'])\n",
    "    for i in solution:\n",
    "        if (solution[i])==1:\n",
    "            grid1.at[i[:-3],i[-3:]]=1\n",
    "    return grid1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "def min_indices(list_of_interaction_scores, c='min'):\n",
    "    if c=='min':\n",
    "        c=min(list_of_interaction_scores)\n",
    "    series1=pd.Series(list_of_interaction_scores)\n",
    "    min_indices_list=[]\n",
    "    for index,value in series1.items():\n",
    "        if value==c:\n",
    "            min_indices_list.append(index)\n",
    "    return min_indices_list\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "def merge_solutions(grid1, grid2):\n",
    "    return pd.concat([grid1, grid2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "def days_series_creator(grid, employeeslist, workingdays):\n",
    "    g = globals()\n",
    "    for i in range(0,len(workingdays)):\n",
    "        g['Day_{0}'.format(i+1)] = pd.Series([x for x in grid.iloc[:,i]],index=employeeslist)\n",
    "    return [Day_1,Day_2,Day_3,Day_4,Day_5]\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "@calculate_time\n",
    "def consolidated_function(solutions):\n",
    "    list_of_employees=[]\n",
    "    for i in solutions[0]:\n",
    "        list_of_employees.append(i[:-3])\n",
    "    employeelist=sorted(list(set(list_of_employees)))\n",
    "    \n",
    "    workingdays=['Mon','Tue','Wed','Thu','Fri']\n",
    "    interaction_score_all=[]\n",
    "    for solution in solutions:\n",
    "        grid1=pd.DataFrame(np.zeros((len(employeelist), len(workingdays))), index=employeelist, columns=workingdays)\n",
    "        for i in solution:\n",
    "            \n",
    "            if (solution[i])==1:\n",
    "                grid1.at[i[:-3],i[-3:]]=1\n",
    "        \n",
    "            g = globals()\n",
    "            for i in range(0,5):\n",
    "                g['Day_{0}'.format(i+1)] = pd.Series([x for x in grid1.iloc[:,i]],index=employeelist)\n",
    "            ml=master_list([Day_1,Day_2,Day_3,Day_4,Day_5])\n",
    "            print (ml)\n",
    "            EvsE_grid=pd.DataFrame(np.zeros((len(employeelist), len(employeelist))), index=employeelist, columns=employeelist)\n",
    "            for i in range (0,len(ml)):\n",
    "                if ml[i]=='#':\n",
    "                    pass\n",
    "                else:\n",
    "                    j=i+1\n",
    "                    while ml[j]!='#':\n",
    "                        EvsE_grid.at[ml[i],ml[j]]=1\n",
    "                        EvsE_grid.at[ml[j],ml[i]]=1\n",
    "                        j+=1\n",
    "            # EvsE_grid.drop(columns='#',inplace=True)\n",
    "            unique_interactions=(EvsE_grid.values.sum())/2\n",
    "            interaction_score_all.append(unique_interactions)\n",
    "\n",
    "    return interaction_score_all\n",
    "                \n",
    "                \n",
    "                    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def populator_fn(ml, employeelist):\n",
    "    EvsE_grid=pd.DataFrame(np.zeros((len(employeelist), len(employeelist))), index=employeelist, columns=employeelist)\n",
    "    for i in range (0,len(ml)):\n",
    "        if ml[i]=='#':\n",
    "            pass\n",
    "        else:\n",
    "            j=i+1\n",
    "            while ml[j]!='#':\n",
    "                EvsE_grid.at[ml[i],ml[j]]=1\n",
    "                EvsE_grid.at[ml[j],ml[i]]=1\n",
    "                j+=1\n",
    "    # EvsE_grid.drop(columns='#',inplace=True)\n",
    "    unique_interactions=(EvsE_grid.values.sum())/2\n",
    "    return EvsE_grid, unique_interactions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "@calculate_time\n",
    "def consolidated_function(solutions):\n",
    "    list_of_employees=[]\n",
    "    for i in solutions[0]:\n",
    "        list_of_employees.append(i[:-3])\n",
    "    employeelist=sorted(list(set(list_of_employees)))\n",
    "    \n",
    "    \n",
    "    workingdays=['Mon','Tue','Wed','Thu','Fri']\n",
    "    interaction_score_all=[]\n",
    "    for solution in solutions:\n",
    "        grid1=pd.DataFrame(np.zeros((len(employeelist), len(workingdays))), index=employeelist, columns=workingdays)\n",
    "        for i in solution:\n",
    "            if (solution[i])==1:\n",
    "                grid1.at[i[:-3],i[-3:]]=1\n",
    "            print (grid1)\n",
    "#             g = globals()\n",
    "#             for i in range(0,5):\n",
    "#                 g['Day_{0}'.format(i+1)] = pd.Series([x for x in grid1.iloc[:,i]],index=employeelist)\n",
    "#             ml=master_list([Day_1,Day_2,Day_3,Day_4,Day_5])\n",
    "#             EvsE_grid=pd.DataFrame(np.zeros((len(employeelist), len(employeelist))), index=employeelist, columns=employeelist)\n",
    "#             print (ml)\n",
    "            \n",
    "# #             for i in range (0,len(ml)):\n",
    "# #                 if ml[i]=='#':\n",
    "# #                     pass\n",
    "# #                 else:\n",
    "# #                     j=i+1\n",
    "# #                     while ml[j]!='#':\n",
    "# #                         EvsE_grid.at[ml[i],ml[j]]=1\n",
    "# #                         EvsE_grid.at[ml[j],ml[i]]=1\n",
    "# #                         j+=1\n",
    "# #             # EvsE_grid.drop(columns='#',inplace=True)\n",
    "# #             print (EvsE_grid)\n",
    "# # #             unique_interactions=(EvsE_grid.values.sum())/2\n",
    "# # #             interaction_score_all.append(unique_interactions)\n",
    "\n",
    "# # #     return interaction_score_all\n",
    "                \n",
    "                "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "def Days_list_as_series(grid, employeelist):\n",
    "    g = globals()\n",
    "    for i in range(0,5):\n",
    "        g['Day_{0}'.format(i+1)] = pd.Series([x for x in grid.iloc[:,i]],index=employeelist)\n",
    "    return [Day_1, Day_2, Day_3, Day_4, Day_5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "def master_list(list_of_days_as_series):\n",
    "    master_list=[]\n",
    "    for i in list_of_days_as_series:\n",
    "        for index, value in i.items():\n",
    "            if value==1:\n",
    "                master_list.append(index)\n",
    "        master_list.append('#')\n",
    "    return master_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "@calculate_time\n",
    "def consolidated_function_mod(solutions):\n",
    "    list_of_employees=[]\n",
    "    for i in solutions[0]:\n",
    "        list_of_employees.append(i[:-3])\n",
    "    employeeslist=sorted(list(set(list_of_employees)))\n",
    "    workingdays=['Mon','Tue','Wed','Thu','Fri']\n",
    "    interaction_score_all=[]\n",
    "    for solution in solutions:\n",
    "        grid1=pd.DataFrame(np.zeros((len(employeeslist), len(workingdays))), index=employeeslist, columns=workingdays)\n",
    "        for i in solution:\n",
    "            if (solution[i])==1:\n",
    "                grid1.at[i[:-3],i[-3:]]=1\n",
    "                days_as_series=days_series_creator(grid1, employeeslist, workingdays)\n",
    "                ml=master_list(days_as_series)\n",
    "                EvsE_grid, grid_int_score = populator_fn(ml, employeeslist)\n",
    "        interaction_score_all.append(grid_int_score)\n",
    "    return interaction_score_all\n",
    "                "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "def list_index_returner(input_list, value):\n",
    "    index=[]\n",
    "    for i in range(0,len(input_list)):\n",
    "        if input_list[i]==value:\n",
    "            index.append(i)\n",
    "    return index      \n",
    "        \n",
    "            "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**DEPARTMENTWISE EMPLOYEE VARIABLE CREATION**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "Shipwright_emp=list(df['Emp Names'][df['DEPARTMENT']=='SHIPWRIGHT'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "Engineering_emp=list(df['Emp Names'][df['DEPARTMENT']=='ENGINEERING'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "Piping_emp=list(df['Emp Names'][df['DEPARTMENT']=='PIPING'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "E_and_I_emp=list(df['Emp Names'][df['DEPARTMENT']=='ELECTRICAL & INSTRUMENTATION'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "Machine_shop_emp=list(df['Emp Names'][df['DEPARTMENT']=='MACHINE SHOP'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "C_m_and_o_emp=list(df['Emp Names'][df['DEPARTMENT']=='COMMERCIAL, MARINE & O&IE'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "Finance_emp=list(df['Emp Names'][df['DEPARTMENT']=='FINANCE'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "Hsse_emp=list(df['Emp Names'][df['DEPARTMENT']=='HSSE'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "Machinery_emp=list(df['Emp Names'][df['DEPARTMENT']=='MACHINERY'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "production_control_emp=list(df['Emp Names'][df['DEPARTMENT']=='PRODUCTION CONTROL'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "proc_and_sc=list(df['Emp Names'][df['DEPARTMENT']=='PROCUREMENT & SUPPLY CHAIN'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "steel_works_emp=list(df['Emp Names'][df['DEPARTMENT']=='STEEL WORKS'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "plnt_and_mntnc_emp=list(df['Emp Names'][df['DEPARTMENT']=='PLANT & MAINTENANCE'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**COMBINING DEPARTMENTS WITH LOW STRENGTHS**\n",
    "\n",
    "FHMP=Finance+HSSE+Machinery+ProductionControl\n",
    "EIM=ELECTRICAL & INSTRUMENTATION + MACHINE SHOP\n",
    "SCMO=SHIPWRIGHT+COMMERCIAL, MARINE & O&IE\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "STEEL WORKS                     8\n",
       "PLANT & MAINTENANCE             6\n",
       "IT & SYSTEMS                    5\n",
       "PROCUREMENT & SUPPLY CHAIN      5\n",
       "SHIPWRIGHT                      4\n",
       "BUSINESS SUPPORT SERVICE        4\n",
       "PIPING                          3\n",
       "ELECTRICAL & INSTRUMENTATION    3\n",
       "ENGINEERING                     3\n",
       "COMMERCIAL, MARINE & O&IE       2\n",
       "FINANCE                         2\n",
       "MACHINE SHOP                    2\n",
       "PRODUCTION CONTROL              1\n",
       "MACHINERY                       1\n",
       "HSSE                            1\n",
       "Name: DEPARTMENT, dtype: int64"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.DEPARTMENT.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "department_mapping={'STEEL WORKS':'Inventory & Production','PLANT & MAINTENANCE':'Supply chain(SCM)','IT & SYSTEMS': 'Information Technology',\n",
    "                   'PROCUREMENT & SUPPLY CHAIN':'Procurement','BUSINESS SUPPORT SERVICE':'Operations','SHIPWRIGHT':'Sales','ENGINEERING': 'Information Technology',\n",
    "                   'PIPING':'Human Resources','ELECTRICAL & INSTRUMENTATION':'Finance', 'MACHINE SHOP':'Sales', 'COMMERCIAL, MARINE & O&IE':'Operations',\n",
    "                   'FINANCE':'Marketing','HSSE':'General Management','MACHINERY':'Supply chain(SCM)','PRODUCTION CONTROL':'Inventory & Production'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'STEEL WORKS': 'Inventory & Production',\n",
       " 'PLANT & MAINTENANCE': 'Supply chain(SCM)',\n",
       " 'IT & SYSTEMS': 'Information Technology',\n",
       " 'PROCUREMENT & SUPPLY CHAIN': 'Procurement',\n",
       " 'BUSINESS SUPPORT SERVICE': 'Operations',\n",
       " 'SHIPWRIGHT': 'Sales',\n",
       " 'ENGINEERING': 'Information Technology',\n",
       " 'PIPING': 'Human Resources',\n",
       " 'ELECTRICAL & INSTRUMENTATION': 'Finance',\n",
       " 'MACHINE SHOP': 'Sales',\n",
       " 'COMMERCIAL, MARINE & O&IE': 'Operations',\n",
       " 'FINANCE': 'Marketing',\n",
       " 'HSSE': 'General Management',\n",
       " 'MACHINERY': 'Supply chain(SCM)',\n",
       " 'PRODUCTION CONTROL': 'Inventory & Production'}"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "department_mapping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "mapped_departments=[]\n",
    "for index, item in df['DEPARTMENT'].iteritems():\n",
    "    mapped_departments.append(department_mapping[item])\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['DEPARTMENT']=mapped_departments"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0                Procurement\n",
       "1                Procurement\n",
       "2                  Marketing\n",
       "3                 Operations\n",
       "4            Human Resources\n",
       "5                      Sales\n",
       "6                    Finance\n",
       "7                      Sales\n",
       "8          Supply chain(SCM)\n",
       "9          Supply chain(SCM)\n",
       "10         Supply chain(SCM)\n",
       "11    Information Technology\n",
       "12    Inventory & Production\n",
       "13           Human Resources\n",
       "14                     Sales\n",
       "15         Supply chain(SCM)\n",
       "16                   Finance\n",
       "17                     Sales\n",
       "18         Supply chain(SCM)\n",
       "19    Inventory & Production\n",
       "20    Inventory & Production\n",
       "21    Inventory & Production\n",
       "22               Procurement\n",
       "23    Inventory & Production\n",
       "24                   Finance\n",
       "25                     Sales\n",
       "26         Supply chain(SCM)\n",
       "27                Operations\n",
       "28    Information Technology\n",
       "29                Operations\n",
       "30                Operations\n",
       "31                Operations\n",
       "32    Information Technology\n",
       "33                Operations\n",
       "34    Information Technology\n",
       "35    Information Technology\n",
       "36    Information Technology\n",
       "37        General Management\n",
       "38                 Marketing\n",
       "39         Supply chain(SCM)\n",
       "40                     Sales\n",
       "41    Information Technology\n",
       "42    Inventory & Production\n",
       "43               Procurement\n",
       "44    Information Technology\n",
       "45    Inventory & Production\n",
       "46    Inventory & Production\n",
       "47               Procurement\n",
       "48    Inventory & Production\n",
       "49           Human Resources\n",
       "Name: DEPARTMENT, dtype: object"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['DEPARTMENT']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Inventory & Production    9\n",
       "Information Technology    8\n",
       "Supply chain(SCM)         7\n",
       "Operations                6\n",
       "Sales                     6\n",
       "Procurement               5\n",
       "Human Resources           3\n",
       "Finance                   3\n",
       "Marketing                 2\n",
       "General Management        1\n",
       "Name: DEPARTMENT, dtype: int64"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.DEPARTMENT.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\PC\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n",
      "C:\\Users\\PC\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:2: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  \n",
      "C:\\Users\\PC\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:3: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  This is separate from the ipykernel package so we can avoid doing imports until\n"
     ]
    }
   ],
   "source": [
    "df['DEPARTMENT'][df[\"DEPARTMENT\"]=='Finance']='Finance+Marketing+General Management'\n",
    "df['DEPARTMENT'][df[\"DEPARTMENT\"]=='Marketing']='Finance+Marketing+General Management'\n",
    "df['DEPARTMENT'][df[\"DEPARTMENT\"]=='General Management']='Finance+Marketing+General Management'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Inventory & Production                  9\n",
       "Information Technology                  8\n",
       "Supply chain(SCM)                       7\n",
       "Operations                              6\n",
       "Sales                                   6\n",
       "Finance+Marketing+General Management    6\n",
       "Procurement                             5\n",
       "Human Resources                         3\n",
       "Name: DEPARTMENT, dtype: int64"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.DEPARTMENT.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_Inventory=constraint.Problem(BacktrackingSolver())\n",
    "problem_IT=constraint.Problem(BacktrackingSolver())\n",
    "problem_SCM=constraint.Problem(BacktrackingSolver())\n",
    "problem_Sales=constraint.Problem(BacktrackingSolver())\n",
    "problem_FMGM=constraint.Problem(BacktrackingSolver())\n",
    "problem_OP=constraint.Problem(BacktrackingSolver())\n",
    "problem_Proc=constraint.Problem(BacktrackingSolver())\n",
    "problem_HR=constraint.Problem(BacktrackingSolver())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Tara Cantrock',\n",
       " 'Joshua',\n",
       " 'Caleb',\n",
       " 'Ryan',\n",
       " 'Tanzeer Cao',\n",
       " 'Ted Brown',\n",
       " 'Tae Carrillo',\n",
       " 'Thanadtha Brown']"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp_IT=xa0_remover(list(df['Emp Names'][df['DEPARTMENT']=='Information Technology']))\n",
    "emp_IT"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Aaron',\n",
       " 'Greyson',\n",
       " 'Austin',\n",
       " 'Ian',\n",
       " 'Jonathan',\n",
       " 'Jacob',\n",
       " 'Jaxson',\n",
       " 'Adam',\n",
       " 'Adrian']"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp_Inv=xa0_remover(list(df['Emp Names'][df['DEPARTMENT']=='Inventory & Production']))\n",
    "emp_Inv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Jax', 'Barrett', 'Maximus', 'Brandon', 'Brantley', 'Alejandro', 'Grant']"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp_SCM=xa0_remover(list(df['Emp Names'][df['DEPARTMENT']=='Supply chain(SCM)']))\n",
    "emp_SCM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Vincent', 'Timothy', 'Luca', 'Abraham', 'Finn', 'Jasper']"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp_Sales=xa0_remover(list(df['Emp Names'][df['DEPARTMENT']=='Sales']))\n",
    "emp_Sales"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Sompop Chang',\n",
       " 'Calvin',\n",
       " 'Justin',\n",
       " 'Alex',\n",
       " 'Massimo Himmelfarb',\n",
       " 'Tadamitsu Carrow']"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp_FMGM=xa0_remover(list(df['Emp Names'][df['DEPARTMENT']=='Finance+Marketing+General Management']))\n",
    "emp_FMGM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Michelle Grusq',\n",
       " 'Ryan Cloke',\n",
       " 'Ophir Friedman',\n",
       " 'Nicole Gao',\n",
       " 'Rui Cockle',\n",
       " 'Noelle Fu']"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp_OP=xa0_remover(list(df['Emp Names'][df['DEPARTMENT']=='Operations']))\n",
    "emp_OP"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Philip Druckman',\n",
       " 'Patrick Fixler',\n",
       " 'Patino Forsyth',\n",
       " 'Rikin Davis',\n",
       " 'Patrick Flegal']"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp_proc=xa0_remover(list(df['Emp Names'][df['DEPARTMENT']=='Procurement']))\n",
    "emp_proc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Parker', 'Jace', 'Everett']"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp_HR=xa0_remover(list(df['Emp Names'][df['DEPARTMENT']=='Human Resources']))\n",
    "emp_HR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "IT_nd=name_day_variable_creator(emp_IT)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "Inv_nd=name_day_variable_creator(emp_Inv)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "SCM_nd=name_day_variable_creator(emp_SCM)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "Sales_nd=name_day_variable_creator(emp_Sales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "FMGM_nd=name_day_variable_creator(emp_FMGM)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "OP_nd=name_day_variable_creator(emp_OP)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "Proc_nd=name_day_variable_creator(emp_proc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "HR_nd=name_day_variable_creator(emp_HR)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "problem_steel_bt=constraint.Problem(BacktrackingSolver())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "departments=['Inv','IT','SCM','Sales','FMGM','OP','Proc','HR']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_Inv=constraint.Problem(BacktrackingSolver())\n",
      "problem_IT=constraint.Problem(BacktrackingSolver())\n",
      "problem_SCM=constraint.Problem(BacktrackingSolver())\n",
      "problem_Sales=constraint.Problem(BacktrackingSolver())\n",
      "problem_FMGM=constraint.Problem(BacktrackingSolver())\n",
      "problem_OP=constraint.Problem(BacktrackingSolver())\n",
      "problem_Proc=constraint.Problem(BacktrackingSolver())\n",
      "problem_HR=constraint.Problem(BacktrackingSolver())\n"
     ]
    }
   ],
   "source": [
    "for i in departments:\n",
    "    print (\"problem_{}=constraint.Problem(BacktrackingSolver())\".format(i))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Problems Creation**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_Inv=constraint.Problem(BacktrackingSolver())\n",
    "problem_IT=constraint.Problem(BacktrackingSolver())\n",
    "problem_SCM=constraint.Problem(BacktrackingSolver())\n",
    "problem_Sales=constraint.Problem(BacktrackingSolver())\n",
    "problem_FMGM=constraint.Problem(BacktrackingSolver())\n",
    "problem_OP=constraint.Problem(BacktrackingSolver())\n",
    "problem_Proc=constraint.Problem(BacktrackingSolver())\n",
    "problem_HR=constraint.Problem(BacktrackingSolver())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Inventory**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_Inv=constraint.Problem(BacktrackingSolver())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_Inv.addVariable('AaronMon',[0,1])\n",
      "problem_Inv.addVariable('AaronTue',[0,1])\n",
      "problem_Inv.addVariable('AaronWed',[0,1])\n",
      "problem_Inv.addVariable('AaronThu',[1])\n",
      "problem_Inv.addVariable('AaronFri',[0,1])\n",
      "problem_Inv.addVariable('GreysonMon',[1])\n",
      "problem_Inv.addVariable('GreysonTue',[0,1])\n",
      "problem_Inv.addVariable('GreysonWed',[0,1])\n",
      "problem_Inv.addVariable('GreysonThu',[0,1])\n",
      "problem_Inv.addVariable('GreysonFri',[0,1])\n",
      "problem_Inv.addVariable('AustinMon',[0,1])\n",
      "problem_Inv.addVariable('AustinTue',[0,1])\n",
      "problem_Inv.addVariable('AustinWed',[0,1])\n",
      "problem_Inv.addVariable('AustinThu',[0])\n",
      "problem_Inv.addVariable('AustinFri',[0,1])\n",
      "problem_Inv.addVariable('IanMon',[1])\n",
      "problem_Inv.addVariable('IanTue',[0,1])\n",
      "problem_Inv.addVariable('IanWed',[0,1])\n",
      "problem_Inv.addVariable('IanThu',[0,1])\n",
      "problem_Inv.addVariable('IanFri',[0,1])\n",
      "problem_Inv.addVariable('JonathanMon',[0,1])\n",
      "problem_Inv.addVariable('JonathanTue',[0])\n",
      "problem_Inv.addVariable('JonathanWed',[0,1])\n",
      "problem_Inv.addVariable('JonathanThu',[0,1])\n",
      "problem_Inv.addVariable('JonathanFri',[0,1])\n",
      "problem_Inv.addVariable('JacobMon',[0,1])\n",
      "problem_Inv.addVariable('JacobTue',[0,1])\n",
      "problem_Inv.addVariable('JacobWed',[0,1])\n",
      "problem_Inv.addVariable('JacobThu',[0,1])\n",
      "problem_Inv.addVariable('JacobFri',[1])\n",
      "problem_Inv.addVariable('JaxsonMon',[0,1])\n",
      "problem_Inv.addVariable('JaxsonTue',[0,1])\n",
      "problem_Inv.addVariable('JaxsonWed',[0,1])\n",
      "problem_Inv.addVariable('JaxsonThu',[1])\n",
      "problem_Inv.addVariable('JaxsonFri',[0,1])\n",
      "problem_Inv.addVariable('AdamMon',[0,1])\n",
      "problem_Inv.addVariable('AdamTue',[1])\n",
      "problem_Inv.addVariable('AdamWed',[0,1])\n",
      "problem_Inv.addVariable('AdamThu',[0,1])\n",
      "problem_Inv.addVariable('AdamFri',[0,1])\n",
      "problem_Inv.addVariable('AdrianMon',[0,1])\n",
      "problem_Inv.addVariable('AdrianTue',[0,1])\n",
      "problem_Inv.addVariable('AdrianWed',[0])\n",
      "problem_Inv.addVariable('AdrianThu',[0,1])\n",
      "problem_Inv.addVariable('AdrianFri',[0,1])\n",
      "Added 45 variables\n"
     ]
    }
   ],
   "source": [
    "variable_generator(Inv_nd,'problem_Inv' )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_names=xa0_remover(emp_names)\n",
    "days_per_week=list(df['At Office/Week'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Philip Druckman': 4,\n",
       " 'Patrick Fixler': 0,\n",
       " 'Sompop Chang': 0,\n",
       " 'Michelle Grusq': 2,\n",
       " 'Parker': 0,\n",
       " 'Vincent': 5,\n",
       " 'Calvin': 0,\n",
       " 'Timothy': 2,\n",
       " 'Jax': 1,\n",
       " 'Barrett': 1,\n",
       " 'Maximus': 3,\n",
       " 'Tara Cantrock': 0,\n",
       " 'Aaron': 5,\n",
       " 'Jace': 3,\n",
       " 'Luca': 1,\n",
       " 'Brandon': 3,\n",
       " 'Justin': 2,\n",
       " 'Abraham': 3,\n",
       " 'Brantley': 2,\n",
       " 'Greyson': 1,\n",
       " 'Austin': 3,\n",
       " 'Ian': 0,\n",
       " 'Patino Forsyth': 2,\n",
       " 'Jonathan': 0,\n",
       " 'Alex': 3,\n",
       " 'Finn': 2,\n",
       " 'Alejandro': 4,\n",
       " 'Ryan Cloke': 3,\n",
       " 'Joshua': 3,\n",
       " 'Ophir Friedman': 3,\n",
       " 'Nicole Gao': 4,\n",
       " 'Rui Cockle': 5,\n",
       " 'Caleb': 1,\n",
       " 'Noelle Fu': 1,\n",
       " 'Ryan': 0,\n",
       " 'Tanzeer Cao': 1,\n",
       " 'Ted Brown': 3,\n",
       " 'Massimo Himmelfarb': 3,\n",
       " 'Tadamitsu Carrow': 3,\n",
       " 'Grant': 0,\n",
       " 'Jasper': 2,\n",
       " 'Tae Carrillo': 4,\n",
       " 'Jacob': 4,\n",
       " 'Rikin Davis': 0,\n",
       " 'Thanadtha Brown': 0,\n",
       " 'Jaxson': 4,\n",
       " 'Adam': 5,\n",
       " 'Patrick Flegal': 4,\n",
       " 'Adrian': 0,\n",
       " 'Everett': 1}"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name_workday_count_dict={x:y for (x,y) in zip (emp_names,days_per_week)}\n",
    "name_workday_count_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_names=xa0_remover(emp_names)\n",
    "days_per_week=list(df['At Office/Week'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 5,\n",
      "(\"AaronMon\", \"AaronTue\",\"AaronWed\",\"AaronThu\",\"AaronFri\"))\n",
      "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
      "(\"GreysonMon\", \"GreysonTue\",\"GreysonWed\",\"GreysonThu\",\"GreysonFri\"))\n",
      "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
      "(\"AustinMon\", \"AustinTue\",\"AustinWed\",\"AustinThu\",\"AustinFri\"))\n",
      "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
      "(\"IanMon\", \"IanTue\",\"IanWed\",\"IanThu\",\"IanFri\"))\n",
      "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
      "(\"JonathanMon\", \"JonathanTue\",\"JonathanWed\",\"JonathanThu\",\"JonathanFri\"))\n",
      "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 4,\n",
      "(\"JacobMon\", \"JacobTue\",\"JacobWed\",\"JacobThu\",\"JacobFri\"))\n",
      "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 4,\n",
      "(\"JaxsonMon\", \"JaxsonTue\",\"JaxsonWed\",\"JaxsonThu\",\"JaxsonFri\"))\n",
      "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 5,\n",
      "(\"AdamMon\", \"AdamTue\",\"AdamWed\",\"AdamThu\",\"AdamFri\"))\n",
      "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
      "(\"AdrianMon\", \"AdrianTue\",\"AdrianWed\",\"AdrianThu\",\"AdrianFri\"))\n"
     ]
    }
   ],
   "source": [
    "constraint_generator(Inv_nd, 'problem_Inv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_Inv.addVariable('AaronMon',[0,1])\n",
    "problem_Inv.addVariable('AaronTue',[0,1])\n",
    "problem_Inv.addVariable('AaronWed',[0,1])\n",
    "problem_Inv.addVariable('AaronThu',[1])\n",
    "problem_Inv.addVariable('AaronFri',[0,1])\n",
    "problem_Inv.addVariable('GreysonMon',[0,1])\n",
    "problem_Inv.addVariable('GreysonTue',[0,1])\n",
    "problem_Inv.addVariable('GreysonWed',[1])\n",
    "problem_Inv.addVariable('GreysonThu',[0,1])\n",
    "problem_Inv.addVariable('GreysonFri',[0,1])\n",
    "problem_Inv.addVariable('AustinMon',[1])\n",
    "problem_Inv.addVariable('AustinTue',[0,1])\n",
    "problem_Inv.addVariable('AustinWed',[0,1])\n",
    "problem_Inv.addVariable('AustinThu',[0,1])\n",
    "problem_Inv.addVariable('AustinFri',[0,1])\n",
    "problem_Inv.addVariable('IanMon',[0,1])\n",
    "problem_Inv.addVariable('IanTue',[0,1])\n",
    "problem_Inv.addVariable('IanWed',[0,1])\n",
    "problem_Inv.addVariable('IanThu',[0,1])\n",
    "problem_Inv.addVariable('IanFri',[0,1])\n",
    "problem_Inv.addVariable('JonathanMon',[0,1])\n",
    "problem_Inv.addVariable('JonathanTue',[0,1])\n",
    "problem_Inv.addVariable('JonathanWed',[0,1])\n",
    "problem_Inv.addVariable('JonathanThu',[0,1])\n",
    "problem_Inv.addVariable('JonathanFri',[0,1])\n",
    "problem_Inv.addVariable('JacobMon',[0,1])\n",
    "problem_Inv.addVariable('JacobTue',[0,1])\n",
    "problem_Inv.addVariable('JacobWed',[0,1])\n",
    "problem_Inv.addVariable('JacobThu',[0,1])\n",
    "problem_Inv.addVariable('JacobFri',[0,1])\n",
    "problem_Inv.addVariable('JaxsonMon',[0,1])\n",
    "problem_Inv.addVariable('JaxsonTue',[0,1])\n",
    "problem_Inv.addVariable('JaxsonWed',[1])\n",
    "problem_Inv.addVariable('JaxsonThu',[0,1])\n",
    "problem_Inv.addVariable('JaxsonFri',[0,1])\n",
    "problem_Inv.addVariable('AdamMon',[0,1])\n",
    "problem_Inv.addVariable('AdamTue',[0,1])\n",
    "problem_Inv.addVariable('AdamWed',[1])\n",
    "problem_Inv.addVariable('AdamThu',[0,1])\n",
    "problem_Inv.addVariable('AdamFri',[0,1])\n",
    "problem_Inv.addVariable('AdrianMon',[0,1])\n",
    "problem_Inv.addVariable('AdrianTue',[0,1])\n",
    "problem_Inv.addVariable('AdrianWed',[0,1])\n",
    "problem_Inv.addVariable('AdrianThu',[0,1])\n",
    "problem_Inv.addVariable('AdrianFri',[0,1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
    "(\"AaronMon\", \"AaronTue\",\"AaronWed\",\"AaronThu\",\"AaronFri\"))\n",
    "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
    "(\"GreysonMon\", \"GreysonTue\",\"GreysonWed\",\"GreysonThu\",\"GreysonFri\"))\n",
    "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
    "(\"AustinMon\", \"AustinTue\",\"AustinWed\",\"AustinThu\",\"AustinFri\"))\n",
    "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"IanMon\", \"IanTue\",\"IanWed\",\"IanThu\",\"IanFri\"))\n",
    "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"JonathanMon\", \"JonathanTue\",\"JonathanWed\",\"JonathanThu\",\"JonathanFri\"))\n",
    "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
    "(\"JacobMon\", \"JacobTue\",\"JacobWed\",\"JacobThu\",\"JacobFri\"))\n",
    "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 4,\n",
    "(\"JaxsonMon\", \"JaxsonTue\",\"JaxsonWed\",\"JaxsonThu\",\"JaxsonFri\"))\n",
    "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 4,\n",
    "(\"AdamMon\", \"AdamTue\",\"AdamWed\",\"AdamThu\",\"AdamFri\"))\n",
    "problem_Inv.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"AdrianMon\", \"AdrianTue\",\"AdrianWed\",\"AdrianThu\",\"AdrianFri\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  solution_function 5.9162819385528564\n"
     ]
    }
   ],
   "source": [
    "sol_Inv=solution_function(problem_Inv)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5760"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(sol_Inv)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  consolidated_function_mod 373.5148651599884\n"
     ]
    }
   ],
   "source": [
    "Inv_int_total=consolidated_function_mod(sol_Inv)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{12.0, 13.0, 14.0, 15.0}"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(Inv_int_total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [],
   "source": [
    "good_index_Inv=min_indices(Inv_int_total, min(Inv_int_total))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [],
   "source": [
    "bad_index_Inv=min_indices(Inv_int_total, max(Inv_int_total))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "864"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(bad_index_Inv)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [],
   "source": [
    "Inv_bad_solns=[sol_Inv[i] for i in bad_index_Inv]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [],
   "source": [
    "Inv_best_solns=[sol_Inv[i] for i in good_index_Inv]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [],
   "source": [
    "bad_grids_Inv=[]\n",
    "for solution in Inv_bad_solns:\n",
    "    bad_grids_Inv.append(grid_populator_big(solution,emp_Inv,workingdays=['Mon','Tue','Wed','Thu','Fri']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_grids_Inv=[]\n",
    "for solution in Inv_best_solns:\n",
    "    best_grids_Inv.append(grid_populator_big(solution,emp_Inv,workingdays=['Mon','Tue','Wed','Thu','Fri']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "all_grids_Inv=[]\n",
    "for solution in sol_Inv:\n",
    "    all_grids_Inv.append(grid_populator_big(solution,emp_Inv,workingdays=['Mon','Tue','Wed','Thu','Fri']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5760"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(all_grids_Inv)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Inventory & Production                  9\n",
       "Information Technology                  8\n",
       "Supply chain(SCM)                       7\n",
       "Operations                              6\n",
       "Sales                                   6\n",
       "Finance+Marketing+General Management    6\n",
       "Procurement                             5\n",
       "Human Resources                         3\n",
       "Name: DEPARTMENT, dtype: int64"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.DEPARTMENT.value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**FMGM**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_fmgm=constraint.Problem()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_fmgm.addVariable('Sompop ChangMon',[0])\n",
      "problem_fmgm.addVariable('Sompop ChangTue',[0,1])\n",
      "problem_fmgm.addVariable('Sompop ChangWed',[0,1])\n",
      "problem_fmgm.addVariable('Sompop ChangThu',[0,1])\n",
      "problem_fmgm.addVariable('Sompop ChangFri',[0,1])\n",
      "problem_fmgm.addVariable('CalvinMon',[0,1])\n",
      "problem_fmgm.addVariable('CalvinTue',[0,1])\n",
      "problem_fmgm.addVariable('CalvinWed',[0,1])\n",
      "problem_fmgm.addVariable('CalvinThu',[0,1])\n",
      "problem_fmgm.addVariable('CalvinFri',[0])\n",
      "problem_fmgm.addVariable('JustinMon',[0,1])\n",
      "problem_fmgm.addVariable('JustinTue',[0,1])\n",
      "problem_fmgm.addVariable('JustinWed',[0])\n",
      "problem_fmgm.addVariable('JustinThu',[0,1])\n",
      "problem_fmgm.addVariable('JustinFri',[0,1])\n",
      "problem_fmgm.addVariable('AlexMon',[0,1])\n",
      "problem_fmgm.addVariable('AlexTue',[1])\n",
      "problem_fmgm.addVariable('AlexWed',[0,1])\n",
      "problem_fmgm.addVariable('AlexThu',[0,1])\n",
      "problem_fmgm.addVariable('AlexFri',[0,1])\n",
      "problem_fmgm.addVariable('Massimo HimmelfarbMon',[0,1])\n",
      "problem_fmgm.addVariable('Massimo HimmelfarbTue',[0,1])\n",
      "problem_fmgm.addVariable('Massimo HimmelfarbWed',[1])\n",
      "problem_fmgm.addVariable('Massimo HimmelfarbThu',[0,1])\n",
      "problem_fmgm.addVariable('Massimo HimmelfarbFri',[0,1])\n",
      "problem_fmgm.addVariable('Tadamitsu CarrowMon',[0,1])\n",
      "problem_fmgm.addVariable('Tadamitsu CarrowTue',[0,1])\n",
      "problem_fmgm.addVariable('Tadamitsu CarrowWed',[0,1])\n",
      "problem_fmgm.addVariable('Tadamitsu CarrowThu',[1])\n",
      "problem_fmgm.addVariable('Tadamitsu CarrowFri',[0,1])\n",
      "Added 30 variables\n"
     ]
    }
   ],
   "source": [
    "variable_generator(FMGM_nd,'problem_fmgm')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_fmgm.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
      "(\"Sompop ChangMon\", \"Sompop ChangTue\",\"Sompop ChangWed\",\"Sompop ChangThu\",\"Sompop ChangFri\"))\n",
      "problem_fmgm.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
      "(\"CalvinMon\", \"CalvinTue\",\"CalvinWed\",\"CalvinThu\",\"CalvinFri\"))\n",
      "problem_fmgm.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
      "(\"JustinMon\", \"JustinTue\",\"JustinWed\",\"JustinThu\",\"JustinFri\"))\n",
      "problem_fmgm.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
      "(\"AlexMon\", \"AlexTue\",\"AlexWed\",\"AlexThu\",\"AlexFri\"))\n",
      "problem_fmgm.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
      "(\"Massimo HimmelfarbMon\", \"Massimo HimmelfarbTue\",\"Massimo HimmelfarbWed\",\"Massimo HimmelfarbThu\",\"Massimo HimmelfarbFri\"))\n",
      "problem_fmgm.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
      "(\"Tadamitsu CarrowMon\", \"Tadamitsu CarrowTue\",\"Tadamitsu CarrowWed\",\"Tadamitsu CarrowThu\",\"Tadamitsu CarrowFri\"))\n"
     ]
    }
   ],
   "source": [
    "constraint_generator(FMGM_nd, 'problem_fmgm')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_fmgm.addVariable('Sompop ChangMon',[0])\n",
    "problem_fmgm.addVariable('Sompop ChangTue',[0,1])\n",
    "problem_fmgm.addVariable('Sompop ChangWed',[0,1])\n",
    "problem_fmgm.addVariable('Sompop ChangThu',[0,1])\n",
    "problem_fmgm.addVariable('Sompop ChangFri',[0,1])\n",
    "problem_fmgm.addVariable('CalvinMon',[0,1])\n",
    "problem_fmgm.addVariable('CalvinTue',[0,1])\n",
    "problem_fmgm.addVariable('CalvinWed',[0,1])\n",
    "problem_fmgm.addVariable('CalvinThu',[0,1])\n",
    "problem_fmgm.addVariable('CalvinFri',[0,1])\n",
    "problem_fmgm.addVariable('JustinMon',[0,1])\n",
    "problem_fmgm.addVariable('JustinTue',[0,1])\n",
    "problem_fmgm.addVariable('JustinWed',[0])\n",
    "problem_fmgm.addVariable('JustinThu',[0,1])\n",
    "problem_fmgm.addVariable('JustinFri',[0,1])\n",
    "problem_fmgm.addVariable('AlexMon',[0,1])\n",
    "problem_fmgm.addVariable('AlexTue',[1])\n",
    "problem_fmgm.addVariable('AlexWed',[0,1])\n",
    "problem_fmgm.addVariable('AlexThu',[0,1])\n",
    "problem_fmgm.addVariable('AlexFri',[0,1])\n",
    "problem_fmgm.addVariable('Massimo HimmelfarbMon',[0,1])\n",
    "problem_fmgm.addVariable('Massimo HimmelfarbTue',[0,1])\n",
    "problem_fmgm.addVariable('Massimo HimmelfarbWed',[0,1])\n",
    "problem_fmgm.addVariable('Massimo HimmelfarbThu',[0,1])\n",
    "problem_fmgm.addVariable('Massimo HimmelfarbFri',[0,1])\n",
    "problem_fmgm.addVariable('Tadamitsu CarrowMon',[0,1])\n",
    "problem_fmgm.addVariable('Tadamitsu CarrowTue',[0,1])\n",
    "problem_fmgm.addVariable('Tadamitsu CarrowWed',[0,1])\n",
    "problem_fmgm.addVariable('Tadamitsu CarrowThu',[1])\n",
    "problem_fmgm.addVariable('Tadamitsu CarrowFri',[0,1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_fmgm.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"Sompop ChangMon\", \"Sompop ChangTue\",\"Sompop ChangWed\",\"Sompop ChangThu\",\"Sompop ChangFri\"))\n",
    "problem_fmgm.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"CalvinMon\", \"CalvinTue\",\"CalvinWed\",\"CalvinThu\",\"CalvinFri\"))\n",
    "problem_fmgm.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
    "(\"JustinMon\", \"JustinTue\",\"JustinWed\",\"JustinThu\",\"JustinFri\"))\n",
    "problem_fmgm.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
    "(\"AlexMon\", \"AlexTue\",\"AlexWed\",\"AlexThu\",\"AlexFri\"))\n",
    "problem_fmgm.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
    "(\"Massimo HimmelfarbMon\", \"Massimo HimmelfarbTue\",\"Massimo HimmelfarbWed\",\"Massimo HimmelfarbThu\",\"Massimo HimmelfarbFri\"))\n",
    "problem_fmgm.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
    "(\"Tadamitsu CarrowMon\", \"Tadamitsu CarrowTue\",\"Tadamitsu CarrowWed\",\"Tadamitsu CarrowThu\",\"Tadamitsu CarrowFri\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  solution_function 0.2257840633392334\n"
     ]
    }
   ],
   "source": [
    "sol_fmgm=solution_function(problem_fmgm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1440"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(sol_fmgm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  consolidated_function_mod 48.99046874046326\n"
     ]
    }
   ],
   "source": [
    "fmgm_int_total=consolidated_function_mod(sol_fmgm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{2.0, 3.0, 4.0, 5.0, 6.0}"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(fmgm_int_total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [],
   "source": [
    "bad_index_fmgm=list_index_returner(fmgm_int_total, max(fmgm_int_total))\n",
    "bad_solns_fmgm=[sol_fmgm[i] for i in bad_index_fmgm]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "good_index_fmgm=list_index_returner(fmgm_int_total, min(fmgm_int_total))\n",
    "len(good_index_fmgm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1440"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "all_grids_fmgm=[]\n",
    "for solution in sol_fmgm:\n",
    "    all_grids_fmgm.append(grid_populator_big(solution,emp_FMGM,workingdays=['Mon','Tue','Wed','Thu','Fri']))\n",
    "len(all_grids_fmgm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "712"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bad_grids_fmgm=[]\n",
    "for solution in bad_solns_fmgm:\n",
    "    bad_grids_fmgm.append(grid_populator_big(solution,emp_FMGM,workingdays=['Mon','Tue','Wed','Thu','Fri']))\n",
    "len(bad_grids_fmgm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Information Technology**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_IT=constraint.Problem(BacktrackingSolver())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_IT.addVariable('Tara CantrockMon',[0,1])\n",
      "problem_IT.addVariable('Tara CantrockTue',[0,1])\n",
      "problem_IT.addVariable('Tara CantrockWed',[0,1])\n",
      "problem_IT.addVariable('Tara CantrockThu',[0,1])\n",
      "problem_IT.addVariable('Tara CantrockFri',[1])\n",
      "problem_IT.addVariable('JoshuaMon',[0,1])\n",
      "problem_IT.addVariable('JoshuaTue',[0,1])\n",
      "problem_IT.addVariable('JoshuaWed',[0])\n",
      "problem_IT.addVariable('JoshuaThu',[0,1])\n",
      "problem_IT.addVariable('JoshuaFri',[0,1])\n",
      "problem_IT.addVariable('CalebMon',[0,1])\n",
      "problem_IT.addVariable('CalebTue',[0,1])\n",
      "problem_IT.addVariable('CalebWed',[0,1])\n",
      "problem_IT.addVariable('CalebThu',[0,1])\n",
      "problem_IT.addVariable('CalebFri',[0])\n",
      "problem_IT.addVariable('RyanMon',[0,1])\n",
      "problem_IT.addVariable('RyanTue',[0,1])\n",
      "problem_IT.addVariable('RyanWed',[0,1])\n",
      "problem_IT.addVariable('RyanThu',[1])\n",
      "problem_IT.addVariable('RyanFri',[0,1])\n",
      "problem_IT.addVariable('Tanzeer CaoMon',[0,1])\n",
      "problem_IT.addVariable('Tanzeer CaoTue',[0,1])\n",
      "problem_IT.addVariable('Tanzeer CaoWed',[0,1])\n",
      "problem_IT.addVariable('Tanzeer CaoThu',[0,1])\n",
      "problem_IT.addVariable('Tanzeer CaoFri',[1])\n",
      "problem_IT.addVariable('Ted BrownMon',[0,1])\n",
      "problem_IT.addVariable('Ted BrownTue',[0,1])\n",
      "problem_IT.addVariable('Ted BrownWed',[0,1])\n",
      "problem_IT.addVariable('Ted BrownThu',[0])\n",
      "problem_IT.addVariable('Ted BrownFri',[0,1])\n",
      "problem_IT.addVariable('Tae CarrilloMon',[0,1])\n",
      "problem_IT.addVariable('Tae CarrilloTue',[1])\n",
      "problem_IT.addVariable('Tae CarrilloWed',[0,1])\n",
      "problem_IT.addVariable('Tae CarrilloThu',[0,1])\n",
      "problem_IT.addVariable('Tae CarrilloFri',[0,1])\n",
      "problem_IT.addVariable('Thanadtha BrownMon',[1])\n",
      "problem_IT.addVariable('Thanadtha BrownTue',[0,1])\n",
      "problem_IT.addVariable('Thanadtha BrownWed',[0,1])\n",
      "problem_IT.addVariable('Thanadtha BrownThu',[0,1])\n",
      "problem_IT.addVariable('Thanadtha BrownFri',[0,1])\n",
      "Added 40 variables\n"
     ]
    }
   ],
   "source": [
    "variable_generator(IT_nd,'problem_IT')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
      "(\"Tara CantrockMon\", \"Tara CantrockTue\",\"Tara CantrockWed\",\"Tara CantrockThu\",\"Tara CantrockFri\"))\n",
      "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
      "(\"JoshuaMon\", \"JoshuaTue\",\"JoshuaWed\",\"JoshuaThu\",\"JoshuaFri\"))\n",
      "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
      "(\"CalebMon\", \"CalebTue\",\"CalebWed\",\"CalebThu\",\"CalebFri\"))\n",
      "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
      "(\"RyanMon\", \"RyanTue\",\"RyanWed\",\"RyanThu\",\"RyanFri\"))\n",
      "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
      "(\"Tanzeer CaoMon\", \"Tanzeer CaoTue\",\"Tanzeer CaoWed\",\"Tanzeer CaoThu\",\"Tanzeer CaoFri\"))\n",
      "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
      "(\"Ted BrownMon\", \"Ted BrownTue\",\"Ted BrownWed\",\"Ted BrownThu\",\"Ted BrownFri\"))\n",
      "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 4,\n",
      "(\"Tae CarrilloMon\", \"Tae CarrilloTue\",\"Tae CarrilloWed\",\"Tae CarrilloThu\",\"Tae CarrilloFri\"))\n",
      "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
      "(\"Thanadtha BrownMon\", \"Thanadtha BrownTue\",\"Thanadtha BrownWed\",\"Thanadtha BrownThu\",\"Thanadtha BrownFri\"))\n"
     ]
    }
   ],
   "source": [
    "constraint_generator(IT_nd,'problem_IT')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_IT.addVariable('Tara CantrockMon',[0,1])\n",
    "problem_IT.addVariable('Tara CantrockTue',[0,1])\n",
    "problem_IT.addVariable('Tara CantrockWed',[0,1])\n",
    "problem_IT.addVariable('Tara CantrockThu',[0,1])\n",
    "problem_IT.addVariable('Tara CantrockFri',[0,1])\n",
    "problem_IT.addVariable('JoshuaMon',[0,1])\n",
    "problem_IT.addVariable('JoshuaTue',[0,1])\n",
    "problem_IT.addVariable('JoshuaWed',[1])\n",
    "problem_IT.addVariable('JoshuaThu',[0,1])\n",
    "problem_IT.addVariable('JoshuaFri',[0,1])\n",
    "problem_IT.addVariable('CalebMon',[0,1])\n",
    "problem_IT.addVariable('CalebTue',[0])\n",
    "problem_IT.addVariable('CalebWed',[0,1])\n",
    "problem_IT.addVariable('CalebThu',[0,1])\n",
    "problem_IT.addVariable('CalebFri',[0,1])\n",
    "problem_IT.addVariable('RyanMon',[0,1])\n",
    "problem_IT.addVariable('RyanTue',[0,1])\n",
    "problem_IT.addVariable('RyanWed',[0,1])\n",
    "problem_IT.addVariable('RyanThu',[0,1])\n",
    "problem_IT.addVariable('RyanFri',[0,1])\n",
    "problem_IT.addVariable('Tanzeer CaoMon',[0])\n",
    "problem_IT.addVariable('Tanzeer CaoTue',[0,1])\n",
    "problem_IT.addVariable('Tanzeer CaoWed',[0,1])\n",
    "problem_IT.addVariable('Tanzeer CaoThu',[1])\n",
    "problem_IT.addVariable('Tanzeer CaoFri',[0,1])\n",
    "problem_IT.addVariable('Ted BrownMon',[0,1])\n",
    "problem_IT.addVariable('Ted BrownTue',[1])\n",
    "problem_IT.addVariable('Ted BrownWed',[0,1])\n",
    "problem_IT.addVariable('Ted BrownThu',[0,1])\n",
    "problem_IT.addVariable('Ted BrownFri',[0,1])\n",
    "problem_IT.addVariable('Tae CarrilloMon',[0,1])\n",
    "problem_IT.addVariable('Tae CarrilloTue',[1])\n",
    "problem_IT.addVariable('Tae CarrilloWed',[0,1])\n",
    "problem_IT.addVariable('Tae CarrilloThu',[0,1])\n",
    "problem_IT.addVariable('Tae CarrilloFri',[0,1])\n",
    "problem_IT.addVariable('Thanadtha BrownMon',[1])\n",
    "problem_IT.addVariable('Thanadtha BrownTue',[0,1])\n",
    "problem_IT.addVariable('Thanadtha BrownWed',[0,1])\n",
    "problem_IT.addVariable('Thanadtha BrownThu',[0,1])\n",
    "problem_IT.addVariable('Thanadtha BrownFri',[0,1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"Tara CantrockMon\", \"Tara CantrockTue\",\"Tara CantrockWed\",\"Tara CantrockThu\",\"Tara CantrockFri\"))\n",
    "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
    "(\"JoshuaMon\", \"JoshuaTue\",\"JoshuaWed\",\"JoshuaThu\",\"JoshuaFri\"))\n",
    "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
    "(\"CalebMon\", \"CalebTue\",\"CalebWed\",\"CalebThu\",\"CalebFri\"))\n",
    "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"RyanMon\", \"RyanTue\",\"RyanWed\",\"RyanThu\",\"RyanFri\"))\n",
    "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
    "(\"Tanzeer CaoMon\", \"Tanzeer CaoTue\",\"Tanzeer CaoWed\",\"Tanzeer CaoThu\",\"Tanzeer CaoFri\"))\n",
    "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
    "(\"Ted BrownMon\", \"Ted BrownTue\",\"Ted BrownWed\",\"Ted BrownThu\",\"Ted BrownFri\"))\n",
    "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
    "(\"Tae CarrilloMon\", \"Tae CarrilloTue\",\"Tae CarrilloWed\",\"Tae CarrilloThu\",\"Tae CarrilloFri\"))\n",
    "problem_IT.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
    "(\"Thanadtha BrownMon\", \"Thanadtha BrownTue\",\"Thanadtha BrownWed\",\"Thanadtha BrownThu\",\"Thanadtha BrownFri\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  solution_function 0.7567458152770996\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "3456"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sol_IT=solution_function(problem_IT)\n",
    "len(sol_IT)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  consolidated_function_mod 159.94392704963684\n"
     ]
    }
   ],
   "source": [
    "IT_int_total=consolidated_function_mod(sol_IT)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0}"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(IT_int_total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [],
   "source": [
    "stretch=list_index_returner(IT_int_total,5)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 263,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 263,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "good_index_IT=list_index_returner(IT_int_total,min(IT_int_total))\n",
    "bad_index_IT=list_index_returner(IT_int_total,max(IT_int_total))\n",
    "len(good_index_IT)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 264,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 264,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "IT_bad_solns=[sol_IT[i] for i in bad_index_IT]\n",
    "IT_best_solns=[sol_IT[i] for i in good_index_IT]\n",
    "len(IT_best_solns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 265,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27"
      ]
     },
     "execution_count": 265,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bad_grids_IT=[]\n",
    "for solution in IT_bad_solns:\n",
    "    bad_grids_IT.append(grid_populator_big(solution,emp_IT,workingdays=['Mon','Tue','Wed','Thu','Fri']))\n",
    "len(bad_grids_IT)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 266,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_grids_IT=[]\n",
    "for solution in IT_best_solns:\n",
    "    best_grids_IT.append(grid_populator_big(solution,emp_IT,workingdays=['Mon','Tue','Wed','Thu','Fri']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 267,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3456"
      ]
     },
     "execution_count": 267,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "all_grids_IT=[]\n",
    "for solution in sol_IT:\n",
    "    all_grids_IT.append(grid_populator_big(solution,emp_IT,workingdays=['Mon','Tue','Wed','Thu','Fri']))\n",
    "len(all_grids_IT)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 268,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27"
      ]
     },
     "execution_count": 268,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(bad_grids_IT)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**SCM**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_SCM.addVariable('JaxMon',[0,1])\n",
      "problem_SCM.addVariable('JaxTue',[0,1])\n",
      "problem_SCM.addVariable('JaxWed',[1])\n",
      "problem_SCM.addVariable('JaxThu',[0,1])\n",
      "problem_SCM.addVariable('JaxFri',[0,1])\n",
      "problem_SCM.addVariable('BarrettMon',[0,1])\n",
      "problem_SCM.addVariable('BarrettTue',[0,1])\n",
      "problem_SCM.addVariable('BarrettWed',[0,1])\n",
      "problem_SCM.addVariable('BarrettThu',[0,1])\n",
      "problem_SCM.addVariable('BarrettFri',[0])\n",
      "problem_SCM.addVariable('MaximusMon',[0,1])\n",
      "problem_SCM.addVariable('MaximusTue',[0,1])\n",
      "problem_SCM.addVariable('MaximusWed',[0])\n",
      "problem_SCM.addVariable('MaximusThu',[0,1])\n",
      "problem_SCM.addVariable('MaximusFri',[0,1])\n",
      "problem_SCM.addVariable('BrandonMon',[0,1])\n",
      "problem_SCM.addVariable('BrandonTue',[0,1])\n",
      "problem_SCM.addVariable('BrandonWed',[0])\n",
      "problem_SCM.addVariable('BrandonThu',[0,1])\n",
      "problem_SCM.addVariable('BrandonFri',[0,1])\n",
      "problem_SCM.addVariable('BrantleyMon',[1])\n",
      "problem_SCM.addVariable('BrantleyTue',[0,1])\n",
      "problem_SCM.addVariable('BrantleyWed',[0,1])\n",
      "problem_SCM.addVariable('BrantleyThu',[0,1])\n",
      "problem_SCM.addVariable('BrantleyFri',[0,1])\n",
      "problem_SCM.addVariable('AlejandroMon',[0,1])\n",
      "problem_SCM.addVariable('AlejandroTue',[0,1])\n",
      "problem_SCM.addVariable('AlejandroWed',[0,1])\n",
      "problem_SCM.addVariable('AlejandroThu',[0,1])\n",
      "problem_SCM.addVariable('AlejandroFri',[0])\n",
      "problem_SCM.addVariable('GrantMon',[0,1])\n",
      "problem_SCM.addVariable('GrantTue',[0])\n",
      "problem_SCM.addVariable('GrantWed',[0,1])\n",
      "problem_SCM.addVariable('GrantThu',[0,1])\n",
      "problem_SCM.addVariable('GrantFri',[0,1])\n",
      "Added 35 variables\n"
     ]
    }
   ],
   "source": [
    "variable_generator(SCM_nd,'problem_SCM')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_SCM.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
      "(\"JaxMon\", \"JaxTue\",\"JaxWed\",\"JaxThu\",\"JaxFri\"))\n",
      "problem_SCM.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
      "(\"BarrettMon\", \"BarrettTue\",\"BarrettWed\",\"BarrettThu\",\"BarrettFri\"))\n",
      "problem_SCM.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
      "(\"MaximusMon\", \"MaximusTue\",\"MaximusWed\",\"MaximusThu\",\"MaximusFri\"))\n",
      "problem_SCM.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
      "(\"BrandonMon\", \"BrandonTue\",\"BrandonWed\",\"BrandonThu\",\"BrandonFri\"))\n",
      "problem_SCM.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
      "(\"BrantleyMon\", \"BrantleyTue\",\"BrantleyWed\",\"BrantleyThu\",\"BrantleyFri\"))\n",
      "problem_SCM.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 4,\n",
      "(\"AlejandroMon\", \"AlejandroTue\",\"AlejandroWed\",\"AlejandroThu\",\"AlejandroFri\"))\n",
      "problem_SCM.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
      "(\"GrantMon\", \"GrantTue\",\"GrantWed\",\"GrantThu\",\"GrantFri\"))\n"
     ]
    }
   ],
   "source": [
    "constraint_generator(SCM_nd,'problem_SCM')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_SCM.addVariable('JaxMon',[0,1])\n",
    "problem_SCM.addVariable('JaxTue',[0,1])\n",
    "problem_SCM.addVariable('JaxWed',[1])\n",
    "problem_SCM.addVariable('JaxThu',[0,1])\n",
    "problem_SCM.addVariable('JaxFri',[0,1])\n",
    "problem_SCM.addVariable('BarrettMon',[0,1])\n",
    "problem_SCM.addVariable('BarrettTue',[0,1])\n",
    "problem_SCM.addVariable('BarrettWed',[0,1])\n",
    "problem_SCM.addVariable('BarrettThu',[0,1])\n",
    "problem_SCM.addVariable('BarrettFri',[0])\n",
    "problem_SCM.addVariable('MaximusMon',[0,1])\n",
    "problem_SCM.addVariable('MaximusTue',[0,1])\n",
    "problem_SCM.addVariable('MaximusWed',[0])\n",
    "problem_SCM.addVariable('MaximusThu',[0,1])\n",
    "problem_SCM.addVariable('MaximusFri',[0,1])\n",
    "problem_SCM.addVariable('BrandonMon',[0,1])\n",
    "problem_SCM.addVariable('BrandonTue',[0,1])\n",
    "problem_SCM.addVariable('BrandonWed',[0])\n",
    "problem_SCM.addVariable('BrandonThu',[0,1])\n",
    "problem_SCM.addVariable('BrandonFri',[0,1])\n",
    "problem_SCM.addVariable('BrantleyMon',[1])\n",
    "problem_SCM.addVariable('BrantleyTue',[0,1])\n",
    "problem_SCM.addVariable('BrantleyWed',[0,1])\n",
    "problem_SCM.addVariable('BrantleyThu',[0,1])\n",
    "problem_SCM.addVariable('BrantleyFri',[0,1])\n",
    "problem_SCM.addVariable('AlejandroMon',[0,1])\n",
    "problem_SCM.addVariable('AlejandroTue',[0,1])\n",
    "problem_SCM.addVariable('AlejandroWed',[0,1])\n",
    "problem_SCM.addVariable('AlejandroThu',[0,1])\n",
    "problem_SCM.addVariable('AlejandroFri',[0])\n",
    "problem_SCM.addVariable('GrantMon',[0,1])\n",
    "problem_SCM.addVariable('GrantTue',[0])\n",
    "problem_SCM.addVariable('GrantWed',[0,1])\n",
    "problem_SCM.addVariable('GrantThu',[0,1])\n",
    "problem_SCM.addVariable('GrantFri',[0,1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_SCM.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
    "(\"JaxMon\", \"JaxTue\",\"JaxWed\",\"JaxThu\",\"JaxFri\"))\n",
    "problem_SCM.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
    "(\"BarrettMon\", \"BarrettTue\",\"BarrettWed\",\"BarrettThu\",\"BarrettFri\"))\n",
    "problem_SCM.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
    "(\"MaximusMon\", \"MaximusTue\",\"MaximusWed\",\"MaximusThu\",\"MaximusFri\"))\n",
    "problem_SCM.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
    "(\"BrandonMon\", \"BrandonTue\",\"BrandonWed\",\"BrandonThu\",\"BrandonFri\"))\n",
    "problem_SCM.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
    "(\"BrantleyMon\", \"BrantleyTue\",\"BrantleyWed\",\"BrantleyThu\",\"BrantleyFri\"))\n",
    "problem_SCM.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"AlejandroMon\", \"AlejandroTue\",\"AlejandroWed\",\"AlejandroThu\",\"AlejandroFri\"))\n",
    "problem_SCM.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"GrantMon\", \"GrantTue\",\"GrantWed\",\"GrantThu\",\"GrantFri\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  solution_function 0.10936641693115234\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "256"
      ]
     },
     "execution_count": 155,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sol_SCM=solution_function(problem_SCM)\n",
    "len(sol_SCM)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  consolidated_function_mod 9.073949337005615\n"
     ]
    }
   ],
   "source": [
    "SCM_int_total=consolidated_function_mod(sol_SCM)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{3.0, 4.0, 5.0, 6.0, 7.0}"
      ]
     },
     "execution_count": 167,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(SCM_int_total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "metadata": {},
   "outputs": [],
   "source": [
    "good_index_SCM=min_indices(SCM_int_total, min(SCM_int_total))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [],
   "source": [
    "bad_index_SCM=min_indices(SCM_int_total, max(SCM_int_total))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 170,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(min_indices(SCM_int_total, 11))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {},
   "outputs": [],
   "source": [
    "SCM_bad_solns=[sol_SCM[i] for i in bad_index_SCM]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [],
   "source": [
    "SCM_best_solns=[sol_SCM[i] for i in good_index_SCM]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "metadata": {},
   "outputs": [],
   "source": [
    "bad_grids_SCM=[]\n",
    "for solution in SCM_bad_solns:\n",
    "    bad_grids_SCM.append(grid_populator_big(solution,emp_SCM,workingdays=['Mon','Tue','Wed','Thu','Fri']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_grids_SCM=[]\n",
    "for solution in SCM_best_solns:\n",
    "    best_grids_SCM.append(grid_populator_big(solution,emp_SCM,workingdays=['Mon','Tue','Wed','Thu','Fri']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 175,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(best_grids_SCM)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mon</th>\n",
       "      <th>Tue</th>\n",
       "      <th>Wed</th>\n",
       "      <th>Thu</th>\n",
       "      <th>Fri</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Jax</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Barrett</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Maximus</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Brandon</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Brantley</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Alejandro</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Grant</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Mon  Tue  Wed  Thu  Fri\n",
       "Jax        0.0  0.0  1.0  0.0  0.0\n",
       "Barrett    1.0  0.0  0.0  0.0  0.0\n",
       "Maximus    1.0  0.0  0.0  1.0  1.0\n",
       "Brandon    1.0  0.0  0.0  1.0  1.0\n",
       "Brantley   1.0  0.0  1.0  0.0  0.0\n",
       "Alejandro  0.0  0.0  0.0  0.0  0.0\n",
       "Grant      0.0  0.0  0.0  0.0  0.0"
      ]
     },
     "execution_count": 176,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bad_grids_SCM[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 177,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(bad_grids_SCM)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Operations**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_OP=constraint.Problem(BacktrackingSolver())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_OP.addVariable('Michelle GrusqMon',[0,1])\n",
      "problem_OP.addVariable('Michelle GrusqTue',[0,1])\n",
      "problem_OP.addVariable('Michelle GrusqWed',[1])\n",
      "problem_OP.addVariable('Michelle GrusqThu',[0,1])\n",
      "problem_OP.addVariable('Michelle GrusqFri',[0,1])\n",
      "problem_OP.addVariable('Ryan ClokeMon',[0])\n",
      "problem_OP.addVariable('Ryan ClokeTue',[0,1])\n",
      "problem_OP.addVariable('Ryan ClokeWed',[0,1])\n",
      "problem_OP.addVariable('Ryan ClokeThu',[0,1])\n",
      "problem_OP.addVariable('Ryan ClokeFri',[0,1])\n",
      "problem_OP.addVariable('Ophir FriedmanMon',[0,1])\n",
      "problem_OP.addVariable('Ophir FriedmanTue',[0,1])\n",
      "problem_OP.addVariable('Ophir FriedmanWed',[0])\n",
      "problem_OP.addVariable('Ophir FriedmanThu',[0,1])\n",
      "problem_OP.addVariable('Ophir FriedmanFri',[0,1])\n",
      "problem_OP.addVariable('Nicole GaoMon',[0,1])\n",
      "problem_OP.addVariable('Nicole GaoTue',[0,1])\n",
      "problem_OP.addVariable('Nicole GaoWed',[0,1])\n",
      "problem_OP.addVariable('Nicole GaoThu',[0,1])\n",
      "problem_OP.addVariable('Nicole GaoFri',[0])\n",
      "problem_OP.addVariable('Rui CockleMon',[0,1])\n",
      "problem_OP.addVariable('Rui CockleTue',[0,1])\n",
      "problem_OP.addVariable('Rui CockleWed',[0,1])\n",
      "problem_OP.addVariable('Rui CockleThu',[1])\n",
      "problem_OP.addVariable('Rui CockleFri',[0,1])\n",
      "problem_OP.addVariable('Noelle FuMon',[0,1])\n",
      "problem_OP.addVariable('Noelle FuTue',[0,1])\n",
      "problem_OP.addVariable('Noelle FuWed',[0,1])\n",
      "problem_OP.addVariable('Noelle FuThu',[1])\n",
      "problem_OP.addVariable('Noelle FuFri',[0,1])\n",
      "Added 30 variables\n"
     ]
    }
   ],
   "source": [
    "variable_generator(OP_nd,'problem_OP')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_OP.addVariable('Michelle GrusqMon',[0,1])\n",
    "problem_OP.addVariable('Michelle GrusqTue',[0,1])\n",
    "problem_OP.addVariable('Michelle GrusqWed',[0,1])\n",
    "problem_OP.addVariable('Michelle GrusqThu',[0,1])\n",
    "problem_OP.addVariable('Michelle GrusqFri',[0,1])\n",
    "problem_OP.addVariable('Ryan ClokeMon',[0,1])\n",
    "problem_OP.addVariable('Ryan ClokeTue',[0,1])\n",
    "problem_OP.addVariable('Ryan ClokeWed',[0,1])\n",
    "problem_OP.addVariable('Ryan ClokeThu',[0,1])\n",
    "problem_OP.addVariable('Ryan ClokeFri',[0,1])\n",
    "problem_OP.addVariable('Ophir FriedmanMon',[0,1])\n",
    "problem_OP.addVariable('Ophir FriedmanTue',[0,1])\n",
    "problem_OP.addVariable('Ophir FriedmanWed',[0,1])\n",
    "problem_OP.addVariable('Ophir FriedmanThu',[0,1])\n",
    "problem_OP.addVariable('Ophir FriedmanFri',[0,1])\n",
    "problem_OP.addVariable('Nicole GaoMon',[0,1])\n",
    "problem_OP.addVariable('Nicole GaoTue',[0,1])\n",
    "problem_OP.addVariable('Nicole GaoWed',[0,1])\n",
    "problem_OP.addVariable('Nicole GaoThu',[0,1])\n",
    "problem_OP.addVariable('Nicole GaoFri',[0])\n",
    "problem_OP.addVariable('Rui CockleMon',[0,1])\n",
    "problem_OP.addVariable('Rui CockleTue',[0,1])\n",
    "problem_OP.addVariable('Rui CockleWed',[0,1])\n",
    "problem_OP.addVariable('Rui CockleThu',[0,1])\n",
    "problem_OP.addVariable('Rui CockleFri',[0,1])\n",
    "problem_OP.addVariable('Noelle FuMon',[0,1])\n",
    "problem_OP.addVariable('Noelle FuTue',[0,1])\n",
    "problem_OP.addVariable('Noelle FuWed',[0,1])\n",
    "problem_OP.addVariable('Noelle FuThu',[1])\n",
    "problem_OP.addVariable('Noelle FuFri',[0,1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_OP.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
      "(\"Michelle GrusqMon\", \"Michelle GrusqTue\",\"Michelle GrusqWed\",\"Michelle GrusqThu\",\"Michelle GrusqFri\"))\n",
      "problem_OP.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
      "(\"Ryan ClokeMon\", \"Ryan ClokeTue\",\"Ryan ClokeWed\",\"Ryan ClokeThu\",\"Ryan ClokeFri\"))\n",
      "problem_OP.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
      "(\"Ophir FriedmanMon\", \"Ophir FriedmanTue\",\"Ophir FriedmanWed\",\"Ophir FriedmanThu\",\"Ophir FriedmanFri\"))\n",
      "problem_OP.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 4,\n",
      "(\"Nicole GaoMon\", \"Nicole GaoTue\",\"Nicole GaoWed\",\"Nicole GaoThu\",\"Nicole GaoFri\"))\n",
      "problem_OP.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 5,\n",
      "(\"Rui CockleMon\", \"Rui CockleTue\",\"Rui CockleWed\",\"Rui CockleThu\",\"Rui CockleFri\"))\n",
      "problem_OP.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
      "(\"Noelle FuMon\", \"Noelle FuTue\",\"Noelle FuWed\",\"Noelle FuThu\",\"Noelle FuFri\"))\n"
     ]
    }
   ],
   "source": [
    "constraint_generator(OP_nd, 'problem_OP')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_OP.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
    "(\"Michelle GrusqMon\", \"Michelle GrusqTue\",\"Michelle GrusqWed\",\"Michelle GrusqThu\",\"Michelle GrusqFri\"))\n",
    "problem_OP.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
    "(\"Ryan ClokeMon\", \"Ryan ClokeTue\",\"Ryan ClokeWed\",\"Ryan ClokeThu\",\"Ryan ClokeFri\"))\n",
    "problem_OP.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
    "(\"Ophir FriedmanMon\", \"Ophir FriedmanTue\",\"Ophir FriedmanWed\",\"Ophir FriedmanThu\",\"Ophir FriedmanFri\"))\n",
    "problem_OP.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"Nicole GaoMon\", \"Nicole GaoTue\",\"Nicole GaoWed\",\"Nicole GaoThu\",\"Nicole GaoFri\"))\n",
    "problem_OP.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"Rui CockleMon\", \"Rui CockleTue\",\"Rui CockleWed\",\"Rui CockleThu\",\"Rui CockleFri\"))\n",
    "problem_OP.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
    "(\"Noelle FuMon\", \"Noelle FuTue\",\"Noelle FuWed\",\"Noelle FuThu\",\"Noelle FuFri\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  solution_function 0.2141411304473877\n"
     ]
    }
   ],
   "source": [
    "sol_OP=solution_function(problem_OP)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1000"
      ]
     },
     "execution_count": 184,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(sol_OP)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  consolidated_function_mod 32.01846694946289\n"
     ]
    }
   ],
   "source": [
    "OP_int_total=consolidated_function_mod(sol_OP)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{2.0, 3.0, 4.0, 5.0, 6.0}"
      ]
     },
     "execution_count": 186,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(OP_int_total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "metadata": {},
   "outputs": [],
   "source": [
    "bad_index_OP=min_indices(OP_int_total,max(OP_int_total))\n",
    "OP_bad_solns=[sol_OP[i] for i in bad_index_OP]\n",
    "bad_grids_OP=[]\n",
    "for solution in OP_bad_solns:\n",
    "    bad_grids_OP.append(grid_populator_big(solution,emp_OP,workingdays=['Mon','Tue','Wed','Thu','Fri']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "metadata": {},
   "outputs": [],
   "source": [
    "all_grids_OP=[]\n",
    "for solution in sol_OP:\n",
    "    all_grids_OP.append(grid_populator_big(solution,emp_OP,workingdays=['Mon','Tue','Wed','Thu','Fri']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "144"
      ]
     },
     "execution_count": 189,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(bad_grids_OP)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1000"
      ]
     },
     "execution_count": 190,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(all_grids_OP)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**PROCUREMENT**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_Proc=constraint.Problem(BacktrackingSolver())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_Proc.addVariable('Philip DruckmanMon',[0,1])\n",
      "problem_Proc.addVariable('Philip DruckmanTue',[0,1])\n",
      "problem_Proc.addVariable('Philip DruckmanWed',[1])\n",
      "problem_Proc.addVariable('Philip DruckmanThu',[0,1])\n",
      "problem_Proc.addVariable('Philip DruckmanFri',[0,1])\n",
      "problem_Proc.addVariable('Patrick FixlerMon',[0,1])\n",
      "problem_Proc.addVariable('Patrick FixlerTue',[0,1])\n",
      "problem_Proc.addVariable('Patrick FixlerWed',[0,1])\n",
      "problem_Proc.addVariable('Patrick FixlerThu',[0])\n",
      "problem_Proc.addVariable('Patrick FixlerFri',[0,1])\n",
      "problem_Proc.addVariable('Patino ForsythMon',[0,1])\n",
      "problem_Proc.addVariable('Patino ForsythTue',[0,1])\n",
      "problem_Proc.addVariable('Patino ForsythWed',[0,1])\n",
      "problem_Proc.addVariable('Patino ForsythThu',[0,1])\n",
      "problem_Proc.addVariable('Patino ForsythFri',[0])\n",
      "problem_Proc.addVariable('Rikin DavisMon',[0,1])\n",
      "problem_Proc.addVariable('Rikin DavisTue',[0])\n",
      "problem_Proc.addVariable('Rikin DavisWed',[0,1])\n",
      "problem_Proc.addVariable('Rikin DavisThu',[0,1])\n",
      "problem_Proc.addVariable('Rikin DavisFri',[0,1])\n",
      "problem_Proc.addVariable('Patrick FlegalMon',[0,1])\n",
      "problem_Proc.addVariable('Patrick FlegalTue',[0,1])\n",
      "problem_Proc.addVariable('Patrick FlegalWed',[0,1])\n",
      "problem_Proc.addVariable('Patrick FlegalThu',[0])\n",
      "problem_Proc.addVariable('Patrick FlegalFri',[0,1])\n",
      "Added 25 variables\n"
     ]
    }
   ],
   "source": [
    "variable_generator(Proc_nd,'problem_Proc')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_Proc.addVariable('Philip DruckmanMon',[0,1])\n",
    "problem_Proc.addVariable('Philip DruckmanTue',[0,1])\n",
    "problem_Proc.addVariable('Philip DruckmanWed',[0,1])\n",
    "problem_Proc.addVariable('Philip DruckmanThu',[0,1])\n",
    "problem_Proc.addVariable('Philip DruckmanFri',[0,1])\n",
    "problem_Proc.addVariable('Patrick FixlerMon',[0,1])\n",
    "problem_Proc.addVariable('Patrick FixlerTue',[0,1])\n",
    "problem_Proc.addVariable('Patrick FixlerWed',[0,1])\n",
    "problem_Proc.addVariable('Patrick FixlerThu',[0,1])\n",
    "problem_Proc.addVariable('Patrick FixlerFri',[0,1])\n",
    "problem_Proc.addVariable('Patino ForsythMon',[0,1])\n",
    "problem_Proc.addVariable('Patino ForsythTue',[0,1])\n",
    "problem_Proc.addVariable('Patino ForsythWed',[0,1])\n",
    "problem_Proc.addVariable('Patino ForsythThu',[0,1])\n",
    "problem_Proc.addVariable('Patino ForsythFri',[0,1])\n",
    "problem_Proc.addVariable('Rikin DavisMon',[0,1])\n",
    "problem_Proc.addVariable('Rikin DavisTue',[0,1])\n",
    "problem_Proc.addVariable('Rikin DavisWed',[0,1])\n",
    "problem_Proc.addVariable('Rikin DavisThu',[0,1])\n",
    "problem_Proc.addVariable('Rikin DavisFri',[0,1])\n",
    "problem_Proc.addVariable('Patrick FlegalMon',[0,1])\n",
    "problem_Proc.addVariable('Patrick FlegalTue',[0,1])\n",
    "problem_Proc.addVariable('Patrick FlegalWed',[0,1])\n",
    "problem_Proc.addVariable('Patrick FlegalThu',[0,1])\n",
    "problem_Proc.addVariable('Patrick FlegalFri',[0,1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_Proc.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 4,\n",
      "(\"Philip DruckmanMon\", \"Philip DruckmanTue\",\"Philip DruckmanWed\",\"Philip DruckmanThu\",\"Philip DruckmanFri\"))\n",
      "problem_Proc.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
      "(\"Patrick FixlerMon\", \"Patrick FixlerTue\",\"Patrick FixlerWed\",\"Patrick FixlerThu\",\"Patrick FixlerFri\"))\n",
      "problem_Proc.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
      "(\"Patino ForsythMon\", \"Patino ForsythTue\",\"Patino ForsythWed\",\"Patino ForsythThu\",\"Patino ForsythFri\"))\n",
      "problem_Proc.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
      "(\"Rikin DavisMon\", \"Rikin DavisTue\",\"Rikin DavisWed\",\"Rikin DavisThu\",\"Rikin DavisFri\"))\n",
      "problem_Proc.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 4,\n",
      "(\"Patrick FlegalMon\", \"Patrick FlegalTue\",\"Patrick FlegalWed\",\"Patrick FlegalThu\",\"Patrick FlegalFri\"))\n"
     ]
    }
   ],
   "source": [
    "constraint_generator(Proc_nd, 'problem_Proc')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_Proc.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
    "(\"Philip DruckmanMon\", \"Philip DruckmanTue\",\"Philip DruckmanWed\",\"Philip DruckmanThu\",\"Philip DruckmanFri\"))\n",
    "problem_Proc.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"Patrick FixlerMon\", \"Patrick FixlerTue\",\"Patrick FixlerWed\",\"Patrick FixlerThu\",\"Patrick FixlerFri\"))\n",
    "problem_Proc.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
    "(\"Patino ForsythMon\", \"Patino ForsythTue\",\"Patino ForsythWed\",\"Patino ForsythThu\",\"Patino ForsythFri\"))\n",
    "problem_Proc.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
    "(\"Rikin DavisMon\", \"Rikin DavisTue\",\"Rikin DavisWed\",\"Rikin DavisThu\",\"Rikin DavisFri\"))\n",
    "problem_Proc.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 4,\n",
    "(\"Patrick FlegalMon\", \"Patrick FlegalTue\",\"Patrick FlegalWed\",\"Patrick FlegalThu\",\"Patrick FlegalFri\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  solution_function 0.39064645767211914\n"
     ]
    }
   ],
   "source": [
    "sol_Proc=solution_function(problem_Proc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2500"
      ]
     },
     "execution_count": 197,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(sol_Proc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  consolidated_function_mod 85.057621717453\n"
     ]
    }
   ],
   "source": [
    "Proc_int_total=consolidated_function_mod(sol_Proc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 199,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{3.0, 4.0, 5.0, 6.0}"
      ]
     },
     "execution_count": 199,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(Proc_int_total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "metadata": {},
   "outputs": [],
   "source": [
    "all_grids_Proc=[]\n",
    "for solution in sol_Proc:\n",
    "    all_grids_Proc.append((grid_populator_big(solution,emp_proc,workingdays=['Mon','Tue','Wed','Thu','Fri'])))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2500"
      ]
     },
     "execution_count": 201,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(all_grids_Proc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Human Resources**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_HR=constraint.Problem(BacktrackingSolver())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_HR.addVariable('ParkerMon',[0,1])\n",
      "problem_HR.addVariable('ParkerTue',[0])\n",
      "problem_HR.addVariable('ParkerWed',[0,1])\n",
      "problem_HR.addVariable('ParkerThu',[0,1])\n",
      "problem_HR.addVariable('ParkerFri',[0,1])\n",
      "problem_HR.addVariable('JaceMon',[0,1])\n",
      "problem_HR.addVariable('JaceTue',[0,1])\n",
      "problem_HR.addVariable('JaceWed',[0])\n",
      "problem_HR.addVariable('JaceThu',[0,1])\n",
      "problem_HR.addVariable('JaceFri',[0,1])\n",
      "problem_HR.addVariable('EverettMon',[1])\n",
      "problem_HR.addVariable('EverettTue',[0,1])\n",
      "problem_HR.addVariable('EverettWed',[0,1])\n",
      "problem_HR.addVariable('EverettThu',[0,1])\n",
      "problem_HR.addVariable('EverettFri',[0,1])\n",
      "Added 15 variables\n"
     ]
    }
   ],
   "source": [
    "variable_generator(HR_nd, 'problem_HR')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_HR.addVariable('ParkerMon',[0,1])\n",
    "problem_HR.addVariable('ParkerTue',[0,1])\n",
    "problem_HR.addVariable('ParkerWed',[0,1])\n",
    "problem_HR.addVariable('ParkerThu',[0,1])\n",
    "problem_HR.addVariable('ParkerFri',[0,1])\n",
    "problem_HR.addVariable('JaceMon',[0,1])\n",
    "problem_HR.addVariable('JaceTue',[0,1])\n",
    "problem_HR.addVariable('JaceWed',[0,1])\n",
    "problem_HR.addVariable('JaceThu',[0,1])\n",
    "problem_HR.addVariable('JaceFri',[0,1])\n",
    "problem_HR.addVariable('EverettMon',[0,1])\n",
    "problem_HR.addVariable('EverettTue',[0,1])\n",
    "problem_HR.addVariable('EverettWed',[0,1])\n",
    "problem_HR.addVariable('EverettThu',[0,1])\n",
    "problem_HR.addVariable('EverettFri',[0,1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_HR.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
      "(\"ParkerMon\", \"ParkerTue\",\"ParkerWed\",\"ParkerThu\",\"ParkerFri\"))\n",
      "problem_HR.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
      "(\"JaceMon\", \"JaceTue\",\"JaceWed\",\"JaceThu\",\"JaceFri\"))\n",
      "problem_HR.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
      "(\"EverettMon\", \"EverettTue\",\"EverettWed\",\"EverettThu\",\"EverettFri\"))\n"
     ]
    }
   ],
   "source": [
    "constraint_generator(HR_nd, 'problem_HR')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_HR.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"ParkerMon\", \"ParkerTue\",\"ParkerWed\",\"ParkerThu\",\"ParkerFri\"))\n",
    "problem_HR.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
    "(\"JaceMon\", \"JaceTue\",\"JaceWed\",\"JaceThu\",\"JaceFri\"))\n",
    "problem_HR.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
    "(\"EverettMon\", \"EverettTue\",\"EverettWed\",\"EverettThu\",\"EverettFri\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  solution_function 0.04903268814086914\n"
     ]
    }
   ],
   "source": [
    "sol_HR=solution_function(problem_HR)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 208,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(sol_HR)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  consolidated_function_mod 0.6932849884033203\n"
     ]
    }
   ],
   "source": [
    "HR_int_total=consolidated_function_mod(sol_HR)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{0.0, 1.0}"
      ]
     },
     "execution_count": 210,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(HR_int_total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "metadata": {},
   "outputs": [],
   "source": [
    "all_grids_HR=[]\n",
    "for solution in sol_HR:\n",
    "    all_grids_HR.append((grid_populator_big(solution,emp_HR,workingdays=['Mon','Tue','Wed','Thu','Fri'])))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 212,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(all_grids_HR)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Sales**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_Sales=constraint.Problem(BacktrackingSolver())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_Sales.addVariable('VincentMon',[0,1])\n",
      "problem_Sales.addVariable('VincentTue',[0,1])\n",
      "problem_Sales.addVariable('VincentWed',[1])\n",
      "problem_Sales.addVariable('VincentThu',[0,1])\n",
      "problem_Sales.addVariable('VincentFri',[0,1])\n",
      "problem_Sales.addVariable('TimothyMon',[0,1])\n",
      "problem_Sales.addVariable('TimothyTue',[0,1])\n",
      "problem_Sales.addVariable('TimothyWed',[0,1])\n",
      "problem_Sales.addVariable('TimothyThu',[0])\n",
      "problem_Sales.addVariable('TimothyFri',[0,1])\n",
      "problem_Sales.addVariable('LucaMon',[0])\n",
      "problem_Sales.addVariable('LucaTue',[0,1])\n",
      "problem_Sales.addVariable('LucaWed',[0,1])\n",
      "problem_Sales.addVariable('LucaThu',[0,1])\n",
      "problem_Sales.addVariable('LucaFri',[0,1])\n",
      "problem_Sales.addVariable('AbrahamMon',[0])\n",
      "problem_Sales.addVariable('AbrahamTue',[0,1])\n",
      "problem_Sales.addVariable('AbrahamWed',[0,1])\n",
      "problem_Sales.addVariable('AbrahamThu',[0,1])\n",
      "problem_Sales.addVariable('AbrahamFri',[0,1])\n",
      "problem_Sales.addVariable('FinnMon',[0,1])\n",
      "problem_Sales.addVariable('FinnTue',[0,1])\n",
      "problem_Sales.addVariable('FinnWed',[0,1])\n",
      "problem_Sales.addVariable('FinnThu',[0,1])\n",
      "problem_Sales.addVariable('FinnFri',[1])\n",
      "problem_Sales.addVariable('JasperMon',[0,1])\n",
      "problem_Sales.addVariable('JasperTue',[0,1])\n",
      "problem_Sales.addVariable('JasperWed',[0])\n",
      "problem_Sales.addVariable('JasperThu',[0,1])\n",
      "problem_Sales.addVariable('JasperFri',[0,1])\n",
      "Added 30 variables\n"
     ]
    }
   ],
   "source": [
    "variable_generator(Sales_nd,'problem_Sales')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_Sales.addVariable('VincentMon',[0,1])\n",
    "problem_Sales.addVariable('VincentTue',[0,1])\n",
    "problem_Sales.addVariable('VincentWed',[1])\n",
    "problem_Sales.addVariable('VincentThu',[0,1])\n",
    "problem_Sales.addVariable('VincentFri',[0,1])\n",
    "problem_Sales.addVariable('TimothyMon',[0,1])\n",
    "problem_Sales.addVariable('TimothyTue',[0,1])\n",
    "problem_Sales.addVariable('TimothyWed',[0,1])\n",
    "problem_Sales.addVariable('TimothyThu',[0])\n",
    "problem_Sales.addVariable('TimothyFri',[0,1])\n",
    "problem_Sales.addVariable('LucaMon',[0])\n",
    "problem_Sales.addVariable('LucaTue',[0,1])\n",
    "problem_Sales.addVariable('LucaWed',[0,1])\n",
    "problem_Sales.addVariable('LucaThu',[0,1])\n",
    "problem_Sales.addVariable('LucaFri',[0,1])\n",
    "problem_Sales.addVariable('AbrahamMon',[0])\n",
    "problem_Sales.addVariable('AbrahamTue',[0,1])\n",
    "problem_Sales.addVariable('AbrahamWed',[0,1])\n",
    "problem_Sales.addVariable('AbrahamThu',[0,1])\n",
    "problem_Sales.addVariable('AbrahamFri',[0,1])\n",
    "problem_Sales.addVariable('FinnMon',[0,1])\n",
    "problem_Sales.addVariable('FinnTue',[0,1])\n",
    "problem_Sales.addVariable('FinnWed',[0,1])\n",
    "problem_Sales.addVariable('FinnThu',[0,1])\n",
    "problem_Sales.addVariable('FinnFri',[1])\n",
    "problem_Sales.addVariable('JasperMon',[0,1])\n",
    "problem_Sales.addVariable('JasperTue',[0,1])\n",
    "problem_Sales.addVariable('JasperWed',[0])\n",
    "problem_Sales.addVariable('JasperThu',[0,1])\n",
    "problem_Sales.addVariable('JasperFri',[0,1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "problem_Sales.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 5,\n",
      "(\"VincentMon\", \"VincentTue\",\"VincentWed\",\"VincentThu\",\"VincentFri\"))\n",
      "problem_Sales.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
      "(\"TimothyMon\", \"TimothyTue\",\"TimothyWed\",\"TimothyThu\",\"TimothyFri\"))\n",
      "problem_Sales.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
      "(\"LucaMon\", \"LucaTue\",\"LucaWed\",\"LucaThu\",\"LucaFri\"))\n",
      "problem_Sales.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 3,\n",
      "(\"AbrahamMon\", \"AbrahamTue\",\"AbrahamWed\",\"AbrahamThu\",\"AbrahamFri\"))\n",
      "problem_Sales.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
      "(\"FinnMon\", \"FinnTue\",\"FinnWed\",\"FinnThu\",\"FinnFri\"))\n",
      "problem_Sales.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
      "(\"JasperMon\", \"JasperTue\",\"JasperWed\",\"JasperThu\",\"JasperFri\"))\n"
     ]
    }
   ],
   "source": [
    "constraint_generator(Sales_nd,'problem_Sales')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {},
   "outputs": [],
   "source": [
    "problem_Sales.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 5,\n",
    "(\"VincentMon\", \"VincentTue\",\"VincentWed\",\"VincentThu\",\"VincentFri\"))\n",
    "problem_Sales.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
    "(\"TimothyMon\", \"TimothyTue\",\"TimothyWed\",\"TimothyThu\",\"TimothyFri\"))\n",
    "problem_Sales.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 1,\n",
    "(\"LucaMon\", \"LucaTue\",\"LucaWed\",\"LucaThu\",\"LucaFri\"))\n",
    "problem_Sales.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"AbrahamMon\", \"AbrahamTue\",\"AbrahamWed\",\"AbrahamThu\",\"AbrahamFri\"))\n",
    "problem_Sales.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 2,\n",
    "(\"FinnMon\", \"FinnTue\",\"FinnWed\",\"FinnThu\",\"FinnFri\"))\n",
    "problem_Sales.addConstraint(lambda p, q, r, s, t: p+q+r+s+t == 0,\n",
    "(\"JasperMon\", \"JasperTue\",\"JasperWed\",\"JasperThu\",\"JasperFri\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  solution_function 0.053705453872680664\n"
     ]
    }
   ],
   "source": [
    "sol_Sales=solution_function(problem_Sales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "96"
      ]
     },
     "execution_count": 221,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(sol_Sales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  consolidated_function_mod 4.401006460189819\n"
     ]
    }
   ],
   "source": [
    "Sales_int_total=consolidated_function_mod(sol_Sales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 223,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{3.0, 4.0, 5.0, 6.0}"
      ]
     },
     "execution_count": 223,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(Sales_int_total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "metadata": {},
   "outputs": [],
   "source": [
    "good_index_Sales=min_indices(Sales_int_total, min(Sales_int_total))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
   "metadata": {},
   "outputs": [],
   "source": [
    "bad_index_Sales=min_indices(Sales_int_total, max(Sales_int_total))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 226,
   "metadata": {},
   "outputs": [],
   "source": [
    "Sales_bad_solns=[sol_Sales[i] for i in bad_index_Sales]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "metadata": {},
   "outputs": [],
   "source": [
    "Sales_best_solns=[sol_Sales[i] for i in good_index_Sales]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 228,
   "metadata": {},
   "outputs": [],
   "source": [
    "all_grids_Sales=[]\n",
    "for solution in sol_Sales:\n",
    "    all_grids_Sales.append((grid_populator_big(solution,emp_Sales,workingdays=['Mon','Tue','Wed','Thu','Fri'])))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 229,
   "metadata": {},
   "outputs": [],
   "source": [
    "bad_grids_Sales=[]\n",
    "for solution in Sales_bad_solns:\n",
    "    bad_grids_Sales.append(grid_populator_big(solution,emp_Sales,workingdays=['Mon','Tue','Wed','Thu','Fri']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 230,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_grids_Sales=[]\n",
    "for solution in Sales_best_solns:\n",
    "    best_grids_Sales.append(grid_populator_big(solution,emp_Sales,workingdays=['Mon','Tue','Wed','Thu','Fri']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 231,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[         Mon  Tue  Wed  Thu  Fri\n",
       " Vincent  1.0  1.0  1.0  1.0  1.0\n",
       " Timothy  0.0  1.0  1.0  0.0  0.0\n",
       " Luca     0.0  0.0  0.0  1.0  0.0\n",
       " Abraham  0.0  0.0  0.0  0.0  0.0\n",
       " Finn     1.0  0.0  0.0  0.0  1.0\n",
       " Jasper   0.0  0.0  0.0  0.0  0.0,          Mon  Tue  Wed  Thu  Fri\n",
       " Vincent  1.0  1.0  1.0  1.0  1.0\n",
       " Timothy  1.0  0.0  1.0  0.0  0.0\n",
       " Luca     0.0  1.0  0.0  0.0  0.0\n",
       " Abraham  0.0  0.0  0.0  0.0  0.0\n",
       " Finn     0.0  0.0  0.0  1.0  1.0\n",
       " Jasper   0.0  0.0  0.0  0.0  0.0,          Mon  Tue  Wed  Thu  Fri\n",
       " Vincent  1.0  1.0  1.0  1.0  1.0\n",
       " Timothy  1.0  1.0  0.0  0.0  0.0\n",
       " Luca     0.0  0.0  1.0  0.0  0.0\n",
       " Abraham  0.0  0.0  0.0  0.0  0.0\n",
       " Finn     0.0  0.0  0.0  1.0  1.0\n",
       " Jasper   0.0  0.0  0.0  0.0  0.0,          Mon  Tue  Wed  Thu  Fri\n",
       " Vincent  1.0  1.0  1.0  1.0  1.0\n",
       " Timothy  1.0  0.0  1.0  0.0  0.0\n",
       " Luca     0.0  0.0  0.0  1.0  0.0\n",
       " Abraham  0.0  0.0  0.0  0.0  0.0\n",
       " Finn     0.0  1.0  0.0  0.0  1.0\n",
       " Jasper   0.0  0.0  0.0  0.0  0.0,          Mon  Tue  Wed  Thu  Fri\n",
       " Vincent  1.0  1.0  1.0  1.0  1.0\n",
       " Timothy  1.0  1.0  0.0  0.0  0.0\n",
       " Luca     0.0  0.0  0.0  1.0  0.0\n",
       " Abraham  0.0  0.0  0.0  0.0  0.0\n",
       " Finn     0.0  0.0  1.0  0.0  1.0\n",
       " Jasper   0.0  0.0  0.0  0.0  0.0]"
      ]
     },
     "execution_count": 231,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "best_grids_Sales"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Grid Evaluator**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "metadata": {},
   "outputs": [],
   "source": [
    "g1=grid_populator_big(Sales_best_solns[0],emp_Sales,workingdays=['Mon','Tue','Wed','Thu','Fri'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 233,
   "metadata": {},
   "outputs": [],
   "source": [
    "def grid_eval(grid):\n",
    "    employeelist=list(grid.index)\n",
    "    days_list=days_series_creator(grid, employeelist, workingdays=['Mon','Tue','Wed','Thu','Fri'])\n",
    "    ml=master_list(days_list)\n",
    "    EvsE,Interaction_score=populator_fn(ml, employeelist)\n",
    "    return Interaction_score\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 234,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.0"
      ]
     },
     "execution_count": 234,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grid_eval(g1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 236,
   "metadata": {},
   "outputs": [],
   "source": [
    "# grid_eval(grid_populator_big(sol_Sales[205],emp_Sales,workingdays=['Mon','Tue','Wed','Thu','Fri']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Grid Concatenation**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 237,
   "metadata": {},
   "outputs": [],
   "source": [
    "def merge_solutions(grid1, grid2):\n",
    "    return pd.concat([grid1, grid2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 238,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "19.0"
      ]
     },
     "execution_count": 238,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grid_eval(merge_solutions(best_grids_Sales[2], best_grids_SCM[4]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 239,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mon</th>\n",
       "      <th>Tue</th>\n",
       "      <th>Wed</th>\n",
       "      <th>Thu</th>\n",
       "      <th>Fri</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Vincent</th>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Timothy</th>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Luca</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Abraham</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Finn</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jasper</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Mon  Tue  Wed  Thu  Fri\n",
       "Vincent  1.0  1.0  1.0  1.0  1.0\n",
       "Timothy  0.0  1.0  1.0  0.0  0.0\n",
       "Luca     0.0  0.0  0.0  1.0  0.0\n",
       "Abraham  0.0  0.0  0.0  0.0  0.0\n",
       "Finn     1.0  0.0  0.0  0.0  1.0\n",
       "Jasper   0.0  0.0  0.0  0.0  0.0"
      ]
     },
     "execution_count": 239,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "best_grids_Sales[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 240,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mon</th>\n",
       "      <th>Tue</th>\n",
       "      <th>Wed</th>\n",
       "      <th>Thu</th>\n",
       "      <th>Fri</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Jax</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Barrett</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Maximus</th>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Brandon</th>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Brantley</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Alejandro</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Grant</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Mon  Tue  Wed  Thu  Fri\n",
       "Jax        0.0  0.0  1.0  0.0  0.0\n",
       "Barrett    1.0  0.0  0.0  0.0  0.0\n",
       "Maximus    0.0  1.0  0.0  1.0  1.0\n",
       "Brandon    0.0  1.0  0.0  1.0  1.0\n",
       "Brantley   1.0  0.0  1.0  0.0  0.0\n",
       "Alejandro  0.0  0.0  0.0  0.0  0.0\n",
       "Grant      0.0  0.0  0.0  0.0  0.0"
      ]
     },
     "execution_count": 240,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "best_grids_SCM[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 241,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "28.0"
      ]
     },
     "execution_count": 241,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grid_eval(merge_solutions(bad_grids_Sales[2], bad_grids_SCM[1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 242,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "21.0\n",
      "18.0\n",
      "19.0\n",
      "18.0\n",
      "19.0\n",
      "18.0\n",
      "21.0\n",
      "21.0\n",
      "19.0\n",
      "19.0\n",
      "19.0\n",
      "19.0\n",
      "18.0\n",
      "19.0\n",
      "19.0\n",
      "18.0\n",
      "19.0\n",
      "19.0\n",
      "21.0\n",
      "21.0\n",
      "21.0\n",
      "19.0\n",
      "18.0\n",
      "21.0\n",
      "21.0\n"
     ]
    }
   ],
   "source": [
    "for i in best_grids_Sales:\n",
    "    for j in best_grids_SCM:\n",
    "        p=grid_eval(merge_solutions(i,j))\n",
    "        print (p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "metadata": {},
   "outputs": [],
   "source": [
    "dl=[]\n",
    "for i in bad_grids_Sales:\n",
    "    for j in bad_grids_SCM:\n",
    "        \n",
    "        q=grid_eval(merge_solutions(i,j))\n",
    "    dl.append(q)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27.0"
      ]
     },
     "execution_count": 244,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max(dl)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "metadata": {},
   "outputs": [],
   "source": [
    "@calculate_time\n",
    "def concat_and_evaluate(list_of_grids_1, list_of_grids_2):\n",
    "    sol_list=[]\n",
    "    score_list=[]\n",
    "    for i in list_of_grids_1:\n",
    "        for j in list_of_grids_2:\n",
    "            p=merge_solutions(i,j)\n",
    "            q=grid_eval(p)\n",
    "            sol_list.append(p)\n",
    "            score_list.append(q)\n",
    "    return sol_list, score_list"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**COMBINING Sales and SCM**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 246,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 0.14209389686584473\n"
     ]
    }
   ],
   "source": [
    "best_solns, best_scores=concat_and_evaluate(best_grids_Sales,best_grids_SCM)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 247,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{18.0, 19.0, 21.0}"
      ]
     },
     "execution_count": 247,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(best_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 248,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 0.8647551536560059\n"
     ]
    }
   ],
   "source": [
    "worst_solns, worst_scores=concat_and_evaluate(bad_grids_Sales, bad_grids_SCM)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 249,
   "metadata": {},
   "outputs": [],
   "source": [
    "worst_index=[]\n",
    "for i in range (0,len(worst_scores)):\n",
    "    if worst_scores[i]==53:\n",
    "        worst_index.append(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 250,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mon</th>\n",
       "      <th>Tue</th>\n",
       "      <th>Wed</th>\n",
       "      <th>Thu</th>\n",
       "      <th>Fri</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Vincent</th>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Timothy</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Luca</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Abraham</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Finn</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jasper</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jax</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Barrett</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Maximus</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Brandon</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Brantley</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Alejandro</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Grant</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Mon  Tue  Wed  Thu  Fri\n",
       "Vincent    1.0  1.0  1.0  1.0  1.0\n",
       "Timothy    1.0  0.0  0.0  0.0  1.0\n",
       "Luca       0.0  0.0  0.0  0.0  1.0\n",
       "Abraham    0.0  0.0  0.0  0.0  0.0\n",
       "Finn       1.0  0.0  0.0  0.0  1.0\n",
       "Jasper     0.0  0.0  0.0  0.0  0.0\n",
       "Jax        0.0  0.0  1.0  0.0  0.0\n",
       "Barrett    1.0  0.0  0.0  0.0  0.0\n",
       "Maximus    1.0  0.0  0.0  1.0  1.0\n",
       "Brandon    1.0  0.0  0.0  1.0  1.0\n",
       "Brantley   1.0  0.0  1.0  0.0  0.0\n",
       "Alejandro  0.0  0.0  0.0  0.0  0.0\n",
       "Grant      0.0  0.0  0.0  0.0  0.0"
      ]
     },
     "execution_count": 250,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "worst_solns[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 251,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 251,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "worst_index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 252,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0}"
      ]
     },
     "execution_count": 252,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(worst_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 253,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 253,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(list_index_returner(worst_scores, 55))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**concat1=Sales+SCM**\n",
    "\n",
    "**Concat2=concat1+IT**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 269,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_concat1=[best_solns[i] for i in list_index_returner(best_scores, min(best_scores))]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "metadata": {},
   "outputs": [],
   "source": [
    "worst_concat1=[worst_solns[i] for i in list_index_returner(worst_scores, max(worst_scores))]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 271,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 0.05603766441345215\n"
     ]
    }
   ],
   "source": [
    "c2_sol_list, c2_score_list=concat_and_evaluate(best_concat1,best_grids_IT)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 272,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 1.0096697807312012\n"
     ]
    }
   ],
   "source": [
    "c2_w_sol_list, c2_w_score_list=concat_and_evaluate(worst_concat1, bad_grids_IT)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 273,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                 Mon  Tue  Wed  Thu  Fri\n",
       " Tara Cantrock    0.0  0.0  0.0  0.0  0.0\n",
       " Joshua           0.0  1.0  1.0  0.0  1.0\n",
       " Caleb            1.0  0.0  0.0  0.0  0.0\n",
       " Ryan             0.0  0.0  0.0  0.0  0.0\n",
       " Tanzeer Cao      0.0  0.0  0.0  1.0  0.0\n",
       " Ted Brown        0.0  1.0  1.0  0.0  1.0\n",
       " Tae Carrillo     0.0  1.0  1.0  0.0  1.0\n",
       " Thanadtha Brown  1.0  0.0  0.0  1.0  0.0]"
      ]
     },
     "execution_count": 273,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "best_grids_IT"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 274,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{68.0,\n",
       " 69.0,\n",
       " 70.0,\n",
       " 71.0,\n",
       " 72.0,\n",
       " 73.0,\n",
       " 74.0,\n",
       " 75.0,\n",
       " 76.0,\n",
       " 77.0,\n",
       " 78.0,\n",
       " 79.0,\n",
       " 80.0,\n",
       " 81.0}"
      ]
     },
     "execution_count": 274,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(c2_w_score_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 275,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{59.0, 62.0}"
      ]
     },
     "execution_count": 275,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(c2_score_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 276,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 276,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list_index_returner(c2_w_score_list,114)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 277,
   "metadata": {},
   "outputs": [],
   "source": [
    "BESTC2= [c2_sol_list[i] for i in list_index_returner(c2_score_list,85)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 278,
   "metadata": {},
   "outputs": [],
   "source": [
    "WORSTC2=[c2_w_sol_list[i] for i in list_index_returner(c2_w_score_list,114)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 279,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-279-ffa763b4a689>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdf3\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mBESTC2\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "df3=BESTC2[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "grid_eval(BESTC2[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df4=WORSTC2[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "grid_eval(WORSTC2[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# df1.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\Good_sol_1.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# df2.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\Bad_sol_1.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# df3.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\Good_sol_2.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# df4.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\Bad_sol_2.csv', index = True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**HYPOTHESIS TESTING**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_grids_SCM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "hyp_grids, hyp_scores=concat_and_evaluate(best_grids_SCM, all_grids_Sales)\n",
    "\n",
    "set(hyp_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**PROPER CONCATENATION**\n",
    "\n",
    "Core: SCM\n",
    "\n",
    "layer1=Sales,\n",
    "layer2=IT,\n",
    "layer3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 280,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 2.3749794960021973\n"
     ]
    }
   ],
   "source": [
    "#Best SCM grids are to be combined with all Sales Grids\n",
    "core_and_l1_grids, core_and_l1_int_scores=concat_and_evaluate(best_grids_SCM, all_grids_Sales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 281,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "480"
      ]
     },
     "execution_count": 281,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(core_and_l1_int_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 282,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0}"
      ]
     },
     "execution_count": 282,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(core_and_l1_int_scores)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#Number of solutions obtained in core+layer_1: 480\n",
    "#Range of Interaction scores: 18 to 25\n",
    "\n",
    "**CREATING BEST AND WORST GRIDS FROM C+L1**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 283,
   "metadata": {},
   "outputs": [],
   "source": [
    "min_indices_Cl1=list_index_returner(core_and_l1_int_scores, min(core_and_l1_int_scores))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 284,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_Cl1_grids=[core_and_l1_grids[i] for i in min_indices_Cl1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 285,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20.0"
      ]
     },
     "execution_count": 285,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grid_eval(core_and_l1_grids[334])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 286,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "17"
      ]
     },
     "execution_count": 286,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(best_Cl1_grids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 287,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Best C+L1 grid socre: 39, count= 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 288,
   "metadata": {},
   "outputs": [],
   "source": [
    "max_indices_Cl1=list_index_returner(core_and_l1_int_scores, max(core_and_l1_int_scores))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 289,
   "metadata": {},
   "outputs": [],
   "source": [
    "worst_Cl1_grids=[core_and_l1_grids[i] for i in max_indices_Cl1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 290,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 290,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(worst_Cl1_grids)\n",
    "#Worst C+L1 grid score: 53, count=7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**L2=C+L1+IT**\n",
    "Best grids from C+L1 to be combined with all IT Grids\n",
    "Worst C+l1 grids to be combined with bad IT Grids\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 291,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3456"
      ]
     },
     "execution_count": 291,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(all_grids_IT)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 292,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 419.38829255104065\n"
     ]
    }
   ],
   "source": [
    "#Since there are 2880 solns, we pick only 5 best solutions from the core (out of 10)\n",
    "cl1_and_l2_grids, cl1_and_l2_int_scores=concat_and_evaluate(best_Cl1_grids, all_grids_IT)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 293,
   "metadata": {},
   "outputs": [],
   "source": [
    "min_indices_Cl1_and_l2=list_index_returner(cl1_and_l2_int_scores, min(cl1_and_l2_int_scores))\n",
    "max_indices_Cl1_and_l2=list_index_returner(cl1_and_l2_int_scores, max(cl1_and_l2_int_scores))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 294,
   "metadata": {},
   "outputs": [],
   "source": [
    "# set(cl1_and_l2_int_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 295,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Cl1+l2 interaction scores range: 83 to 99"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 296,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "58752"
      ]
     },
     "execution_count": 296,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(cl1_and_l2_grids)\n",
    "#Total no of grids in cl1+l2: 28800\n",
    "#No of grids with least inteaction (83): 36\n",
    "#No of grids with most interaction (99):2 (enough)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 298,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_cl1_and_l2_grids=[cl1_and_l2_grids[i] for i in min_indices_Cl1_and_l2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**WORST GRIDS**\n",
    "\n",
    "**Concatenate IT bad solutions with Formation so far (Fsf's) worst solutions** "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 299,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 1.1177432537078857\n"
     ]
    }
   ],
   "source": [
    "worst_c1_and_2_grids, worst_c1_and_2_int_scores= concat_and_evaluate(bad_grids_IT,worst_Cl1_grids )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 300,
   "metadata": {},
   "outputs": [],
   "source": [
    "worst_of_worst_1_index=list_index_returner(worst_c1_and_2_int_scores, max(worst_c1_and_2_int_scores))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 301,
   "metadata": {},
   "outputs": [],
   "source": [
    "#This is the list that is to be concatenated with bad grids of next team (FMGM)\n",
    "#Maximum interaction so far is 117\n",
    "worst_of_worst_1_grids=[worst_c1_and_2_grids[i] for i in worst_of_worst_1_index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 302,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 302,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(worst_of_worst_1_grids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**L3=CL1L2+Inv**\n",
    "\n",
    "Best CL1L2 solutions with all solutions of Inv\n",
    "\n",
    "Worst CL1L2 solutions with bad solutions of Inv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 303,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 61.50033140182495\n"
     ]
    }
   ],
   "source": [
    "c2_3_grids, c2_3_int_scores=concat_and_evaluate(best_cl1_and_l2_grids, all_grids_Inv)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 304,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5760"
      ]
     },
     "execution_count": 304,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(c2_3_grids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 305,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{128.0,\n",
       " 129.0,\n",
       " 130.0,\n",
       " 131.0,\n",
       " 132.0,\n",
       " 133.0,\n",
       " 134.0,\n",
       " 135.0,\n",
       " 136.0,\n",
       " 137.0,\n",
       " 138.0,\n",
       " 139.0,\n",
       " 140.0,\n",
       " 141.0,\n",
       " 142.0,\n",
       " 143.0,\n",
       " 144.0,\n",
       " 145.0,\n",
       " 146.0}"
      ]
     },
     "execution_count": 305,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(c2_3_int_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 306,
   "metadata": {},
   "outputs": [],
   "source": [
    "##Core plus 3 layers so far:\n",
    "#Interaction score ranges: 128 to 146\n",
    "good_indices_c2_3=list_index_returner(c2_3_int_scores, min (c2_3_int_scores))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 307,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "bad_indices_c2_3=list_index_returner(c2_3_int_scores, max (c2_3_int_scores))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 308,
   "metadata": {},
   "outputs": [],
   "source": [
    "c2_3_good_grids=[c2_3_grids[i] for i in good_indices_c2_3]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#TO be combined with fsf's worst\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 309,
   "metadata": {},
   "outputs": [],
   "source": [
    "c2_3_bad_grids=[c2_3_grids[i] for i in bad_indices_c2_3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 310,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "48"
      ]
     },
     "execution_count": 310,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(c2_3_bad_grids)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**CONCATENATING c23 with FMGM to form c3_4**\n",
    "\n",
    "Best CL2L3 solutions with all solutions of FMGM\n",
    "\n",
    "Worst CL2L3 solutions with bad solutions of FMGM"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Best solution**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 311,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 19.72508430480957\n"
     ]
    }
   ],
   "source": [
    "c3_4_grids, c3_4_interaction_scores=concat_and_evaluate(c2_3_good_grids, all_grids_fmgm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 313,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1440"
      ]
     },
     "execution_count": 313,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(c3_4_grids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 312,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{188.0,\n",
       " 189.0,\n",
       " 190.0,\n",
       " 191.0,\n",
       " 192.0,\n",
       " 193.0,\n",
       " 194.0,\n",
       " 195.0,\n",
       " 196.0,\n",
       " 197.0,\n",
       " 198.0,\n",
       " 199.0,\n",
       " 200.0,\n",
       " 201.0,\n",
       " 202.0,\n",
       " 203.0,\n",
       " 204.0,\n",
       " 205.0,\n",
       " 206.0,\n",
       " 207.0,\n",
       " 208.0}"
      ]
     },
     "execution_count": 312,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(c3_4_interaction_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 314,
   "metadata": {},
   "outputs": [],
   "source": [
    "#1440 solutions are evaluated:\n",
    "# Best interaction score: 188\n",
    "\n",
    "#Best grids are to be combined with all grids of next department (operations)\n",
    "\n",
    "good_index_c3_4=list_index_returner(c3_4_interaction_scores, min(c3_4_interaction_scores))\n",
    "c3_4_good_grids=[c3_4_grids[i] for i in good_index_c3_4]\n",
    "\n",
    "# len(c3_4_good_grids)\n",
    "\n",
    "#The above 18 solns are to be combined with all solutions of operations"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Bad Solutions**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 315,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 9.062011241912842\n"
     ]
    }
   ],
   "source": [
    "c2_3_bad_grids, c2_3_int_scores_bad=concat_and_evaluate(bad_grids_Inv,worst_of_worst_1_grids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 316,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{153.0,\n",
       " 154.0,\n",
       " 155.0,\n",
       " 156.0,\n",
       " 157.0,\n",
       " 158.0,\n",
       " 159.0,\n",
       " 160.0,\n",
       " 161.0,\n",
       " 162.0,\n",
       " 163.0,\n",
       " 164.0,\n",
       " 165.0,\n",
       " 166.0,\n",
       " 167.0,\n",
       " 168.0,\n",
       " 169.0,\n",
       " 170.0}"
      ]
     },
     "execution_count": 316,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(c2_3_int_scores_bad)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 317,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Following to be combined with bad FMGM\n",
    "bad_indices_bad_c2_3=list_index_returner(c2_3_int_scores_bad, max(c2_3_int_scores_bad))\n",
    "\n",
    "worst_grids_c2_3=[c2_3_bad_grids[i] for i in bad_indices_bad_c2_3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 318,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "712"
      ]
     },
     "execution_count": 318,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(bad_grids_fmgm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 319,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 2.757827043533325\n"
     ]
    }
   ],
   "source": [
    "c3_4_bad_grids, c3_4_bad_int_scores=concat_and_evaluate(worst_grids_c2_3, bad_grids_fmgm[0:50])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 320,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "36"
      ]
     },
     "execution_count": 320,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(c3_4_bad_grids[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 323,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1440"
      ]
     },
     "execution_count": 323,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(c3_4_grids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 322,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{239.0, 240.0, 241.0, 242.0, 243.0, 244.0, 245.0, 246.0, 247.0, 248.0, 249.0}"
      ]
     },
     "execution_count": 322,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(c3_4_bad_int_scores)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Now, we have added 4 layers to the core, i.e.**\n",
    "\n",
    "**SCM+Sales+IT+Inv+FMGM have been optimized**\n",
    "\n",
    "Total employees optimised: 36\n",
    "\n",
    "Best interaction score so far: 188\n",
    "\n",
    "Worst interaction score so far: 249"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**5th layer Best Solutions**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 324,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 16.47292971611023\n"
     ]
    }
   ],
   "source": [
    "c4_5_grids, c4_5_int_scores=concat_and_evaluate(c3_4_good_grids[0:10], all_grids_OP)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 325,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{251.0,\n",
       " 254.0,\n",
       " 255.0,\n",
       " 256.0,\n",
       " 257.0,\n",
       " 258.0,\n",
       " 259.0,\n",
       " 260.0,\n",
       " 261.0,\n",
       " 262.0,\n",
       " 263.0,\n",
       " 264.0,\n",
       " 265.0,\n",
       " 266.0,\n",
       " 267.0,\n",
       " 268.0,\n",
       " 269.0,\n",
       " 270.0,\n",
       " 271.0,\n",
       " 272.0,\n",
       " 273.0}"
      ]
     },
     "execution_count": 325,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(c4_5_int_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 326,
   "metadata": {},
   "outputs": [],
   "source": [
    "good_index_c4_5=list_index_returner(c4_5_int_scores, min(c4_5_int_scores))\n",
    "c4_5_good_grids=[c4_5_grids[i] for i in good_index_c4_5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 332,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "251.0"
      ]
     },
     "execution_count": 332,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "min(c4_5_int_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 327,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 327,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(c4_5_good_grids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 328,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "251.0"
      ]
     },
     "execution_count": 328,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grid_eval(c4_5_good_grids[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#This above grid is to be combined with all grids of "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.DEPARTMENT.value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**BAD Solution**\n",
    "\n",
    "Adding bad_OP solns to worst_solution so far (c3_4_bad_grids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 329,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "200"
      ]
     },
     "execution_count": 329,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(c3_4_bad_grids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 330,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 50.312374114990234\n"
     ]
    }
   ],
   "source": [
    "c4_5_grids_bad, c4_5_index_bad=concat_and_evaluate(bad_grids_OP, c3_4_bad_grids[0:20])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 331,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{320.0,\n",
       " 321.0,\n",
       " 322.0,\n",
       " 323.0,\n",
       " 324.0,\n",
       " 325.0,\n",
       " 326.0,\n",
       " 327.0,\n",
       " 328.0,\n",
       " 329.0,\n",
       " 330.0,\n",
       " 331.0,\n",
       " 332.0,\n",
       " 333.0,\n",
       " 334.0,\n",
       " 335.0,\n",
       " 336.0,\n",
       " 337.0,\n",
       " 338.0,\n",
       " 339.0,\n",
       " 340.0,\n",
       " 341.0,\n",
       " 343.0}"
      ]
     },
     "execution_count": 331,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(c4_5_index_bad)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 333,
   "metadata": {},
   "outputs": [],
   "source": [
    "##As of this level the trade-off between good vs bad interactions is 251-343 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 334,
   "metadata": {},
   "outputs": [],
   "source": [
    "c4_5_worst_index=list_index_returner(c4_5_index_bad, max(c4_5_index_bad))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 335,
   "metadata": {},
   "outputs": [],
   "source": [
    "c4_5_worst_grids=[c4_5_grids_bad[i] for i in c4_5_worst_index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Concat Proc to make c5_6**\n",
    "\n",
    "Since Proc has only 250 solutions and all are of the same interaction score of 3, we use all proc grids with both best and worst c4_5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 336,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 52.94664263725281\n"
     ]
    }
   ],
   "source": [
    "c5_6_grids, c5_6_int_scores=concat_and_evaluate(c4_5_good_grids, all_grids_Proc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 337,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{322.0,\n",
       " 323.0,\n",
       " 324.0,\n",
       " 325.0,\n",
       " 326.0,\n",
       " 327.0,\n",
       " 328.0,\n",
       " 329.0,\n",
       " 330.0,\n",
       " 331.0,\n",
       " 332.0,\n",
       " 333.0,\n",
       " 334.0,\n",
       " 335.0,\n",
       " 336.0,\n",
       " 337.0,\n",
       " 338.0,\n",
       " 339.0,\n",
       " 340.0,\n",
       " 341.0,\n",
       " 342.0,\n",
       " 343.0,\n",
       " 344.0,\n",
       " 345.0,\n",
       " 346.0,\n",
       " 347.0,\n",
       " 348.0,\n",
       " 349.0,\n",
       " 350.0,\n",
       " 351.0,\n",
       " 352.0,\n",
       " 353.0,\n",
       " 354.0,\n",
       " 355.0,\n",
       " 356.0,\n",
       " 357.0}"
      ]
     },
     "execution_count": 337,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(c5_6_int_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 338,
   "metadata": {},
   "outputs": [],
   "source": [
    "good_c5_6_index=list_index_returner(c5_6_int_scores, min(c5_6_int_scores))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 339,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_c5_6_grids=[c5_6_grids[i] for i in good_c5_6_index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 340,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 340,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(best_c5_6_grids)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**WORST SOLUTION**\n",
    "\n",
    "Concat worst c4_5 with all proc grids"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 341,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 54.54618525505066\n"
     ]
    }
   ],
   "source": [
    "c5_6_bad_grids, c5_6_int_score_bad=concat_and_evaluate(c4_5_worst_grids, all_grids_Proc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 342,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{414.0,\n",
       " 415.0,\n",
       " 416.0,\n",
       " 417.0,\n",
       " 418.0,\n",
       " 419.0,\n",
       " 420.0,\n",
       " 421.0,\n",
       " 422.0,\n",
       " 423.0,\n",
       " 424.0,\n",
       " 425.0,\n",
       " 426.0,\n",
       " 427.0,\n",
       " 428.0,\n",
       " 429.0,\n",
       " 430.0,\n",
       " 431.0,\n",
       " 432.0,\n",
       " 433.0,\n",
       " 434.0,\n",
       " 435.0,\n",
       " 436.0,\n",
       " 437.0,\n",
       " 438.0,\n",
       " 439.0,\n",
       " 440.0,\n",
       " 441.0,\n",
       " 442.0,\n",
       " 443.0,\n",
       " 444.0,\n",
       " 445.0,\n",
       " 446.0,\n",
       " 447.0,\n",
       " 448.0,\n",
       " 449.0,\n",
       " 450.0,\n",
       " 451.0,\n",
       " 452.0,\n",
       " 453.0,\n",
       " 454.0,\n",
       " 455.0}"
      ]
     },
     "execution_count": 342,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(c5_6_int_score_bad)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 343,
   "metadata": {},
   "outputs": [],
   "source": [
    "worst_c5_6_index=list_index_returner(c5_6_int_score_bad, max(c5_6_int_score_bad))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 344,
   "metadata": {},
   "outputs": [],
   "source": [
    "worst_c5_6_grids=[c5_6_bad_grids[i] for i in worst_c5_6_index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 345,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 345,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(worst_c5_6_grids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 346,
   "metadata": {},
   "outputs": [],
   "source": [
    "#So far, the tally between best and worst solution interactions is 322 vs 455"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Adding the final layer: HR  c6_7**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 347,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 2.4246060848236084\n"
     ]
    }
   ],
   "source": [
    "c6_7_grids, c6_7_int_scores=concat_and_evaluate(best_c5_6_grids, all_grids_HR)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 348,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{354.0,\n",
       " 355.0,\n",
       " 356.0,\n",
       " 357.0,\n",
       " 359.0,\n",
       " 360.0,\n",
       " 361.0,\n",
       " 362.0,\n",
       " 363.0,\n",
       " 364.0,\n",
       " 365.0,\n",
       " 366.0,\n",
       " 367.0,\n",
       " 369.0,\n",
       " 370.0,\n",
       " 372.0,\n",
       " 373.0,\n",
       " 374.0,\n",
       " 375.0}"
      ]
     },
     "execution_count": 348,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(c6_7_int_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 349,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_solution_overall_index=list_index_returner(c6_7_int_scores, min(c6_7_int_scores))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 350,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_overall_grids=[c6_7_grids[i] for i in best_solution_overall_index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 359,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 359,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(best_overall_grids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 353,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Wow! Poetic!!\n",
    "\n",
    "#the overall optimized minimum interaction score is 354"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 362,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 362,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(best_overall_grids[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Last Worst Solution**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 354,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total time taken in :  concat_and_evaluate 2.608731269836426\n"
     ]
    }
   ],
   "source": [
    "c6_7_bad_grids, c6_7_bad_int_scores=concat_and_evaluate(worst_c5_6_grids, all_grids_HR)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 355,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{486.0,\n",
       " 487.0,\n",
       " 489.0,\n",
       " 490.0,\n",
       " 491.0,\n",
       " 492.0,\n",
       " 493.0,\n",
       " 494.0,\n",
       " 495.0,\n",
       " 496.0,\n",
       " 497.0,\n",
       " 498.0,\n",
       " 499.0,\n",
       " 500.0,\n",
       " 501.0,\n",
       " 502.0,\n",
       " 504.0,\n",
       " 505.0,\n",
       " 506.0,\n",
       " 507.0,\n",
       " 508.0,\n",
       " 509.0,\n",
       " 510.0,\n",
       " 512.0,\n",
       " 514.0}"
      ]
     },
     "execution_count": 355,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(c6_7_bad_int_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 356,
   "metadata": {},
   "outputs": [],
   "source": [
    "worst_overall_index=list_index_returner(c6_7_bad_int_scores, max(c6_7_bad_int_scores))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 357,
   "metadata": {},
   "outputs": [],
   "source": [
    "worst_overall_grids=[c6_7_bad_grids[i] for i in worst_overall_index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 358,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 358,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(worst_overall_grids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 374,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "514.0"
      ]
     },
     "execution_count": 374,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grid_eval(worst_overall_grids[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Random Exploration**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(df['Emp Names'][df['At Office/Week']==0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(df['Emp Names'][df['At Office/Week']!=0])\n",
    "#No of employees who come to office at least once. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "38*37/2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "38*37/2\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#38C2 can be the total number of interactions, which is 703. We have brought it down to 490. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print ('Risk is reduced by {} %'.format (100-(490/7.03)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfa= best_overall_grids[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfa.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\Overall_best_sol_490.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfb= worst_overall_grids[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfb.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\Overall_best_sol_654.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "grid_eval(dfa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "grid_eval(dfb)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Primary_and_Secondary_contacts**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 363,
   "metadata": {},
   "outputs": [],
   "source": [
    "def primary_contact_employeewise(EvsE_grid, Employee_name):\n",
    "    S1=pd.Series(EvsE_grid[Employee_name])\n",
    "    primary_contact_list=[]\n",
    "    for index, value in S1.items():\n",
    "        if value==1.0:\n",
    "            primary_contact_list.append(index)\n",
    "    return primary_contact_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 364,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'grid1' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-364-38324e965f7a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdays_as_series\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdays_series_creator\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mgrid1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0memployeeslist\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mworkingdays\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mml\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mmaster_list\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdays_as_series\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mEvsE_grid\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mgrid_int_score\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpopulator_fn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mml\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0memployeeslist\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'grid1' is not defined"
     ]
    }
   ],
   "source": [
    "days_as_series=days_series_creator(grid1, employeeslist, workingdays)\n",
    "ml=master_list(days_as_series)\n",
    "EvsE_grid, grid_int_score = populator_fn(ml, employeeslist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 365,
   "metadata": {},
   "outputs": [],
   "source": [
    "def primary_contact(grid):\n",
    "    primary_contact_dict={}\n",
    "    employeeslist=grid.index\n",
    "    days_as_series=days_series_creator(grid, employeeslist, workingdays=['Mon','Tue','Wed','Thu','Fri'])\n",
    "    ml=master_list(days_as_series)\n",
    "    EvsE_grid, grid_int_score = populator_fn(ml, employeeslist)\n",
    "    for i in employeeslist:\n",
    "        \n",
    "        primary_contact_dict[i]=primary_contact_employeewise(EvsE_grid, i)\n",
    "    return primary_contact_dict\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_soln_primary_contact_dict=primary_contact(dfa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "worst_soln_primary_contact_dict=primary_contact(dfb)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_soln_primary_contact_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(best_soln_primary_contact_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "primary_contacts=pd.Series([])\n",
    "for i in dfa.index:\n",
    "    primary_contacts.append(pd.Series(best_soln_primary_contact_dict[i], index=str(i)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "primary_contact_for_best_solution=pd.Series(best_soln_primary_contact_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "S1=primary_contact_for_best_solution"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**SECONDARY CONTACTS**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 366,
   "metadata": {},
   "outputs": [],
   "source": [
    "def secondary_contact_employeewise(EvsE_grid, Employee_name):\n",
    "    primary_list=primary_contact_employeewise(EvsE_grid, Employee_name)\n",
    "    secondary_list=[]\n",
    "    \n",
    "    for i in primary_list:\n",
    "        secondary_list.append(primary_contact_employeewise(EvsE_grid, i))\n",
    "        if i in secondary_list:\n",
    "            secondary_list.remove(i)\n",
    "    true_secondary=[]\n",
    "    for k in secondary_list:\n",
    "        for i in k:\n",
    "            true_secondary.append(i)\n",
    "        if Employee_name in true_secondary:\n",
    "            true_secondary.remove(Employee_name)\n",
    "    return list(set(true_secondary))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 367,
   "metadata": {},
   "outputs": [],
   "source": [
    "def secondary_contacts(grid):\n",
    "    secondary_contact_dict={}\n",
    "    employeeslist=grid.index\n",
    "    days_as_series=days_series_creator(grid, employeeslist, workingdays=['Mon','Tue','Wed','Thu','Fri'])\n",
    "    ml=master_list(days_as_series)\n",
    "    EvsE_grid, grid_int_score = populator_fn(ml, employeeslist)\n",
    "    for i in employeeslist:\n",
    "        secondary_contact_dict[i]=secondary_contact_employeewise(EvsE_grid, i)\n",
    "    return secondary_contact_dict\n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "worst_soln_secondary_contact_dict=secondary_contacts(dfb)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "secondary_contacts(dfa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_soln_secondary_contacts_dict=secondary_contacts(dfa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "worst_soln_secondary_contacts_dict=secondary_contacts(dfb)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "best_soln_secondary_contacts_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.Series(best_soln_secondary_contacts_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.Series(primary_contact)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "primary_contacts=pd.Series([])\n",
    "for i in dfa.index:\n",
    "    primary_contacts.append(pd.Series(best_soln_primary_contact_dict[i], index=str(i)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "primary_contacts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "S2=pd.Series(best_soln_secondary_contacts_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "S2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "secondary_contacts(dfb)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "S3=pd.Series(worst_soln_primary_contact_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "S4=pd.Series(worst_soln_secondary_contact_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# S1=pd.Series(best_soln_primary_contact_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# S1.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\Best_sol_Primary_contacts.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# S2.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\Best_sol_Secondary_contacts.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# S3.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\Worst_sol_Primary_contacts.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# S4.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\Worst_sol_Secondary_contacts.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfa.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfc=df[['Emp Names', 'DEPARTMENT']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfc.set_index('Emp Names', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfa="
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfc.set_index('Emp Names')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfa.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfc.DEPARTMENT.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfc[dfc['DEPARTMENT']=='Information Technology']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfa"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 369,
   "metadata": {},
   "outputs": [],
   "source": [
    "new_best_primary_contact_dict=primary_contact(best_overall_grids[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 371,
   "metadata": {},
   "outputs": [],
   "source": [
    "new_best_secondary_contact_dict=secondary_contacts(best_overall_grids[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 372,
   "metadata": {},
   "outputs": [],
   "source": [
    "S5=pd.Series(new_best_primary_contact_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 373,
   "metadata": {},
   "outputs": [],
   "source": [
    "S6=pd.Series(new_best_secondary_contact_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 375,
   "metadata": {},
   "outputs": [],
   "source": [
    "new_worst_primary_contact_dict=primary_contact(worst_overall_grids[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 376,
   "metadata": {},
   "outputs": [],
   "source": [
    "new_worst_secondary_contact_dict=secondary_contacts(worst_overall_grids[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 377,
   "metadata": {},
   "outputs": [],
   "source": [
    "S7=pd.Series(new_worst_primary_contact_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 378,
   "metadata": {},
   "outputs": [],
   "source": [
    "S8=pd.Series(new_worst_secondary_contact_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 379,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_new_best=best_overall_grids[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 380,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_new_worst=worst_overall_grids[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 381,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_new_best.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\70-30_Overall_new_best_sol_354.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 382,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_new_worst.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\70-30_Overall_new_worst_sol_514.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 383,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\PC\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:1: FutureWarning: The signature of `Series.to_csv` was aligned to that of `DataFrame.to_csv`, and argument 'header' will change its default value from False to True: please pass an explicit value to suppress this warning.\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n"
     ]
    }
   ],
   "source": [
    "S5.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\New_Best_sol_354_Primary_contacts.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 384,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\PC\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:1: FutureWarning: The signature of `Series.to_csv` was aligned to that of `DataFrame.to_csv`, and argument 'header' will change its default value from False to True: please pass an explicit value to suppress this warning.\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n"
     ]
    }
   ],
   "source": [
    "S6.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\New_Best_sol_354_Secondary_contacts.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 385,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\PC\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:1: FutureWarning: The signature of `Series.to_csv` was aligned to that of `DataFrame.to_csv`, and argument 'header' will change its default value from False to True: please pass an explicit value to suppress this warning.\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n"
     ]
    }
   ],
   "source": [
    "S7.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\New_Worst_sol_514_Primary_contacts.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 386,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\PC\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:1: FutureWarning: The signature of `Series.to_csv` was aligned to that of `DataFrame.to_csv`, and argument 'header' will change its default value from False to True: please pass an explicit value to suppress this warning.\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n"
     ]
    }
   ],
   "source": [
    "S8.to_csv(r'C:\\Users\\PC\\Desktop\\Sail Analytics\\SAILCOVID\\New_Worst_sol_514_Secondary_contacts.csv', index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 396,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2           Sompop Chang\n",
       "6                Calvin \n",
       "16               Justin \n",
       "24                 Alex \n",
       "37    Massimo Himmelfarb\n",
       "38      Tadamitsu Carrow\n",
       "Name: Emp Names, dtype: object"
      ]
     },
     "execution_count": 396,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Emp Names'][df['DEPARTMENT']=='Finance+Marketing+General Management']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 390,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Inventory & Production                  9\n",
       "Information Technology                  8\n",
       "Supply chain(SCM)                       7\n",
       "Operations                              6\n",
       "Sales                                   6\n",
       "Finance+Marketing+General Management    6\n",
       "Procurement                             5\n",
       "Human Resources                         3\n",
       "Name: DEPARTMENT, dtype: int64"
      ]
     },
     "execution_count": 390,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.DEPARTMENT.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 397,
   "metadata": {},
   "outputs": [],
   "source": [
    "x2=pd.read_excel('C:/Users/PC/Downloads/70-30_Overall_new_best_sol_354_with_teams.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 399,
   "metadata": {},
   "outputs": [],
   "source": [
    "x2.set_index('Emp Name', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 400,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mon</th>\n",
       "      <th>Tue</th>\n",
       "      <th>Wed</th>\n",
       "      <th>Thu</th>\n",
       "      <th>Fri</th>\n",
       "      <th>Team</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Emp Name</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Jax</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Supply chain(SCM)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Barrett</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Supply chain(SCM)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Maximus</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Supply chain(SCM)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Brandon</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Supply chain(SCM)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Brantley</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Supply chain(SCM)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Alejandro</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Supply chain(SCM)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Grant</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Supply chain(SCM)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Vincent</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sales</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Timothy</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Sales</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Luca</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Sales</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Abraham</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Sales</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Finn</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Sales</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jasper</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Sales</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Tara Cantrock</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Joshua</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Caleb</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ryan</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Tanzeer Cao</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ted Brown</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Tae Carrillo</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Thanadtha Brown</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Aaron</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Greyson</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Austin</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ian</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jonathan</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jacob</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jaxson</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Adam</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Adrian</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Sompop Chang</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Finance+Marketing+General Management</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Calvin</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Finance+Marketing+General Management</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Justin</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Finance+Marketing+General Management</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Alex</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Finance+Marketing+General Management</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Massimo Himmelfarb</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Finance+Marketing+General Management</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Tadamitsu Carrow</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Finance+Marketing+General Management</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Michelle Grusq</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Operations</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ryan Cloke</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Operations</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ophir Friedman</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Operations</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Nicole Gao</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Operations</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rui Cockle</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Operations</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Noelle Fu</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Operations</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Philip Druckman</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Procurement</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Patrick Fixler</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Procurement</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Patino Forsyth</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Procurement</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rikin Davis</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Procurement</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Patrick Flegal</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Procurement</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Parker</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Human Resources</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jace</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Human Resources</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Everett</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Human Resources</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    Mon  Tue  Wed  Thu  Fri  \\\n",
       "Emp Name                                      \n",
       "Jax                   0    0    1    0    0   \n",
       "Barrett               1    0    0    0    0   \n",
       "Maximus               0    1    0    1    1   \n",
       "Brandon               0    1    0    1    1   \n",
       "Brantley              1    0    1    0    0   \n",
       "Alejandro             0    0    0    0    0   \n",
       "Grant                 0    0    0    0    0   \n",
       "Vincent               1    1    1    1    1   \n",
       "Timothy               0    1    0    0    1   \n",
       "Luca                  0    0    1    0    0   \n",
       "Abraham               0    0    0    0    0   \n",
       "Finn                  0    1    0    0    1   \n",
       "Jasper                0    0    0    0    0   \n",
       "Tara Cantrock         0    0    0    0    0   \n",
       "Joshua                0    1    1    0    1   \n",
       "Caleb                 1    0    0    0    0   \n",
       "Ryan                  0    0    0    0    0   \n",
       "Tanzeer Cao           0    0    0    1    0   \n",
       "Ted Brown             0    1    0    1    1   \n",
       "Tae Carrillo          0    1    0    1    1   \n",
       "Thanadtha Brown       1    0    1    0    0   \n",
       "Aaron                 0    1    0    1    1   \n",
       "Greyson               0    0    1    0    0   \n",
       "Austin                1    1    0    0    1   \n",
       "Ian                   0    0    0    0    0   \n",
       "Jonathan              0    0    0    0    0   \n",
       "Jacob                 0    1    0    1    1   \n",
       "Jaxson                0    1    1    1    1   \n",
       "Adam                  0    1    1    1    1   \n",
       "Adrian                0    0    0    0    0   \n",
       "Sompop Chang          0    0    0    0    0   \n",
       "Calvin                0    0    0    0    0   \n",
       "Justin                0    1    0    0    1   \n",
       "Alex                  0    1    0    0    1   \n",
       "Massimo Himmelfarb    0    1    0    1    1   \n",
       "Tadamitsu Carrow      0    1    0    1    1   \n",
       "Michelle Grusq        1    0    1    0    0   \n",
       "Ryan Cloke            0    1    0    1    1   \n",
       "Ophir Friedman        0    1    0    1    1   \n",
       "Nicole Gao            0    0    0    0    0   \n",
       "Rui Cockle            0    0    0    0    0   \n",
       "Noelle Fu             0    0    0    1    0   \n",
       "Philip Druckman       0    1    0    1    1   \n",
       "Patrick Fixler        0    0    0    0    0   \n",
       "Patino Forsyth        1    0    1    0    0   \n",
       "Rikin Davis           1    0    0    0    0   \n",
       "Patrick Flegal        0    1    1    1    1   \n",
       "Parker                0    0    0    0    0   \n",
       "Jace                  0    1    0    1    1   \n",
       "Everett               1    0    0    0    0   \n",
       "\n",
       "                                                    Team  \n",
       "Emp Name                                                  \n",
       "Jax                                    Supply chain(SCM)  \n",
       "Barrett                                Supply chain(SCM)  \n",
       "Maximus                                Supply chain(SCM)  \n",
       "Brandon                                Supply chain(SCM)  \n",
       "Brantley                               Supply chain(SCM)  \n",
       "Alejandro                              Supply chain(SCM)  \n",
       "Grant                                  Supply chain(SCM)  \n",
       "Vincent                                            Sales  \n",
       "Timothy                                            Sales  \n",
       "Luca                                               Sales  \n",
       "Abraham                                            Sales  \n",
       "Finn                                               Sales  \n",
       "Jasper                                             Sales  \n",
       "Tara Cantrock                     Information Technology  \n",
       "Joshua                            Information Technology  \n",
       "Caleb                             Information Technology  \n",
       "Ryan                              Information Technology  \n",
       "Tanzeer Cao                       Information Technology  \n",
       "Ted Brown                         Information Technology  \n",
       "Tae Carrillo                      Information Technology  \n",
       "Thanadtha Brown                   Information Technology  \n",
       "Aaron                             Inventory & Production  \n",
       "Greyson                           Inventory & Production  \n",
       "Austin                            Inventory & Production  \n",
       "Ian                               Inventory & Production  \n",
       "Jonathan                          Inventory & Production  \n",
       "Jacob                             Inventory & Production  \n",
       "Jaxson                            Inventory & Production  \n",
       "Adam                              Inventory & Production  \n",
       "Adrian                            Inventory & Production  \n",
       "Sompop Chang        Finance+Marketing+General Management  \n",
       "Calvin              Finance+Marketing+General Management  \n",
       "Justin              Finance+Marketing+General Management  \n",
       "Alex                Finance+Marketing+General Management  \n",
       "Massimo Himmelfarb  Finance+Marketing+General Management  \n",
       "Tadamitsu Carrow    Finance+Marketing+General Management  \n",
       "Michelle Grusq                                Operations  \n",
       "Ryan Cloke                                    Operations  \n",
       "Ophir Friedman                                Operations  \n",
       "Nicole Gao                                    Operations  \n",
       "Rui Cockle                                    Operations  \n",
       "Noelle Fu                                     Operations  \n",
       "Philip Druckman                              Procurement  \n",
       "Patrick Fixler                               Procurement  \n",
       "Patino Forsyth                               Procurement  \n",
       "Rikin Davis                                  Procurement  \n",
       "Patrick Flegal                               Procurement  \n",
       "Parker                                   Human Resources  \n",
       "Jace                                     Human Resources  \n",
       "Everett                                  Human Resources  "
      ]
     },
     "execution_count": 400,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 401,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Information Technology\n",
      "Procurement\n",
      "Supply chain(SCM)\n",
      "Inventory & Production\n",
      "Finance+Marketing+General Management\n",
      "Sales\n",
      "Human Resources\n",
      "Operations\n"
     ]
    }
   ],
   "source": [
    "for i in set(list(x2['Team'])):\n",
    "    print (i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 404,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mon</th>\n",
       "      <th>Tue</th>\n",
       "      <th>Wed</th>\n",
       "      <th>Thu</th>\n",
       "      <th>Fri</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Emp Name</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Philip Druckman</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Patrick Fixler</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Patino Forsyth</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rikin Davis</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Patrick Flegal</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Mon  Tue  Wed  Thu  Fri\n",
       "Emp Name                                \n",
       "Philip Druckman    0    1    0    1    1\n",
       "Patrick Fixler     0    0    0    0    0\n",
       "Patino Forsyth     1    0    1    0    0\n",
       "Rikin Davis        1    0    0    0    0\n",
       "Patrick Flegal     0    1    1    1    1"
      ]
     },
     "execution_count": 404,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x2[['Mon','Tue','Wed','Thu','Fri']][x2['Team']=='Procurement']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 407,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Interaction Score for Information Technology Department is 7.0\n",
      "Interaction Score for Procurement Department is 3.0\n",
      "Interaction Score for Supply chain(SCM) Department is 3.0\n",
      "Interaction Score for Inventory & Production Department is 12.0\n",
      "Interaction Score for Finance+Marketing+General Management Department is 6.0\n",
      "Interaction Score for Sales Department is 4.0\n",
      "Interaction Score for Human Resources Department is 0.0\n",
      "Interaction Score for Operations Department is 3.0\n"
     ]
    }
   ],
   "source": [
    "for i in set(list(x2['Team'])):\n",
    "#     print(x2[['Mon','Tue','Wed','Thu','Fri']][x2['Team']==i])\n",
    "    print ('Interaction Score for {0} Department is {1}'.format(i, grid_eval(x2[['Mon','Tue','Wed','Thu','Fri']][x2['Team']==i])))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 408,
   "metadata": {},
   "outputs": [],
   "source": [
    "x3=pd.read_excel('C:/Users/PC/Downloads/70-30_Overall_new_worst_sol_514.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 410,
   "metadata": {},
   "outputs": [],
   "source": [
    "x3.set_index('Emp Name', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 411,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mon</th>\n",
       "      <th>Tue</th>\n",
       "      <th>Wed</th>\n",
       "      <th>Thu</th>\n",
       "      <th>Fri</th>\n",
       "      <th>Team</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Emp Name</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Michelle Grusq</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Operations</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ryan Cloke</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Operations</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ophir Friedman</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Operations</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Nicole Gao</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Operations</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rui Cockle</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Operations</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Noelle Fu</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Operations</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Aaron</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Greyson</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Austin</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ian</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jonathan</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jacob</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jaxson</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Adam</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Adrian</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Inventory &amp; Production</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Tara Cantrock</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Joshua</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Caleb</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ryan</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Tanzeer Cao</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ted Brown</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Tae Carrillo</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Thanadtha Brown</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Information Technology</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jax</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Supply chain(SCM)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Barrett</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Supply chain(SCM)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Maximus</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Supply chain(SCM)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Brandon</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Supply chain(SCM)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Brantley</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Supply chain(SCM)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Alejandro</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Supply chain(SCM)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Grant</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Supply chain(SCM)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Vincent</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sales</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Timothy</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Sales</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Luca</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Sales</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Abraham</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Sales</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Finn</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sales</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jasper</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Sales</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Sompop Chang</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Finance+Marketing+General Management</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Calvin</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Finance+Marketing+General Management</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Justin</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Finance+Marketing+General Management</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Alex</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Finance+Marketing+General Management</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Massimo Himmelfarb</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Finance+Marketing+General Management</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Tadamitsu Carrow</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Finance+Marketing+General Management</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Philip Druckman</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Procurement</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Patrick Fixler</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Procurement</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Patino Forsyth</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Procurement</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rikin Davis</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Procurement</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Patrick Flegal</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Procurement</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Parker</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Human Resources</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jace</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Human Resources</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Everett</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Human Resources</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    Mon  Tue  Wed  Thu  Fri  \\\n",
       "Emp Name                                      \n",
       "Michelle Grusq        0    0    0    1    1   \n",
       "Ryan Cloke            0    0    1    1    1   \n",
       "Ophir Friedman        0    0    1    1    1   \n",
       "Nicole Gao            0    0    0    0    0   \n",
       "Rui Cockle            0    0    0    0    0   \n",
       "Noelle Fu             0    0    0    1    0   \n",
       "Aaron                 0    0    1    1    1   \n",
       "Greyson               0    0    1    0    0   \n",
       "Austin                1    0    1    1    0   \n",
       "Ian                   0    0    0    0    0   \n",
       "Jonathan              0    0    0    0    0   \n",
       "Jacob                 0    0    1    1    1   \n",
       "Jaxson                1    0    1    1    1   \n",
       "Adam                  1    0    1    1    1   \n",
       "Adrian                0    0    0    0    0   \n",
       "Tara Cantrock         0    0    0    0    0   \n",
       "Joshua                0    0    1    1    1   \n",
       "Caleb                 0    0    0    1    0   \n",
       "Ryan                  0    0    0    0    0   \n",
       "Tanzeer Cao           0    0    0    1    0   \n",
       "Ted Brown             0    1    0    1    1   \n",
       "Tae Carrillo          0    1    0    1    1   \n",
       "Thanadtha Brown       1    0    0    1    0   \n",
       "Jax                   0    0    1    0    0   \n",
       "Barrett               0    0    0    1    0   \n",
       "Maximus               1    1    0    0    1   \n",
       "Brandon               1    1    0    0    1   \n",
       "Brantley              1    0    0    0    1   \n",
       "Alejandro             0    0    0    0    0   \n",
       "Grant                 0    0    0    0    0   \n",
       "Vincent               1    1    1    1    1   \n",
       "Timothy               0    0    1    0    1   \n",
       "Luca                  0    0    0    0    1   \n",
       "Abraham               0    0    0    0    0   \n",
       "Finn                  0    0    0    1    1   \n",
       "Jasper                0    0    0    0    0   \n",
       "Sompop Chang          0    0    0    0    0   \n",
       "Calvin                0    0    0    0    0   \n",
       "Justin                1    0    0    0    1   \n",
       "Alex                  0    1    0    0    1   \n",
       "Massimo Himmelfarb    0    0    1    1    1   \n",
       "Tadamitsu Carrow      0    0    1    1    1   \n",
       "Philip Druckman       0    0    1    1    1   \n",
       "Patrick Fixler        0    0    0    0    0   \n",
       "Patino Forsyth        0    0    0    1    1   \n",
       "Rikin Davis           0    0    0    0    1   \n",
       "Patrick Flegal        1    0    1    1    1   \n",
       "Parker                0    0    0    0    0   \n",
       "Jace                  0    0    1    1    1   \n",
       "Everett               0    0    0    0    1   \n",
       "\n",
       "                                                    Team  \n",
       "Emp Name                                                  \n",
       "Michelle Grusq                                Operations  \n",
       "Ryan Cloke                                    Operations  \n",
       "Ophir Friedman                                Operations  \n",
       "Nicole Gao                                    Operations  \n",
       "Rui Cockle                                    Operations  \n",
       "Noelle Fu                                     Operations  \n",
       "Aaron                             Inventory & Production  \n",
       "Greyson                           Inventory & Production  \n",
       "Austin                            Inventory & Production  \n",
       "Ian                               Inventory & Production  \n",
       "Jonathan                          Inventory & Production  \n",
       "Jacob                             Inventory & Production  \n",
       "Jaxson                            Inventory & Production  \n",
       "Adam                              Inventory & Production  \n",
       "Adrian                            Inventory & Production  \n",
       "Tara Cantrock                     Information Technology  \n",
       "Joshua                            Information Technology  \n",
       "Caleb                             Information Technology  \n",
       "Ryan                              Information Technology  \n",
       "Tanzeer Cao                       Information Technology  \n",
       "Ted Brown                         Information Technology  \n",
       "Tae Carrillo                      Information Technology  \n",
       "Thanadtha Brown                   Information Technology  \n",
       "Jax                                    Supply chain(SCM)  \n",
       "Barrett                                Supply chain(SCM)  \n",
       "Maximus                                Supply chain(SCM)  \n",
       "Brandon                                Supply chain(SCM)  \n",
       "Brantley                               Supply chain(SCM)  \n",
       "Alejandro                              Supply chain(SCM)  \n",
       "Grant                                  Supply chain(SCM)  \n",
       "Vincent                                            Sales  \n",
       "Timothy                                            Sales  \n",
       "Luca                                               Sales  \n",
       "Abraham                                            Sales  \n",
       "Finn                                               Sales  \n",
       "Jasper                                             Sales  \n",
       "Sompop Chang        Finance+Marketing+General Management  \n",
       "Calvin              Finance+Marketing+General Management  \n",
       "Justin              Finance+Marketing+General Management  \n",
       "Alex                Finance+Marketing+General Management  \n",
       "Massimo Himmelfarb  Finance+Marketing+General Management  \n",
       "Tadamitsu Carrow    Finance+Marketing+General Management  \n",
       "Philip Druckman                              Procurement  \n",
       "Patrick Fixler                               Procurement  \n",
       "Patino Forsyth                               Procurement  \n",
       "Rikin Davis                                  Procurement  \n",
       "Patrick Flegal                               Procurement  \n",
       "Parker                                   Human Resources  \n",
       "Jace                                     Human Resources  \n",
       "Everett                                  Human Resources  "
      ]
     },
     "execution_count": 411,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 412,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Interaction Score for Information Technology Department is 15.0\n",
      "Interaction Score for Procurement Department is 6.0\n",
      "Interaction Score for Supply chain(SCM) Department is 3.0\n",
      "Interaction Score for Inventory & Production Department is 15.0\n",
      "Interaction Score for Finance+Marketing+General Management Department is 6.0\n",
      "Interaction Score for Sales Department is 6.0\n",
      "Interaction Score for Human Resources Department is 1.0\n",
      "Interaction Score for Operations Department is 6.0\n"
     ]
    }
   ],
   "source": [
    "for i in set(list(x3['Team'])):\n",
    "#     print(x2[['Mon','Tue','Wed','Thu','Fri']][x2['Team']==i])\n",
    "    print ('Interaction Score for {0} Department is {1}'.format(i, grid_eval(x3[['Mon','Tue','Wed','Thu','Fri']][x3['Team']==i])))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
