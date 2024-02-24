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
    "import mongomock\n",
    "import logging\n",
    "\n",
    "# Configure logging\n",
    "logging.basicConfig(level=logging.INFO)\n",
    "\n",
    "class AnimalShelter(object):\n",
    "    \"\"\"CRUD OPERATIONS for Animal Collection in MongoDB\"\"\"\n",
    "    \n",
    "    def __init__(self, user, password, aacuser, UserCS340, db_connection=None):\n",
    "        # If a mock database connection is provided, use it\n",
    "        # Otherwise, establish a new MongoDB connection with the given credentials\n",
    "        if db_connection:\n",
    "            self.database = db_connection\n",
    "        else:\n",
    "            # Original connection string modified to accept credentials\n",
    "            self.client = MongoClient('mongodb://%s:%s@localhost:53598/AAC' % (aacuser, UserCS340))\n",
    "            self.database = self.client['AAC']\n",
    "\n",
    "        print(\"Connected to Database\")\n",
    "\n",
    "        # Usage in test environment\n",
    "        # Assuming a test environment is required and mongomock needs to be used\n",
    "        \n",
    "    def test_setup():\n",
    "        mock_db = mongomock.MongoClient().AAC\n",
    "        animal_shelter = AnimalShelter(user=\"dummyUser\", password=\"dummyPassword\", aacuser=\"dummyAacuser\", UserCS340=\"dummyUserCS340\", db_connection=mock_db)\n",
    "        # The animal_shelter class can now be used with a mocked database for testing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Implement Create in Crud\n",
    "    def create(self, data):\n",
    "        try:\n",
    "            if data is not None:\n",
    "                insert_result = self.database.animals.insert_one(data)  # data should be dictionary\n",
    "                logging.info(f\"Insert successful, ID: {insert_result.inserted_id}\")\n",
    "                return {'success': True, 'id': insert_result.inserted_id}\n",
    "            else:\n",
    "                # Specific error handling\n",
    "                raise ValueError(\"Nothing to save, data is empty\")\n",
    "        except ValueError as ve:\n",
    "            logging.error(f\"Validation error: {ve}\")\n",
    "            return {'success': False, 'error': str(ve)}\n",
    "        except Exception as e:\n",
    "            logging.error(f\"Unexpected error: {e}\")\n",
    "            return {'success': False, 'error': 'Unexpected error occurred'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Implement Read in Crud\n",
    "    def read(self, criteria):\n",
    "        try:\n",
    "            if criteria is not None:\n",
    "                data = self.database.animals.find(criteria)  # criteria should be a dictionary\n",
    "                results = [item for item in data]\n",
    "                if results:\n",
    "                    logging.info(f\"Read successful, found {len(results)} items\")\n",
    "                else:\n",
    "                    logging.info(\"No items found\")\n",
    "                return {'success': True, 'data': results}\n",
    "            else:\n",
    "                raise ValueError(\"Search criteria is empty\")\n",
    "        except ValueError as ve:\n",
    "            logging.error(f\"Validation error: {ve}\")\n",
    "            return {'success': False, 'error': str(ve)}\n",
    "        except Exception as e:\n",
    "            logging.error(f\"Unexpected error: {e}\")\n",
    "            eturn {'success': False, 'error': 'Unexpected error occurred'}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#U Operation for Update in CRUD\n",
    "    def update(self, criteria, update_data):\n",
    "    try:\n",
    "        if criteria is None or update_data is None:\n",
    "            raise ValueError(\"Update criteria or data to update is missing\")\n",
    "\n",
    "        update_result = self.database.animals.update_many(criteria, {'$set': update_data})\n",
    "        \n",
    "        if update_result.modified_count > 0:\n",
    "            logging.info(f\"Update successful, modified {update_result.modified_count} items\")\n",
    "            return {'success': True, 'modified_count': update_result.modified_count}\n",
    "        else:\n",
    "            logging.info(\"No items updated\")\n",
    "            return {'success': False, 'modified_count': 0}\n",
    "    except ValueError as ve:\n",
    "        logging.error(f\"Validation error: {ve}\")\n",
    "        return {'success': False, 'error': str(ve)}\n",
    "    except Exception as e:\n",
    "        logging.error(f\"Unexpected error: {e}\")\n",
    "        return {'success': False, 'error': 'Unexpected error occurred'}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#D Operation for Delete in CRUD\n",
    "    def delete(self, criteria):\n",
    "    try:\n",
    "        if criteria is None:\n",
    "            raise ValueError(\"Delete criteria is missing\")\n",
    "\n",
    "        delete_result = self.database.animals.delete_many(criteria)\n",
    "\n",
    "        if delete_result.deleted_count > 0:\n",
    "            logging.info(f\"Delete successful, removed {delete_result.deleted_count} items\")\n",
    "            return {'success': True, 'deleted_count': delete_result.deleted_count}\n",
    "        else:\n",
    "            logging.info(\"No items deleted\")\n",
    "            return {'success': False, 'deleted_count': 0}\n",
    "    except ValueError as ve:\n",
    "        logging.error(f\"Validation error: {ve}\")\n",
    "        return {'success': False, 'error': str(ve)}\n",
    "    except Exception as e:\n",
    "        logging.error(f\"Unexpected error: {e}\")\n",
    "        return {'success': False, 'error': 'Unexpected error occurred'}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
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
