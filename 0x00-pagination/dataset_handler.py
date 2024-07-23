# #!/usr/bin/env python3
# """
# Module for handling the loading and cachhing of
# Popular Baby Names dataset
# """

# import csv
# from typing import List, Dict

# DATA_FILE = "Popular_Baby_Names.csv"

# class DatasetHandler:
#     def __init__(self):
#         self.__dataset = None
#         self.__indexed_dataset = None

#     def dataset(self) -> List[List]:
#         """Load and cache the dataset"""
#         if self.__dataset is None:
#             with open(DATA_FILE) as f:
#                 reader = csv.reader(f)
#                 dataset = [row for row in reader]
#             self.__dataset = dataset[1:]  # Skip header
#         return self.__dataset

#     def indexed_dataset(self) -> Dict[int, List]:
#         """Create an indexed dataset"""
#         if self.__indexed_dataset is None:
#             dataset = self.dataset()
#             self.__indexed_dataset = {
#                 i: dataset[i] for i in range(len(dataset))
#             }
#         return self.__indexed_dataset
