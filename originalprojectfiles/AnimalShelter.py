{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pymongo import MongoClient\n",
    "from bson.objectid import ObjectId\n",
    "\n",
    "class AnimalShelter(object):\n",
    "\n",
    "    \"\"\" CRUD operations for Animal collection in MongoDB \"\"\"\n",
    "\n",
    "    def __init__(self):\n",
    "        # Initializing the MongoClient. This help to\n",
    "        # access the MongoDB databases and collections.\n",
    "        self.client = MongoClient('mongodb://%s:%s@localhost:53598' % (aacuser, UserCS340))\n",
    "        if not self.client:\n",
    "            self.client = MongoClient('mongodb://localhost:53598')\n",
    "            \n",
    "        self.database = self.client['AAC']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "   # Create method to implement the C in CRUD.\n",
    "    def create(self, data):\n",
    "        if data is not None:\n",
    "            insert = self.database.animals.insert(data)  \n",
    "            # data should be dictionary \n",
    "            if insert!=0:\n",
    "                return True\n",
    "            else:\n",
    "                return False           \n",
    "        else:\n",
    "            raise Exception(\"Nothing to save, because data parameter is empty\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "   # Create method to implement the R in CRUD.\n",
    "    def read(self,criteria=None):\n",
    "\n",
    "        # criteria is not None then this find will return all rows which matches the criteria\n",
    "        if criteria:\n",
    "        # {'_id':False} just omits the unique ID of each row        \n",
    "\n",
    "            data = self.database.animals.find(criteria,{\"_id\":False})\n",
    "        else:\n",
    "        #if there is no search criteria then all the rows will be return  \n",
    "            data = self.database.animals.find( {} , {\"_id\":False})\n",
    "\n",
    "        return data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "    # Create method to implement the U in CRUD.\n",
    "    def update(self, update, newUpdate):\n",
    "        if update is not None:\n",
    "            update = self.database.animals.update_one(update, {'$set': newUpdate})\n",
    "            # data shoud be dictionary\n",
    "            print(update) \n",
    "            if update!=0:\n",
    "                return self.database.animals.update_one(update, {'$set': newUpdate})\n",
    "                # data should be dictionary\n",
    "                return True\n",
    "            else:\n",
    "                return jsonify(update)\n",
    "                return False\n",
    "        else:\n",
    "            raise Exception(\"No records to update\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "    # Create method to implement the D in CRUD.\n",
    "    def delete(self, delete):\n",
    "        if delete is not None:\n",
    "            delete = self.database.animals.remove(delete)\n",
    "            # data should be dictionary\n",
    "            if delete!=0:\n",
    "                return jsonify(delete)\n",
    "                return True\n",
    "        else:\n",
    "            raise Exception(\"No records to delete\")"
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
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
