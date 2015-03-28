    # This file is part of MultiDrive.

    # MultiDrive is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # MultiDrive is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with MultiDrive.  If not, see <http://www.gnu.org/licenses/>.

from abc import ABCMeta, abstractmethod

class StorageService(object):
	__metaclass__ = ABCMeta


	@abstractmethod
	def authorize(self):
		pass

	@abstractmethod
	def upload(self, file_name, destination=None, modified_time= None, create_folder=False, overwrite=False):
		pass

	@abstractmethod
	def download(self, file_path, destination=None, overwrite = False):
		pass

	@abstractmethod
	def is_folder(self, folder_path):
		pass

	@abstractmethod
	def list_folder(self, folder_path):
		pass