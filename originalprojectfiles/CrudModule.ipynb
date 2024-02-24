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
    "    \"\"\"CRUD OPERATIONS for Animal Collection in MongoDB\"\"\"\n",
    "    \n",
    "    def __init__(self, user, password):\n",
    "        #self.client = MongoClient('mongodb://localhost:53598')\n",
    "        #self.client = MongoClient('mongodb://127.0.0.1:37300/?authSource=AAC&compressors=disabled&gssapiServiceName=mongodb' % (user, password))\n",
    "        self.client = MongoClient('mongodb://%s:%s@localhost:53598/AAC' % (aacuser, UserCS340))\n",
    "        self.database = self.client['AAC']\n",
    "        print(\"Connected to Database\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Implement create in Crud\n",
    "    def create(self, data):\n",
    "        try:\n",
    "            if data is not None:\n",
    "                insert_result = self.database.animals.insert_one(data) #data should be dictionary\n",
    "                print(insert_result)\n",
    "                return True\n",
    "            else:\n",
    "                #Raise error\n",
    "                raise Exception(\"Nothing to save, data is empty\")\n",
    "        except:\n",
    "            return False # return false for bool requirement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Implement read in Crud\n",
    "    def read(self, target):\n",
    "        try:\n",
    "            if target is not None:\n",
    "                read_result = list(self.database.animals.find(target, {\"_id\": False}))\n",
    "                return read_result\n",
    "            else:\n",
    "                raise Exception(\"Nothing to find. Target is empty.\")\n",
    "                return False\n",
    "        except Exception as e:\n",
    "            print(\"Exception has occured: \", e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#U operation for update in CRUD\n",
    "    def update(self, fromTarget, toTarget, count):\n",
    "        if fromTarget is not None:\n",
    "            if count == 1:\n",
    "                update_result = self.database.animals.update(fromTarget, toTarget)\n",
    "                #print(\"Matched Count: \" + str(update_result.matched_count) + \", Modified Count: \" + str(update_result.modified_count))\n",
    "                #if update_result.modified_count == 1:\n",
    "                print(\"Success!\")\n",
    "                print(update_result)\n",
    "                return True\n",
    "                \n",
    "            elif count == 2:\n",
    "                update_result = self.database.animals.update(fromTarget, toTarget)\n",
    "                #print(\"Matched Count: \" + str(update_result.matched_count) + \", Modified Count: \" + str(update_result.modified_count))\n",
    "                #if update_result.modified_count == update_result.matched_count:\n",
    "                print(\"Success!\")\n",
    "                print(update_result)\n",
    "                return True\n",
    "                \n",
    "            else:\n",
    "                print(\"Count not recognized - try again.\")\n",
    "                return False\n",
    "        else:\n",
    "            #lets the user know there was a problem\n",
    "            raise Exception(\"Nothing to update, because at least one of the target parameters is empty\")\n",
    "            return False       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#D operation for delete in CRUD\n",
    "    def deleteData(self, target, count):\n",
    "        if target is not None:\n",
    "            if count == 1:\n",
    "                try:\n",
    "                    delete_result = self.database.animals.delete_one(target)\n",
    "                    #print(\"Deleted Count: \" + str(delete_result.deleted_count))\n",
    "                    print(\"Success!\")\n",
    "                    print(delete_result)\n",
    "                    return True\n",
    "                except Exception as e:\n",
    "                    print(\"An exception has occurred: \", e)\n",
    "            elif count == 2:\n",
    "                try:\n",
    "                    delete_result = self.database.animals.delete_many(target)\n",
    "                    #print(\"Deleted Count: \" + str(delete_result.deleted_count))\n",
    "                    print(\"Success!\")\n",
    "                    print(delete_result)\n",
    "                    return True\n",
    "                except Exception as e:\n",
    "                    print(\"An exception has occurred: \", e)\n",
    "                    return False\n",
    "            else:\n",
    "                print(\"Count not recognized - try again.\")\n",
    "                return False\n",
    "        else:\n",
    "            #lets the user know there was a problem\n",
    "            raise Exception(\"Nothing to delete, because the target parameter is empty\")\n",
    "            return False     "
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
